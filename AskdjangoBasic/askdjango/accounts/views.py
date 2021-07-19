from django.conf import settings
from django.shortcuts import  redirect , render, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login
#함수기반뷰

'''
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST) #signupForm/forms에서 form처리 가능
        if form.is_valid():
            user=form.save()
            #회원가입 후 로그인 처리를 해주어야함
            auth_login(request,user)
            return redirect(profile)
    else:
        form=SignupForm()
    return render(request,'accounts/signup.html',{
        'form':form,
    })
    pass

'''
class SignupView(CreateView):
    model=User
    form_class=SignupForm
    template_name='accounts/signup.html'
    def get_success_url(self):
        return resolve_url('profile')
    def form_valid(self,form):
        user=form.save()
        auth_login(self.request,user)
        return redirect('profile')
signup=SignupView.as_view()

#CLASS기반 뷰
#signup=CreateView.as_view(model=User, form_class= SignupForm ,success_url=settings.LOGIN_URL, template_name='accounts/signup.html')

@login_required   #login 된 상태에서만 view를 호출
def profile(request):
    request.user
    return render(request,'accounts/profile.html')
    
