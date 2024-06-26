from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('rmedic/',views.CreateMedical.as_view(),name="docre"),
    path('authlogin',obtain_auth_token,name="authlogin"),
    path('log',views.log.as_view(),name="authlogin"),
    path('bilcreate/',views.Billcreate.as_view(),name="bilcreate"),
    path('biledphar',views.Billedphar.as_view(),name="bilcreatepharmacy"),
    path('userdta/',views.userdetail.as_view(),name="usrdtail"),
    path('getbill/',views.getbill.as_view(),name="billid"),



    # path('registerphar/',views.CreatePharmacy.as_view(),name="pharcre"),
    path('madin/',views.medicinelisting.as_view(),name="Medicine"),
    path('login/',views.logiin.as_view(),name="login"),
    path('medi/',views.medicinelistview.as_view(),name="login"),
    

    path('token',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name="token_refresh")

    # path('login',views.)
]