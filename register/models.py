from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(unique = True,max_length=20) #닉네임
    age = models.IntegerField() #나이
    instagram_id = models.CharField(unique = True,max_length = 50) #인스타 아이디
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
    # 추가옵션
    hobby = models.CharField(max_length=50) #취미 또는 성격
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])  # 성별(M, F 중에 고를 것)



