from django.contrib import admin
from .models import Symptom, Doctor, History
# Register your models here.

class SymptomAdmin(admin.ModelAdmin):
    list_display=['id', 'symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5']
    
class DoctorAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'department']
    
class HistoryAdmin(admin.ModelAdmin):
    list_display=['id', 'email', 'symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5', 'diseases', 'departments', 'name']
    
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(History, HistoryAdmin)