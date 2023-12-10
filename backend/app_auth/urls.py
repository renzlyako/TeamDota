from django.urls import path
from .views import user_login, user_logout

urlpatterns = [
    path('api/auth/user-login/', user_login, name='user-login'),
    path('user-logout/', user_logout, name='user-logout'),
    # path('knox-login/', UserLoginView.as_view(), name='knox-login'),
    # path('knox-logout/', UserLogoutView.as_view(), name='knox-logout'),
]