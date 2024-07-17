from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, UserPasswordResetSerializer, SendPasswordResetEmailSerializer, AccessCheckSerializer
from django.utils.encoding import smart_str


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


@api_view(['POST'])
def UserRegistrationView(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@renderer_classes([UserRenderer])
def UserLoginView(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
@renderer_classes([UserRenderer])
@permission_classes([IsAuthenticated])
def UserProfileView(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        # print('request.user: '+ smart_str(request.user))
        # print('request.data: '+ smart_str(request.data))
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@renderer_classes([UserRenderer])
@permission_classes([IsAuthenticated])    
def UserChangePasswordView(request):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@renderer_classes([UserRenderer])
def SendPasswordResetEmailView(request):
    if request.method == 'POST':
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@renderer_classes([UserRenderer])
def UserPasswordResetView(request, uid, token):
    if request.method == 'POST':
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@renderer_classes([UserRenderer])
def AccessCheckView(request):
    if request.method == 'POST':
        serializer = AccessCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Authorized user!'}, status=status.HTTP_200_OK)