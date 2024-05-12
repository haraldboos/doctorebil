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
           print(request.user)
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
        print(request.user.id)
        print(request.data)
        dat= {
            'doc_id':request.data['user']['user_id'],
            'subdesies_id': request.data['subdesies_id'],
            'medicine_id': request.data['medicine_id'],
            'days': request.data['days'],
            'note': request.data['note'],
            'smsnumber':request.data['smsnumber'],
            'bilnote':'hihih'
        }
        print(dat,1)
        serializer = CollectionSerilazer(data=dat)
        if serializer.is_valid():
            serializer.save()
            # print({'collid':collection.},111)
            # dat['coll_id']=collection['collid']
            dat['coll_id']=serializer.data['collid']
            print(dat,"first step done")
            print(serializer.data)
            billserlilazer=Billserilazation(data=dat)
            if billserlilazer.is_valid():
                billserlilazer.save()
                print(billserlilazer.data)
                return Response(billserlilazer.data, status=201)
            else:
                print("nononon")



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

class userdetail(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        print(request)
        user_id=request.GET.get('userid')
        print(user_id)
        if not user_id:
            return Response({"error": "User ID (pk) is missing in the request"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = Medical.objects.get(id=user_id)
        except user.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicaluserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # pass

class getbill(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        print(request)
        bill_id=request.GET.get('billid')
        print(bill_id)
        if not bill_id:
            return Response({"error": "User ID (pk) is missing in the request"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            bill = Bill.objects.get(bilid=bill_id)
        except bill.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NormalBillSerilaizer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)
    