from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .serilaizer import *
from .models import * 
# from .authentication import DoctorAuthenticationBackend,PharmacyAuthenticationBackend

class CreateMedical(generics.CreateAPIView):
    queryset = Medical.objects.all()
    serializer_class=MedicalSerializer
    permission_classes=[AllowAny]

class logiin(APIView):
    def post(self, request):
        email=request.data['email']
        password=request.data['password']
        medi = Medical.objects.filter(email=email).first()
        if medi is None:
            raise AuthenticationFailed('your not an Doctor or pharmacy')
        if not medi.check_password(password):
            raise AuthenticationFailed('wrong password')

        return Response({
            'message':'sucess full login',
            'user':medi
        })
class log(APIView):
    def post(self,request):
        user = authenticate(email=request.data['email'],password=request.data['password'])
        if user :
            tkn,created= Token.objects.get_or_create(user=user)
            return Response({'token':tkn})
        else:
            print('failed')


class medicinelistview(generics.CreateAPIView):
    queryset= Medical.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=MedicalSerializer

# class CreatePharmacy(generics.CreateAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = PharmacySerializer
#     permission_classes = [AllowAny]

@api_view(['GET','POST'])
def home(request):
    dc =Medical.objects.all()
    ctor= {'name':'doctor','xxx':'yyyy','fff':'yyyy'}
    return Response(dc)
# def baes([])
class HomeView(APIView):
     
   permission_classes = [IsAuthenticated]
   def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)