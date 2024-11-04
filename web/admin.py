from django.contrib import admin
from .models import Contact, Gallery,Award,GroupOfCompany,Blog, Experience

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =  ("name", "phone")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name" ,)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("name" ,)


@admin.register(GroupOfCompany)
class GroupOfCompanyAdmin(admin.ModelAdmin):
    list_display = ("name" ,)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
