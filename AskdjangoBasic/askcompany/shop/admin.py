from django.contrib import admin
from .models import Item

#등록법1
#admin.site.register(Item) #모델 클래스를 admin에 등록
#등록법2
class ItemAdmin(admin.ModelAdmin):
    list_display=['pk','name','short_desc','price']  
    list_display_links=['name']
    search_fields=['name']
    list_filter=['is_publish','updated_at']
    def short_desc(self,item):
        return item.desc[:20]
    pass

admin.site.register(Item,ItemAdmin)

#등록법3
#@admin.register(Item)
#class ItemAdmin(admin.Model.Admin):
#    pass