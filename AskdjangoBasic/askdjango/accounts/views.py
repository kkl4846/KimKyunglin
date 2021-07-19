from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required   #login 된 상태에서만 view를 호출
def profile(request):
    request.user
    return render(request,'accounts/profile.html')
    
