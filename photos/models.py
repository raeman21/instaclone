from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(blank=True, manual_crop='800x800')
    bio = HTMLField()

    def save_profile(self):
        '''
        This is a function that will save the profile
        '''
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

class Image(models.Model):
    # image_pic = models.ImageField(upload_to = 'p/', default='Image')
    photo = ImageField(blank=True, manual_crop='800x800')
    image_name = models.CharField(max_length = 50)
    image_caption = HTMLField(blank=True)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def save_image(self):
        self.save()
    
    @classmethod
    def update_caption(cls, update):
        pass
    
    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

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
    photo = models.ImageField(upload_to = 'home/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def save_image(self):
        self.save()
    
    @classmethod
    def update_caption(cls, update):
        pass
    
    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

class Comments(models.Model):
    comment = HTMLField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
