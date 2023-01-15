
from .models import TODO
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .permissions import IsOwnerOfObject

# Create your views here.

class TodoListView(ListCreateAPIView):
    queryset=TODO.objects.all()
    serializer_class=TodoSerializer
    permission_classes = [IsAuthenticated,IsOwnerOfObject]

    def get_queryset(self):
        user = self.request.user
        return TODO.objects.filter(owner=user)

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset=TODO.objects.all()
    serializer_class=TodoSerializer
    permission_classes = [IsOwnerOfObject]


    