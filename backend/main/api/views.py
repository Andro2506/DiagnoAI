from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import os
from .serializers import SymptomSerializer, diseaseListSerializer, HistorySerializer, GetdoctorSerializer, docListSerializer
from django.conf import settings
from rest_framework import status
import pandas as pd
from api.models import Doctor

l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
      'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
      'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
      'yellow_crust_ooze']

disease = ['Fungal_infection', 'Allergy', 'GERD', 'Chronic_cholestasis',
           'Drug_Reaction', 'Peptic_ulcer_diseae', 'AIDS', 'Diabetes',
           'Gastroenteritis', 'Bronchial_Asthma', 'Hypertension', 'Migraine',
           'Cervical_spondylosis', 'Paralysis_(brain_hemorrhage)', 'Jaundice',
           'Malaria', 'Chicken_pox', 'Dengue', 'Typhoid', 'hepatitis_A',
           'Hepatitis_B', 'Hepatitis_C', 'Hepatitis_D', 'Hepatitis_E',
           'Alcoholic_hepatitis', 'Tuberculosis', 'Common_Cold', 'Pneumonia',
           'Dimorphic_hemmorhoids(piles)', 'Heart_attack', 'Varicose_veins',
           'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
           'Osteoarthristis', 'Arthritis',
           '(vertigo)_Paroymsal_Positional_Vertigo', 'Acne',
           'Urinary_tract_infection', 'Psoriasis', 'Impetigo']

disease_department = {
    'Fungal_infection': 'Dermatology',
    'Allergy': 'Immunology',
    'GERD': 'Gastroenterology',
    'Chronic_cholestasis': 'Gastroenterology',
    'Drug_Reaction': 'Pharmacology',
    'Peptic_ulcer_diseae': 'Gastroenterology',
    'AIDS': 'Infectious Disease',
    'Diabetes': 'Endocrinology',
    'Gastroenteritis': 'Gastroenterology',
    'Bronchial_Asthma': 'Pulmonology',
    'Hypertension': 'Cardiology',
    'Migraine': 'Neurology',
    'Cervical_spondylosis': 'Orthopedics',
    'Paralysis_(brain_hemorrhage)': 'Neurology',
    'Jaundice': 'Hepatology',
    'Malaria': 'Infectious Disease',
    'Chicken_pox': 'Infectious Disease',
    'Dengue': 'Infectious Disease',
    'Typhoid': 'Infectious Disease',
    'hepatitis_A': 'Hepatology',
    'Hepatitis_B': 'Hepatology',
    'Hepatitis_C': 'Hepatology',
    'Hepatitis_D': 'Hepatology',
    'Hepatitis_E': 'Hepatology',
    'Alcoholic_hepatitis': 'Hepatology',
    'Tuberculosis': 'Pulmonology',
    'Common_Cold': 'General Medicine',
    'Pneumonia': 'Pulmonology',
    'Dimorphic_hemmorhoids(piles)': 'Gastroenterology',
    'Heart_attack': 'Cardiology',
    'Varicose_veins': 'Vascular Surgery',
    'Hypothyroidism': 'Endocrinology',
    'Hyperthyroidism': 'Endocrinology',
    'Hypoglycemia': 'Endocrinology',
    'Osteoarthristis': 'Orthopedics',
    'Arthritis': 'Rheumatology',
    '(vertigo)_Paroymsal_Positional_Vertigo': 'Neurology',
    'Acne': 'Dermatology',
    'Urinary_tract_infection': 'Urology',
    'Psoriasis': 'Dermatology',
    'Impetigo': 'Dermatology'
}

model_path1 = os.path.join(settings.STATIC_ROOT, 'decisionTree_model.sav')
model_path2 = os.path.join(settings.STATIC_ROOT, 'randomForest_model.sav')
model_path3 = os.path.join(settings.STATIC_ROOT, 'knn_model.sav')
model_path4 = os.path.join(settings.STATIC_ROOT, 'gnb_model.sav')


# Create your views here.
@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        l2 = [0] * len(l1)  # Initialize symptom list
        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            input_data = list(serializer.validated_data.values())
            for k in range(0, len(l1)):
                for z in input_data:
                    if z == l1[k]:
                        l2[k] = 1

            inputtest = pd.DataFrame([l2], columns=l1)

            # Load models
            decisionTree_loaded_model = pickle.load(open(model_path1, 'rb'))
            randomForest_loaded_model = pickle.load(open(model_path2, 'rb'))
            knn_loaded_model = pickle.load(open(model_path3, 'rb'))
            gnb_loaded_model = pickle.load(open(model_path4, 'rb'))

            # Make predictions
            predictions = []
            for model in [decisionTree_loaded_model, randomForest_loaded_model, knn_loaded_model, gnb_loaded_model]:
                prediction = model.predict(inputtest)
                predictions.append(prediction[0])

            unique_predictions = list(set(predictions))
            diseases_with_departments = [{
                "disease": disease[i],
                "department": disease_department[disease[i]]
            } for i in unique_predictions]

            # Return response
            list_serializer = diseaseListSerializer(data={"diseases": diseases_with_departments})
            if list_serializer.is_valid():
                return Response(list_serializer.data, status=status.HTTP_200_OK)
            return Response(list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def history(request):
    if request.method == 'POST':
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'history':serializer.data, 'msg':'History created Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def getdoctor(request):
    if request.method == 'POST':
        serializer = GetdoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        department = serializer.validated_data.get('department')
        doctor = Doctor.objects.filter(department=department).values(*[field.name for field in Doctor._meta.get_fields() if field.name != 'id'])
        if not doctor.exists():
            return Response({'message': 'No doctors found in this department'}, status=status.HTTP_400_BAD_REQUEST)
        doctors_list = list(doctor.values('name'))
        list_serializer = docListSerializer(data={"doctors":doctors_list})
        list_serializer.is_valid(raise_exception=True)
        return Response(list_serializer.data, status=status.HTTP_200_OK)
        
    
