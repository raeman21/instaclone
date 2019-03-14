from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings


def post_save_user_model(sender,instance,created,*args,**kwargs):
    if created:
        try: 
            Profile.objects.create(user = instance)
        except:
            pass
post_save.connect(post_save_user_model,sender=settings.AUTH_USER_MODEL)
        

class Profile(models.Model):
    profile_image = models.ImageField(blank=True,upload_to='profiles/')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    follows = models.ManyToManyField(User, related_name='follows' ,blank = True)

    def save_user(self):
        self.save

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
    
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def get_absolute_url(self): 
        return reverse('home')
    
    @classmethod
    def search_profile(cls,name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    


    def __str__(self):
        return self.user.username


class Image(models.Model):
   """
   This is the class we will use to create images
   """
   image_url = models.ImageField(upload_to = "images/")
   name = models.CharField(max_length = 30)
   caption = HTMLField()
   poster = models.ForeignKey(User,related_name='images')
   likes = models.ManyToManyField(User, related_name='likes' ,blank = True)
   date = models.DateTimeField(auto_now_add = True,null = True)

   def save_image(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

   def search_by_user(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images
   
   def total_likes(self):
       return self.likes.count

   @classmethod
   def get_profile_images(cls, poster):
        images = Image.objects.filter(poster__pk = poster)
        return images

   

   def delete_image(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()

   
   def get_absolute_url(self): 
        return reverse('home') 

   @classmethod
   def get_photos(cls):
       return cls.objects.all()

   
   def __str__(self):
       return self.name

class Comments(models.Model):
    text = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    created_date = models.DateTimeField(auto_now_add = True,null = True)
    approved_comment = models.BooleanField(default=False)


 
    def save_comment(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
        
    def __str__(self):
        return self.text

 