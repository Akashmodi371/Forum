from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils import timezone
from .helpers import * 




class Category (models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= 'Categories'   


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, unique=True, null=True , blank=True)
    content = FroalaField()
    bloger = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    category = models. ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)



class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)





# class Comment(models.Model):
#     comments = models.TextField()
#     item = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True, blank="True")
#     author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank="True")
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body