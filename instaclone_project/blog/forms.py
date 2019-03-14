from django import forms
from django.core import validators
from .models import Image,Profile,Comments


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=['likes','poster']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)