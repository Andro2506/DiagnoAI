from rest_framework import serializers
from .models import Symptom, Doctor, History

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'
        
class DiseaseWithDepartmentSerializer(serializers.Serializer):
    disease = serializers.CharField()
    department = serializers.CharField()

class diseaseListSerializer(serializers.Serializer):
    diseases = serializers.ListField(child=DiseaseWithDepartmentSerializer())
    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
        
class GetdoctorSerializer(serializers.Serializer):
    department = serializers.CharField(max_length=255)
    class Meta:
        model=Doctor
        fields=['department']
        
class docSerializer(serializers.Serializer):
    name = serializers.CharField()
    
class docListSerializer(serializers.Serializer):
    doctors = serializers.ListField(child=docSerializer())