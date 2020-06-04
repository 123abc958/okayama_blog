from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #デフォルト関数の読み込み
 
app_name = 'users'
urlpatterns = [
   path('signup/', views.signup, name='signup'),
   path('users/<int:pk>', views.users, name='users'),
   path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),   
]
