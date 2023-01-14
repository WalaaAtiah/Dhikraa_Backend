from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import test
from .permissions import IsOwnerOrReadOnly
from .serializers import testSerializer


class testList(ListCreateAPIView):
    queryset = test.objects.all()
    serializer_class = testSerializer


class testDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = test.objects.all()
    serializer_class = testSerializer
