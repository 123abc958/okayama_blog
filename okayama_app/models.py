from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User #追加

class Tag(models.Model):
    name=models.CharField('タグ名', max_length=255)
    created_at= models.DateTimeField('作成日', default=timezone.now)
    def __str__(self):
        return self.name

class Post(models.Model):
  title = models.CharField('タイトル', max_length=255)
  text = models.TextField('本文')
  image=models.ImageField('画像', upload_to='images', blank=True)
  created_at = models.DateTimeField('作成日', default=timezone.now)
  tag = models.ForeignKey(Tag, verbose_name='タグ', on_delete=models.PROTECT)
  user = models.ForeignKey(User, on_delete=models.CASCADE)#追加

  def __str__(self):
      return self.title
