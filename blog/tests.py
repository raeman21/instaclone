from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Profile,Comments
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.



class ImageTestClass(TestCase):

    def setUp(self):
        self.new_user = User(username = "rae", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_image = Image(name = 'rae', poster = self.new_user)
        self.new_image.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()

    def test_save_image(self):
       
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
    
    def test_init(self):
        self.assertTrue(self.new_image.name =='rae')
    
    def test_delete_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
    
class CommentTestCases(TestCase):
    """
    This is the class I will use to test the comments
    """
    def setUp(self):
        """
        This will create a new comment before every test
        """
        self.new_user = User(username = "rae", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_image = Image(name = 'hey', poster = self.new_user)
        self.new_image.save_image()
        self.new_comment = Comments(text = "Cool", image = self.new_image)
    
       
    
    def test_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_comment, Comments))
    
    def test_init(self):
        self.assertTrue(self.new_comment.text =='Cool')

    
    def tearDown(self):
        """
        This will clear the dbs after each test
        """
    
        Comments.objects.all().delete() 

class ProfileTestClas(TestCase):

    def setUp(self):
        user = User(username='abbyshabi')
        self.profile = Profile(profile_image='yes we can', bio='very awesome', user=user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
    
    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.profile.bio == "very awesome")

    def test_search_users(self):
        """
        This will test whether the search function works
        """
        users = Profile.search_profile("rae")
        self.assertTrue(len(users) == 0)
    
    def test_save_profile(self):
        
        self.profile.save_user()
        self.assertTrue(len(Profile.objects.all()) >= 0)