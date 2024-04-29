from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Medical)
# admin.site.register(Pharmacy)
admin.site.register(Bill)
admin.site.register(collection)
admin.site.register(subdesies)
admin.site.register(Desies)

admin.site.register(medicine)
admin.site.register(billphar)
# admin.site.register(DoctorToken)
# admin.site.register(PharmacyToken)