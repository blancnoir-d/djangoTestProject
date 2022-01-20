from django.db import models
import os
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'


class Alert_history(models.Model):
    date = models.CharField(max_length=30)
    alert_rating = models.FloatField()
    alert_g_spread = models.FloatField()
    alert_bm_spread = models.FloatField()
    alert_ai = models.FloatField()
    alert = models.FloatField()
    total = models.FloatField()
    region = models.FloatField()
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True)  # 새로 작성했을 때 생성
    update_at = models.DateTimeField(auto_now=True)  # 수정했을 때 업데이트
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)  # 이미지
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d', blank=True)  # 파일 업로드를 위한 FileField

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tag = models.ManyToManyField(Tag, blank=True)

    # 이건 뭘까낭? - __str__함수로 모델의 string 표현 방법 정의
    def __str__(self):
        return f'[{self.pk}]{self.date} :: {self.author}'  # self.date 이부분은 특정 데이터의string 설정을 변경하는 거 같다

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 음...
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
