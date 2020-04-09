from django.conf import settings
from django.db import models
from django.utils import timezone

#장고에게 Post가 DB에 저장되어야한다고 알게해준다
class Post(models.Model):
	author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#ForeignKey - 다른 모델에 대한 링크를 의미
	title  =models.CharField(max_length=200)
	#CharField - 글자 수가 제한된 텍스트를 정의할 때 사용
	#TextField - 글자 수 제한 없는 텍스트
	text = models.TextField(null=True)
	created_date = models.DateTimeField(default=timezone.now)
	#DateTimeField - 날짜와 시간을 의미
	published_date= models.DateTimeField(blank=True,null=True)
	
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title
# Create your models here.
