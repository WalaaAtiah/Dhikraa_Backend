from django.shortcuts import render
from .models import Quiz
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import QuizSerializer

# Create your views here.

class QuizListView(ListCreateAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class QuizDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer
    permission_classes = [IsAdminUser]
