from django.urls import path

from accounts.api.views import(
	registration_view,
    ChangePasswordView,
    UpdateProfileView,
    UserViewSet


)

app_name = 'account'

urlpatterns = [
	path('register/', registration_view, name="register"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/<str:username>', UserViewSet.as_view({'get': 'retrieve'})),


]



