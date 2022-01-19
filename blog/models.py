from django.db import models

# Create your models here.
class Alert_history(models.Model):
    date = models.CharField(max_length=30)
    alert_rating = models.FloatField()
    alert_g_spread = models.FloatField()
    alert_bm_spread = models.FloatField()
    alert_ai = models.FloatField()
    alert = models.FloatField()
    total = models.FloatField()
    region= models.FloatField()
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True) # 새로 작성했을 때 생성
    update_at = models.DateTimeField(auto_now=True) # 수정했을 때 업데이트
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d',blank=True) #이미지
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d',blank=True) #파일 업로드를 위한 FileField

    #이건 뭘까낭? - __str__함수로 모델의 string 표현 방법 정의
    def __str__(self):
        return f'[{self.pk}]{self.date}' # self.date 이부분은 특정 데이터의string 설정을 변경하는 거 같다


    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
