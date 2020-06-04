from django.shortcuts import render, redirect, get_object_or_404# 追加
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from okayama_app .models import Post, Tag# 追加
from django.contrib.auth.models import User# 追加
 
# Create your views here.
def signup(request):
   user_form = UserCreationForm(request.POST or None)
   if request.method == "POST" and user_form.is_valid():
       user = user_form.save()
       input_username = user_form.cleaned_data['username']
       input_email = user_form.cleaned_data['email']
       input_password = user_form.cleaned_data['password1']
       user = authenticate(username=input_username, email=input_email, password=input_password)
       login(request, user)
       return redirect('okayama_app:index')
   context = {
       "user_form": user_form,
   }
   return render(request, 'users/signup.html', context)

def users(request, pk):
   user = get_object_or_404(User, pk=pk)
   posts = user.post_set.all().order_by('-created_at')
   return render(request, 'users/users.html', {'user': user, 'posts': posts})
  
