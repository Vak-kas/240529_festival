from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(unique = True,max_length=20) #닉네임
    age = models.IntegerField() #나이
    instagram_id = models.CharField(unique = True,max_length = 50) #인스타 아이디
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
    # 추가옵션
    hobby = models.CharField(max_length=50, blank=True, null=True) #취미 또는 성격
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])  # 성별(M, F 중에 고를 것)

    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
    # 학생회비 관리
    name = models.CharField(max_length = 10) #이름
    created_time = models.DateTimeField(auto_now_add=True)  # 생성 시각
    is_active = models.BooleanField(default=True) #활동, 잠김 여부


