from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, BackUp
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super(UserViewSet, self).create(request, *args, **kwargs)
        # User 모델 인스턴스가 성공적으로 생성된 경우, response의 status 코드 확인
        if response.status_code == status.HTTP_201_CREATED:
            user_data = request.data
            # BackUp 인스턴스 생성
            BackUp.objects.create(
                nickname=user_data.get('nickname'),
                age=user_data.get('age'),
                instagram_id=user_data.get('instagram_id'),
                hobby=user_data.get('hobby'),
                gender=user_data.get('gender'),
                name=user_data.get('name')
            )
        return response
