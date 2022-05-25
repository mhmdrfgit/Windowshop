from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import logging

# Create your views here.
def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST) #adding modified userregisterform
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            #return redirect('blog-home')
            return redirect('login')
    else:
        #user creation forms- default form
        print("form is invalid")
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    logging.getLogger(__name__).info("Profile request")
    if request.method == "POST":
        try:
            #populate the profile info by sending instance as parameter
            print(request.POST)
            print(request.FILES)
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)#additional data image file so expect a FILE also
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated')
                return redirect('profile')
            else:
                messages.error(request, f'form validation failed')
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context=context)



# messages.success
# info,warning,error
