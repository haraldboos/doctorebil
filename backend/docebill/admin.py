from django.contrib import admin
from .models import *
# Register your models here.
class MedicalAdmin(admin.ModelAdmin):
    list_display=['email','username','medireg','is_admin','is_doctor','is_pharmacy']
class BillAdmin(admin.ModelAdmin):
    list_display=['bilid','billdoc','billtime','smsnumber','bilnote']
class CollectionAdmin(admin.ModelAdmin):
    list_display=['collid','subdesies','medicine','days','note','status']
class subdisesAdmin(admin.ModelAdmin):
    list_display=['minidid','maindesis','subdesiesna']
class DeisesAdmin(admin.ModelAdmin):
    list_display=['desiesid','desiesname']
class MedicineAdmin(admin.ModelAdmin):
    list_display=['medineid','medename','adddate','status']
# class BillAdmin(admin.ModelAdmin):
    # list_display=['']
admin.site.register(Medical,MedicalAdmin)
# admin.site.register(Pharmacy)
admin.site.register(Bill,BillAdmin)
admin.site.register(collection,CollectionAdmin)
admin.site.register(subdesies,subdisesAdmin)
admin.site.register(Desies,DeisesAdmin)

admin.site.register(medicine,MedicineAdmin)
admin.site.register(billphar)
# admin.site.register(DoctorToken)
# admin.site.register(PharmacyToken)