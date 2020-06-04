from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Tag
from .forms import PostCreateForm
from django.db.models import Q #追加

 #省略
 #検証用の関数を追加
def is_valid_q(q):
   return q != '' and q is not None
 #関数内の編集
def index(request):
   posts = Post.objects.all().order_by('-created_at')
   title_or_user = request.GET.get('title_or_user')
   date_min = request.GET.get('date_min')
   date_max = request.GET.get('date_max')
   tag = request.GET.get('tag')

   if is_valid_q(title_or_user):
       posts = posts.filter(Q(title__icontains=title_or_user)
                      | Q(user__username__icontains=title_or_user)
                      ).distinct()

   if is_valid_q(date_min):
       posts = posts.filter(created_at__gte=date_min)

   if is_valid_q(date_max):
       posts = posts.filter(created_at__lt=date_max)

   if is_valid_q(tag) and tag != 'タグを選択...':
       posts = posts.filter(tag__name=tag)
   
   return render(request, 'okayama_app/index.html', 
   {'posts': posts, 'title_or_user': title_or_user , 'date_min': date_min, 'date_max': date_max ,'tag': tag})

def add(request):
   if request.method == "POST":
      form = PostCreateForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.user = request.user
         post.save()                    
         return redirect('okayama_app:index')
   else:  
       form = PostCreateForm()
   return render(request, 'okayama_app/add.html', {'form': form})

def edit(request, post_id):
       post = get_object_or_404(Post, id=post_id)
       if request.method == "POST":
           form = PostCreateForm(request.POST, instance=post)
           if form.is_valid():
               form.save()
               return redirect('okayama_app:index')
       else:
               form = PostCreateForm(instance=post)
       return render(request, 'okayama_app/edit.html', {'form': form, 'post':post })

def delete(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   post.delete()
   return redirect('okayama_app:index')

def detail(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   return render(request, 'okayama_app/detail.html', {'post': post})
  
def bootstrap(request):
    return render(request, 'okayama_app/bootstrap.html')