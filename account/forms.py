from django import forms
from .models import Name_Image


class Image_Form(forms.ModelForm):
    class Meta:
        model = Name_Image
        fields = ('name', 'image')