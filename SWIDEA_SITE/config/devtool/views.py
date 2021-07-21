from django.http.response import JsonResponse
from django.shortcuts import render, redirect , resolve_url, get_object_or_404
import json
from .forms import DevtoolForm
from .models import Devtool
from idea.models import Idea
app_name='devtool'
def devtool_list(request):
    all_devtool=Devtool.objects.all()
    return render(request,'devtool/devtool_list.html',{
        'all_devtool':all_devtool,
    })

def devtool_create(request,devtool=None):
    if request.method=='POST':

        form=DevtoolForm(request.POST,request.FILES, instance=devtool)
        if form.is_valid():
            devtool=form.save()
            return redirect('/devtool/'+str(devtool.pk))
    else:
        form=DevtoolForm(instance=devtool)

    return render(request, 'devtool/devtool_create.html', {
        'form':form,
        })


def devtool_detail(request,pk):
    devtool=get_object_or_404(Devtool, pk=pk)
    ideas=devtool.idea_set.all()
    return render(request,'devtool/devtool_detail.html',{
        'devtool':devtool,
        'ideas':ideas,
    })

def devtool_update(request,pk):
    devtool = get_object_or_404(Devtool, pk=pk)
    return devtool_create(request, devtool)

def devtool_delete(request,pk):
    devtool = get_object_or_404(Devtool, pk=pk)
    devtool.delete()
    return redirect('devtool:devtool_list')
