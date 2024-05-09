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
    permission_classes=[AllowAny]
    serializer_class=MedicinSerializer

@api_view(['GET'])
def mideview(request):
    medicine=medicine.objects.all()
    return medicine
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
   
class medicinelisting(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
           Medicine_queryset=medicine.objects.filter(status=True)
           medicine_serializer=MedicinSerializer(Medicine_queryset,many=True)
           subdesies_query=subdesies.objects.all()
           subdesies_serilzer=SubdiseSerializer(subdesies_query,many=True)
           response_data={
               'medicine': medicine_serializer.data,
               'desies':subdesies_serilzer.data

           }
           return Response(response_data)
    def post(self, request):
        serializer = CollectionSerilazer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            print(serializer.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

        #    return Response(request)
class Billcreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        queryset = Bill.objects.all()
        serializers=Billserilazation(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Billedphar(APIView):
        permission_classes = [AllowAny]
        def post(self,request):
            queryset = billphar.objectss.all()
            for x in request:
                print(x)
            serializers=Pharmacyserlizer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                print(serializers.data)
                return Response(serializers.data)

