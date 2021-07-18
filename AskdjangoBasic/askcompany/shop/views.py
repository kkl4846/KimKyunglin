from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, redirect , resolve_url, get_object_or_404
from shop.models import Item
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Item
import re

#07강 http 상태코드로 응답
#200번대: 성공 300번대: 요청을 마치기 위해ㅣ 추가동작 400번대: 클라이언트측 오류 500번대 서버측 오류(indexerror,keyerror,django,db,models.objectdoesnotexist등)

#200번대 
def view1(request):
    return HttpResponse('Hello, Ask Company')
def view2(request):
    return render(request, 'template.html')
def view3(request):
    return JsonResponse({'hello': 'Ask Company'}) #객체를 문자열로 변환한다음 return 해야하는데 이때 response를 사용하면 내부적으로 변환해줌

#302 응답하는 예시
def view1(request):
    return HttpResponseRedirect('/shop/')

def view2(request):
    url=resolve_url('shop:item_list')
    return HttpResponseRedirect(url)
def view3(request):                         #view2 코드를 한줄로
    return redirect('shop:item_list')

#404 응답하는 예시  try except를 통해 item이 없을 때 오류를 잡을 수 있다. or get_object_or_404의 조건을 통해
def view1(request):  
    try:
        item=Item.objects.get(pk=100)
    except Item.DoesNotExist:
        raise Http404
def view2(request):
    item=get_object_or_404(Item,pk=100)
def view3(request):
    try:
        item-Item.objects.get(pk=100)
    except Item.DoesNotExist:
        return HttpResponseNotFound()

#500 응답하는 에시
def view1(request):
    name=['Tom','Steve'][100] #idex error

    item=Item.objects.get(pk=100) # item레코드가 없거나 1개 있을 때 dosenotExist 예외  그이상이면 multipleObjectsReturn

def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs=Item.objects.all()  #model에서 Item 선언해줘야함
    
    q=request.GET.get('q','')
    if q:
        qs=qs.filter(name__icontains=q)  #대소문자 구별하지 않겠따.
    return render(request,'shop/item_list.html', {
        'item_list': qs, 

        })

def item_detail(request,pk):
    item=get_object_or_404(Item, pk=pk)
    return render(request,'shop/item_detail.html',{
        'item': item,
    })

def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')
        is_publish = data.get('is_publish') in (True, 't', 'True', '1')

        # 유효성 검사
        if len(name) < 5:
            error_list.append('name을 5글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.desc = desc
            item.price = price
            item.is_publish = is_publish

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                return redirect(item)

        initial = {
            'name': name,
            'desc': desc,
            'price': price,
            'photo': photo,
            'is_publish': is_publish,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
                'is_publish': item.is_publish,
            }

    return render(request, 'shop/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)