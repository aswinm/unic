from django.contrib import admin
from enquiry.models import Enquiry

class EnqAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enquiry,EnqAdmin)

# Register your models here.
