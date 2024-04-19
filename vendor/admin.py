from django.contrib import admin
from vendor.models import vendor
from vendor.models import services
# Register your models here.

admin.site.register(vendor)
admin.site.register(services)