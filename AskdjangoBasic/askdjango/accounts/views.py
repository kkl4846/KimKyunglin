from django.conf import settings
from django.shortcuts import  redirect , render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
#함수기반뷰
'''
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST) #signupForm/forms에서 form처리 가능
        if form.is_valid():
            user=form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form=SignupForm()
    return render(request,'accounts/signup.html',{
        'form':form,
    })
    pass
'''
#CLASS기반 뷰
signup=CreateView.as_view(model=User, form_class= SignupForm ,success_url=settings.LOGIN_URL, template_name='accounts/signup.html')

@login_required   #login 된 상태에서만 view를 호출
def profile(request):
    request.user
    return render(request,'accounts/profile.html')
    
