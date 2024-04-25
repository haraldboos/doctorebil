# # from  mongoengine import Document,StringField,IntField
from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from rest_framework.authtoken.models import Token
import random

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You must have enter the email address')
        if not username:
            raise ValueError('you must have a usernmame')
        user = self.model(
            email=self.normalize_email(email),
            username=username,

        )
        user.set_password(password)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(
        email = self.normalize_email(email),
        username=username,
        password=password,
        )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Doctor(AbstractBaseUser):
    email = models.EmailField(verbose_name="enter ur contact email",max_length=60,unique=True)
    username= models.CharField(max_length=30,unique=True)
    medireg = models.CharField(verbose_name="enter ur medical identification number",max_length=20,unique=True)
    clinic = models.CharField(verbose_name="enter ur clinic name",max_length=30)
    clinicreg = models.CharField(verbose_name="enter ur clinic registration number",unique=True,max_length=10)
    date_joined= models.DateTimeField(verbose_name="datejoined",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects = UserManager()
    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Pharmacy(AbstractBaseUser):
    email = models.EmailField(verbose_name="enter ur contact email",max_length=60,unique=True)
    username= models.CharField(max_length=30,unique=True)
    medireg = models.CharField(verbose_name="enter ur medical identification number",max_length=20,unique=True)
    clinic = models.CharField(verbose_name="enter ur clinic name",max_length=30)
    clinicreg = models.CharField(verbose_name="enter ur clinic registration number",unique=True,max_length=10)
    date_joined= models.DateTimeField(verbose_name="datejoined",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects = UserManager()

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Desies(models.Model):
    desiesid=models.AutoField(primary_key=True,unique=True)
    desiesname=models.CharField(unique=True,max_length=20,verbose_name="enter the disese name")

    def __str__(self):
        return str(self.desiesid)
class subdesies(models.Model):
    minidid=models.AutoField(primary_key=True,unique=True)
    maindesis=models.ForeignKey(Desies,on_delete=models.CASCADE)
    subdesiesna = models.CharField(max_length=45,default=None)

class medicine(models.Model):
    medineid=models.AutoField(primary_key=True,unique=True)
    medename = models.CharField(max_length=30,verbose_name="enter the medicine name",unique=True)
    adddate = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.medineid)
class collection(models.Model):
    collid=models.AutoField(primary_key=True,unique=True)
    subdesies=models.ForeignKey(subdesies,on_delete=models.CASCADE)
    medicine = models.ForeignKey(medicine,on_delete=models.CASCADE)
    days= models.PositiveIntegerField(blank=True)
    note = models.CharField(max_length=100,blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.collid)


# class mdicaus


class Bill(models.Model):
    bilid=models.IntegerField(unique=True,default=random.randint(10000,99999))
    billdoc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    billtime= models.DateTimeField(auto_now_add=True)
    smsnumber=models.CharField(max_length=10,default=None)
    bilnote = models.TextField(max_length=100,default=None,blank=True)
    medicine = models.ManyToManyField(collection)
    
    def __str__(self):
       return str(self.bilid)
class billphar(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    collid = models.ForeignKey(collection,on_delete=models.CASCADE)
    billedpharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)

class DoctorToken(Token):
    doctor = models.OneToOneField(Doctor, related_name='doctor_auth_token', on_delete=models.CASCADE)
    
class PharmacyToken(Token):
    pharmacy = models.OneToOneField(Pharmacy, related_name='pharmacy_auth_token', on_delete=models.CASCADE)
