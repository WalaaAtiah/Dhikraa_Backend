
from django.urls import path
from accounts.api.views import(
	registration_view,

)

app_name = 'account'

urlpatterns = [
	path('register/', registration_view, name="register"),
]




# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import SignUpView

# urlpatterns = [
#     path('signup/', SignUpView.as_view()),

# ]


















