#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser #장고에서 사용하는 기본유저모델
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta: #DB테이블의 이름지정해주는 정보 / 즉 데이터베이스에 정보넣어주는역할
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
