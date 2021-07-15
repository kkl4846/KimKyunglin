from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Item
# Create your views here.

#06강- view 호출 시, 인자
#1번째 인자: Httprequest 객체 / 현재 요청에 대한 모든 내역을 담고 있다
#2번째~ 인자: 현재 요청의 url로부터 capture된 문자열들
#url/re_path 를 통한 처리에서는 -> 모든 인자는 str타입으로 전달
#path를 통한 처리에서는 매핑된 converter의 to_python에 맞게 변환된 값이 인자로 전달

#return값은 HttpResponse의 객체이어야한다.


#request.method --> GET ,POST인지 알 수 있다.
#request.META 메타 정보를 알 수 있다.
def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs=Item.objects.all()  #model에서 Item 선언해줘야함
    return render(request,'shop/item_list.html',{
        'item_list':qs, 
        })