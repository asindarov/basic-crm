from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(User)

