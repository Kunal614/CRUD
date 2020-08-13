from django.shortcuts import render , HttpResponseRedirect

# Create your views here.
from .forms import studentRegister , SignupForm , AuthForm , Changepass , UserForm

from django.contrib import messages
from django.urls import reverse
from .models import user

# from django.contrib.auth.forms import UserChangeForm


from django.contrib.auth import authenticate , login as dj_login , logout , update_session_auth_hash



#signup
def sign_up(request):
    
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully !!')
            fm = SignupForm() 
            return HttpResponseRedirect('/login/') 
    else:
        fm = SignupForm()        


    return render(request , 'enroll/signup_in.html',{'form':fm})



#This function will add new item and show all item
def add_show(request , id):
    if request.user.is_authenticated:

        if request.user.is_authenticated:
            if request.method == 'POST':
                fm = studentRegister(request.POST)
                if fm.is_valid():
                    nm = fm.cleaned_data['name']
                    em = fm.cleaned_data['email']
                    cla = fm.cleaned_data['Class']
                    com = fm.cleaned_data['Comments']

                    reg = user(name=nm , email=em , Class=cla,Comments=com)
                    reg.save()
                    fm = studentRegister()
                    # fm.save() or only this
            else:
                fm = studentRegister()
            stud = user.objects.all()
        return render(request,'enroll/add_show.html'  ,{'form':fm,'stu':stud}  )
    else:
        return HttpResponseRedirect('/')   

#this function will delete
def delete_data(request , id):
    if request.method == 'POST':
        de = user.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect(reverse('AddShow', kwargs={'id': request.user.id}))

#update
def update_data(request , id):
   
    if request.method == 'POST':
        
        pi = user.objects.get(pk=id)
        print(pi)
        fm = studentRegister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('AddShow', kwargs={'id': request.user.id}))    
    else:
        pi = user.objects.get(pk=id)
        fm = studentRegister(instance=pi)
      
    context = {
        'form':fm
    }
    return render(request , 'enroll/update.html' , context)


#login
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # fm = AuthenticationForm(request=request , data=request.POST)
            fm = AuthForm(request=request , data=request.POST)

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    dj_login(request, user)
                    messages.success(request , 'Login Successfully !! ')
                    return HttpResponseRedirect(reverse('AddShow', kwargs={'id': user.id}))
            
        else:
            # fm = AuthenticationForm()
            fm = AuthForm()

        return render(request , 'enroll/signup_in.html',{'form1':fm})
    else:
        return HttpResponseRedirect(reverse('AddShow', kwargs={'id': request.user.id}))

#profile

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserForm(request.POST , instance=request.user)
            if fm.is_valid():
                messages.success(request , "Profile Updated")
                fm.save()
        else:
            fm = UserForm(instance=request.user)
        return render(request , 'enroll/profile.html', {'name':request.user , 'form':fm}) 
    else:
        return HttpResponseRedirect('/')    


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Changepass(user=request.user , data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/profile/')
        else:        
            fm = Changepass(user = request.user)
    else:
       return HttpResponseRedirect('/')        

    return render(request , 'enroll/changepass.html', {'form':fm})


def home(request):
    return render(request , 'enroll/home.html')