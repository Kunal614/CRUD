from django.shortcuts import render , HttpResponseRedirect

# Create your views here.
from .forms import studentRegister , SignupForm
from django.contrib import messages

from .models import user





def sign_up(request):
    
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully !!')
            fm = SignupForm()  
    else:
        fm = SignupForm()        


    

    return render(request , 'enroll/signup.html',{'form':fm})



#This function will add new item and show all item
def add_show(request):
   
    if request.method == 'POST':
        fm = studentRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = user(name=nm , email=em , password=pw)
            reg.save()
            fm = studentRegister()
            # fm.save() or only this
    else:
        fm = studentRegister()
    stud = user.objects.all()
    
  
    
    return render(request,'enroll/add_show.html'  ,{'form':fm,'stu':stud}  )

#this function will delete
def delete_data(request , id):
    if request.method == 'POST':
        de = user.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

def update_data(request , id):

    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = studentRegister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')    
    else:
        pi = user.objects.get(pk=id)
        fm = studentRegister(instance=pi)
    context = {
        'form':fm
    }
    return render(request , 'enroll/update.html' , context)
