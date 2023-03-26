from django.contrib import admin

# Register your models here.

from . import models as p_models

admin.site.register(p_models.Office)
admin.site.register(p_models.PerformanceMetric)
