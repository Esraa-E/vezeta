from django.contrib import admin

# Register your models here.
from .models import profile,reservation,comment
admin.site.register(profile)
admin.site.register(reservation)
admin.site.register(comment)