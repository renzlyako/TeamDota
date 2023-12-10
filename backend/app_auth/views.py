from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView
from rest_framework.response import Response
from knox.models import AuthToken

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        token, _ = AuthToken.objects.create(user)

        return JsonResponse({'success': True, 'message': 'Login successful', 'token': str(token)})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=401)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):

    logout(request)

    knox_logout_view = KnoxLogoutView()
    return knox_logout_view.post(request, format=None)    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user

    profile_data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    return Response(profile_data)
