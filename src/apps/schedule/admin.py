from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Period, Audience, DataConfig


admin.site.register(Period)
admin.site.register(Audience)
admin.site.register(DataConfig, SingletonModelAdmin)
