from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='home/')
    bio = models.CharField(max_length=50)

    def save_profile(self):
        '''
        This is a function that will save the profile
        '''
        self.save()

    def update_profile(self):
        '''
        This is a function that will update the profile
        '''
        self.update()

    def delete_profile(self):
        '''
        This is a function that will delete the profile once created
        '''
        self.delete()

    

class Image(models.Model):
    image = models.ImageField(upload_to = 'home/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile = models.ForeignKey(profile)
    likes = models.IntegerField()
    comments = models.TextField()
