from django.contrib import admin
from .models import Contact, Gallery,Award,GroupOfCompany,Blog, Experience

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =  ("name", "phone")


admin.site.register(Gallery)
admin.site.register(Award)
admin.site.register(GroupOfCompany)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)

admin.site.register(Experience)
