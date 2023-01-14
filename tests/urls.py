from django.urls import path
from .views import testList, testDetail

urlpatterns = [
    path("", testList.as_view(), name="test_list"),
    path("<int:pk>/", testDetail.as_view(), name="test_detail"),
]
