from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Visitor(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])  # 성별(M, F 중에 고를 것)
    age = models.IntegerField()
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
    # 추가옵션
    keyword = models.CharField(max_length=50) #검색어 입력
    type = models.CharField(max_length=1, choices=[("A", "all"), ("O", "opposite")])

    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#
    # 학생회비 관리
    name = models.CharField(max_length = 10) #이름
    created_time = models.DateTimeField(auto_now_add=True)  # 생성 시각



