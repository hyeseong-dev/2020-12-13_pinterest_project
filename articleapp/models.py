from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    writer =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article') # 유저가 탈퇴해도 게시글을 삭제하지 않고 그냥 유저 알수 없음?과 같이 표기함
                                                                # related_name이 article인 이유는 User객체에서 Article로 접근하는것이 영문 어순에 부합함.
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False) # 이미지는 반드시 넣어야함 null값 False이므로
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)



