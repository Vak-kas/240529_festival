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

            base_query = User.objects.filter(is_active=True, age__range=(age - age_range, age + age_range))
            if keyword:
                tmp = base_query.filter(hobby__icontains=keyword)
                if tmp.exists():
                    base_query = tmp

            if type == 'A':
                if base_query.exists():
                    user = random.choice(list(base_query))
                    response_serializer = UserSerializer(user)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "매칭된 사람 없음"}, status=status.HTTP_404_NOT_FOUND)

            elif type == 'O':
                filtered_users = base_query.filter(gender=opposite_gender)
                if filtered_users.exists():
                    user = random.choice(list(filtered_users))
                    user.is_active = False  # Set is_active to False instead of deleting
                    user.save()  # Save the change to the database
                    response_serializer = UserSerializer(user)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "매칭된 사람 없음"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
