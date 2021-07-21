from django.http.response import JsonResponse
from django.shortcuts import render, redirect , resolve_url, get_object_or_404
from .models import Idea
import json
from .forms import IdeaForm

def idea_list(request):
    all_idea=Idea.objects.all()
    #interest=request.GET['interest']   #아이디어가 여러개니까 INTEREST도 여러개여서 생기는 문제
    ctx={
        'all_idea':all_idea,
        
    }
    return render(request,'idea/idea_list.html',ctx)
'''
def idea_interest(request):
    jsonObject=json.loads(request.body)
    Idea.interest=jsonObject.get('number')
    return JsonResponse(jsonObject)
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
            item=form.save()
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



