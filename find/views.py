from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Visitor
from register.models import User
from .serializers import VisitorSerializer
from register.serializers import UserSerializer
import random

class VisitorAPIView(APIView):
    def post(self, request):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            type = serializer.validated_data['type']
            age = serializer.validated_data['age']
            keyword = serializer.validated_data.get('keyword', None)
            gender = serializer.validated_data['gender']
            age_range = 3
            opposite_gender = 'M' if gender == 'F' else 'F'

            base_query = User.objects.filter(age__range=(age - age_range, age + age_range))
            if keyword:
                base_query = base_query.filter(hobby__icontains=keyword)

            if type == 'A':
                if base_query.exists():
                    user = random.choice(list(base_query))
                    response_serializer = UserSerializer(user)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"에러": "매칭되고 있는 사람이 없네요. 다시 시도해주세요"}, status=status.HTTP_404_NOT_FOUND)

            elif type == 'O':
                filtered_users = base_query.filter(gender=opposite_gender)
                if filtered_users.exists():
                    user = random.choice(list(filtered_users))
                    response_serializer = UserSerializer(user)
                    user.delete()
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"에러": "매칭되고 있는 사람이 없네요. 다시 시도해주세요"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
