from django.urls import path
from .import views
app_name='okayama_app'
urlpatterns=[
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    #練習用
    path('bootstrap/', views.bootstrap, name='bootstrap'),

]