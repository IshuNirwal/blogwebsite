from django.contrib import admin
from .models import *

# for configuration of category admin.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','description','url','image_tag','add_date')
    search_fields=('title',)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','url','image_tag','post_id')
    search_fields=('title',)
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ContactEnquiry)
admin.site.register(HandleRequest)
admin.site.register(Comment)
