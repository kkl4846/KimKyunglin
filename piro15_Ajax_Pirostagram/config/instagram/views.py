from django.shortcuts import get_object_or_404, render, redirect
from .models import Post,Comment
from .forms import PostForm
from django.urls import reverse


def post_list(request):
    all_post=Post.objects.all()
    all_comment=Comment.objects.all()
    return render(request,'instagram/post_list.html',{
        'all_post':all_post,
        'all_comment':all_comment
    })


def post_create(request,post=None):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('instagram:post_list') #return redirect('/')
    else:
        form=PostForm(instance=post)
    return render(request,'instagram/post_form.html',{
        'form':form,
    })


import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)   
    post_id=req['id']
    type=req['type']

    post=Post.objects.get(id=post_id)

    if type=='like':
        post.like=0 #'🤍'
    else:
        post.like=1 #'❤️'
    post.save()

    return JsonResponse({'id':post_id,'type':type}) 

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name="dispatch")
def comment_create(request):
    req = json.loads(request.body)   
    Post_id = req['id_comment']
    post = Post.objects.get(id=Post_id)
    content = req['comment_content']
    new_comment = Comment(comment_content = content,post=post)
    new_comment.save()

    return JsonResponse({'post_id':Post_id,'comment_content':content , 'comment_id':new_comment.id}) 

def comment_delete(request):
    req = json.loads(request.body)   
    comment_id = req['comment_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'comment_id':comment_id}) 




