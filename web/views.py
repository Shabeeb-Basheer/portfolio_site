import json
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .models import Gallery, Blog, Experience, Award, GroupOfCompany


def index(request):
    galleries = Gallery.objects.all()[:4]
    blogs = Blog.objects.all()[:4]
    context = {
        "is_index": True,
        "galleries": galleries,
        "blogs": blogs
        }
    return render(request, "web/index.html", context)


def about(request):
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    groupofcompanies = GroupOfCompany.objects.all()
    context = {
        "is_about": True,
        "experiences": experiences,
        "awards": awards,
        "groupofcompanies": groupofcompanies
        }
    return render(request, "web/about.html", context)


def gallery(request):
    galleries = Gallery.objects.all()
    context = {
        "is_gallery": True,
        "galleries": galleries,
        }  
    return render(request, "web/gallery.html", context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"is_blog": True,
               "blogs": blogs}
    return render(request, "web/blog.html", context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)
    context = {
        "is_blog": True,
        "blog": blog,
        "other_blogs": other_blogs,
    }
    return render(request, "web/blog_details.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)