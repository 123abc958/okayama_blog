from django import forms
from .models import Post, Tag
from django.forms import ModelForm
 
class PostCreateForm(forms.ModelForm):   
   class Meta:
       model = Post
       fields = ['title', 'text', 'tag']
