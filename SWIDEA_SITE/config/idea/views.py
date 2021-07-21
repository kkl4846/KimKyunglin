from django.http.response import JsonResponse
from django.shortcuts import render, redirect , resolve_url, get_object_or_404
from .models import Idea
import json
from .forms import IdeaForm
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def idea_list(request):
    all_idea=Idea.objects.all()
    ctx={
        'all_idea':all_idea,
        
    }
    return render(request,'idea/idea_list.html',ctx)

'''
def idea_interest(request):
        p=request.POST.get('pk',None)
        i=request.POST.get('interest',None)
        idea = get_object_or_404(Idea, pk=p)
        idea.interest=i
        idea.save()
        ctx={
        'pk':p,
        'interest':idea.interest,
        
        }
        return render(request,'idea/idea_list.html',ctx)

'''


def idea_detail(request,pk):
    idea=get_object_or_404(Idea, pk=pk)
    devtool=idea.devtool
    return render(request,'idea/idea_detail.html',{
        'idea':idea,
        'devtool':devtool,
    })

def idea_create(request,idea=None): 
    if request.method=='POST':

        form=IdeaForm(request.POST,request.FILES, instance=idea)
        if form.is_valid():
            idea=form.save()
            return redirect('/idea/'+str(idea.pk))
    else:
        form=IdeaForm(instance=idea)

    return render(request, 'idea/idea_form.html', {
        'form':form,
        })
 

def idea_update(request,pk):
    idea = get_object_or_404(Idea, pk=pk)
    return idea_create(request,idea)

def idea_delete(request,pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('idea:idea_list')



