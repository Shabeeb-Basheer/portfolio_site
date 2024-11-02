from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='awards/', null=True, blank=True)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='galleries/', null=True, blank=True)

    def __str__(self):
        return self.name

class GroupOfCompany(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='groupofcompanies/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self): 
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse_lazy("web:blog_details", kwargs={"slug": self.slug})
    
    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):      
        return self.title
    
class Experience(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    startdate = models.CharField(max_length=100)
    enddate = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name