from django.contrib import admin #admin툴을 사용하겠다
from .models import UserModel#우리가 생성한 모델 갖고오기

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다