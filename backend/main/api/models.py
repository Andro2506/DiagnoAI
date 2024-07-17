from django.db import models
# Create your models here.


class Symptom(models.Model):
    BACK_PAIN = 'back_pain'
    CONSTIPATION = 'constipation'
    ABDOMINAL_PAIN = 'abdominal_pain'
    DIARRHOEA = 'diarrhoea'
    MILD_FEVER = 'mild_fever'
    YELLOW_URINE = 'yellow_urine'
    YELLOWING_OF_EYES = 'yellowing_of_eyes'
    ACUTE_LIVER_FAILURE = 'acute_liver_failure'
    FLUID_OVERLOAD = 'fluid_overload'
    SWELLING_OF_STOMACH = 'swelling_of_stomach'
    SWELLED_LYMPH_NODES = 'swelled_lymph_nodes'
    MALAISE = 'malaise'
    BLURRED_AND_DISTORTED_VISION = 'blurred_and_distorted_vision'
    PHLEGM = 'phlegm'
    THROAT_IRRITATION = 'throat_irritation'
    REDNESS_OF_EYES = 'redness_of_eyes'
    SINUS_PRESSURE = 'sinus_pressure'
    RUNNY_NOSE = 'runny_nose'
    CONGESTION = 'congestion'
    CHEST_PAIN = 'chest_pain'
    WEAKNESS_IN_LIMBS = 'weakness_in_limbs'
    FAST_HEART_RATE = 'fast_heart_rate'
    PAIN_DURING_BOWEL_MOVEMENTS = 'pain_during_bowel_movements'
    PAIN_IN_ANAL_REGION = 'pain_in_anal_region'
    BLOODY_STOOL = 'bloody_stool'
    IRRITATION_IN_ANUS = 'irritation_in_anus'
    NECK_PAIN = 'neck_pain'
    DIZZINESS = 'dizziness'
    CRAMPS = 'cramps'
    BRUISING = 'bruising'
    OBESITY = 'obesity'
    SWOLLEN_LEGS = 'swollen_legs'
    SWOLLEN_BLOOD_VESSELS = 'swollen_blood_vessels'
    PUFFY_FACE_AND_EYES = 'puffy_face_and_eyes'
    ENLARGED_THYROID = 'enlarged_thyroid'
    BRITTLE_NAILS = 'brittle_nails'
    SWOLLEN_EXTREMETIES = 'swollen_extremeties'
    EXCESSIVE_HUNGER = 'excessive_hunger'
    EXTRA_MARITAL_CONTACTS = 'extra_marital_contacts'
    DRYING_AND_TINGLING_LIPS = 'drying_and_tingling_lips'
    SLURRED_SPEECH = 'slurred_speech'
    KNEE_PAIN = 'knee_pain'
    HIP_JOINT_PAIN = 'hip_joint_pain'
    MUSCLE_WEAKNESS = 'muscle_weakness'
    STIFF_NECK = 'stiff_neck'
    SWELLING_JOINTS = 'swelling_joints'
    MOVEMENT_STIFFNESS = 'movement_stiffness'
    SPINNING_MOVEMENTS = 'spinning_movements'
    LOSS_OF_BALANCE = 'loss_of_balance'
    UNSTEADINESS = 'unsteadiness'
    WEAKNESS_OF_ONE_BODY_SIDE = 'weakness_of_one_body_side'
    LOSS_OF_SMELL = 'loss_of_smell'
    BLADDER_DISCOMFORT = 'bladder_discomfort'
    FOUL_SMELL_OF_URINE = 'foul_smell_of_urine'
    CONTINUOUS_FEEL_OF_URINE = 'continuous_feel_of_urine'
    PASSAGE_OF_GASES = 'passage_of_gases'
    INTERNAL_ITCHING = 'internal_itching'
    TOXIC_LOOK_TYPHOS = 'toxic_look_(typhos)'
    DEPRESSION = 'depression'
    IRRITABILITY = 'irritability'
    MUSCLE_PAIN = 'muscle_pain'
    ALTERED_SENSORIUM = 'altered_sensorium'
    RED_SPOTS_OVER_BODY = 'red_spots_over_body'
    BELLY_PAIN = 'belly_pain'
    ABNORMAL_MENSTRUATION = 'abnormal_menstruation'
    DISCHROMIC_PATCHES = 'dischromic_patches'
    WATERING_FROM_EYES = 'watering_from_eyes'
    INCREASED_APPETITE = 'increased_appetite'
    POLYURIA = 'polyuria'
    FAMILY_HISTORY = 'family_history'
    MUCOID_SPUTUM = 'mucoid_sputum'
    RUSTY_SPUTUM = 'rusty_sputum'
    LACK_OF_CONCENTRATION = 'lack_of_concentration'
    VISUAL_DISTURBANCES = 'visual_disturbances'
    RECEIVING_BLOOD_TRANSFUSION = 'receiving_blood_transfusion'
    RECEIVING_UNSTERILE_INJECTIONS = 'receiving_unsterile_injections'
    COMA = 'coma'
    STOMACH_BLEEDING = 'stomach_bleeding'
    DISTENTION_OF_ABDOMEN = 'distention_of_abdomen'
    HISTORY_OF_ALCOHOL_CONSUMPTION = 'history_of_alcohol_consumption'
    BLOOD_IN_SPUTUM = 'blood_in_sputum'
    PROMINENT_VEINS_ON_CALF = 'prominent_veins_on_calf'
    PALPITATIONS = 'palpitations'
    PAINFUL_WALKING = 'painful_walking'
    PUS_FILLED_PIMPLES = 'pus_filled_pimples'
    BLACKHEADS = 'blackheads'
    SCURRING = 'scurring'
    SKIN_PEELING = 'skin_peeling'
    SILVER_LIKE_DUSTING = 'silver_like_dusting'
    SMALL_DENTS_IN_NAILS = 'small_dents_in_nails'
    INFLAMMATORY_NAILS = 'inflammatory_nails'
    BLISTER = 'blister'
    RED_SORE_AROUND_NOSE = 'red_sore_around_nose'
    YELLOW_CRUST_OOZE = 'yellow_crust_ooze'

    SYMPTOM_CHOICES = (
        (BACK_PAIN, 'Back Pain'),
        (CONSTIPATION, 'Constipation'),
        (ABDOMINAL_PAIN, 'Abdominal Pain'),
        (DIARRHOEA, 'Diarrhoea'),
        (MILD_FEVER, 'Mild Fever'),
        (YELLOW_URINE, 'Yellow Urine'),
        (YELLOWING_OF_EYES, 'Yellowing of Eyes'),
        (ACUTE_LIVER_FAILURE, 'Acute Liver Failure'),
        (FLUID_OVERLOAD, 'Fluid Overload'),
        (SWELLING_OF_STOMACH, 'Swelling of Stomach'),
        (SWELLED_LYMPH_NODES, 'Swelled Lymph Nodes'),
        (MALAISE, 'Malaise'),
        (BLURRED_AND_DISTORTED_VISION, 'Blurred and Distorted Vision'),
        (PHLEGM, 'Phlegm'),
        (THROAT_IRRITATION, 'Throat Irritation'),
        (REDNESS_OF_EYES, 'Redness of Eyes'),
        (SINUS_PRESSURE, 'Sinus Pressure'),
        (RUNNY_NOSE, 'Runny Nose'),
        (CONGESTION, 'Congestion'),
        (CHEST_PAIN, 'Chest Pain'),
        (WEAKNESS_IN_LIMBS, 'Weakness in Limbs'),
        (FAST_HEART_RATE, 'Fast Heart Rate'),
        (PAIN_DURING_BOWEL_MOVEMENTS, 'Pain During Bowel Movements'),
        (PAIN_IN_ANAL_REGION, 'Pain in Anal Region'),
        (BLOODY_STOOL, 'Bloody Stool'),
        (IRRITATION_IN_ANUS, 'Irritation in Anus'),
        (NECK_PAIN, 'Neck Pain'),
        (DIZZINESS, 'Dizziness'),
        (CRAMPS, 'Cramps'),
        (BRUISING, 'Bruising'),
        (OBESITY, 'Obesity'),
        (SWOLLEN_LEGS, 'Swollen Legs'),
        (SWOLLEN_BLOOD_VESSELS, 'Swollen Blood Vessels'),
        (PUFFY_FACE_AND_EYES, 'Puffy Face and Eyes'),
        (ENLARGED_THYROID, 'Enlarged Thyroid'),
        (BRITTLE_NAILS, 'Brittle Nails'),
        (SWOLLEN_EXTREMETIES, 'Swollen Extremities'),
        (EXCESSIVE_HUNGER, 'Excessive Hunger'),
        (EXTRA_MARITAL_CONTACTS, 'Extra Marital Contacts'),
        (DRYING_AND_TINGLING_LIPS, 'Drying and Tingling Lips'),
        (SLURRED_SPEECH, 'Slurred Speech'),
        (KNEE_PAIN, 'Knee Pain'),
        (HIP_JOINT_PAIN, 'Hip Joint Pain'),
        (MUSCLE_WEAKNESS, 'Muscle Weakness'),
        (STIFF_NECK, 'Stiff Neck'),
        (SWELLING_JOINTS, 'Swelling Joints'),
        (MOVEMENT_STIFFNESS, 'Movement Stiffness'),
        (SPINNING_MOVEMENTS, 'Spinning Movements'),
        (LOSS_OF_BALANCE, 'Loss of Balance'),
        (UNSTEADINESS, 'Unsteadiness'),
        (WEAKNESS_OF_ONE_BODY_SIDE, 'Weakness of One Body Side'),
        (LOSS_OF_SMELL, 'Loss of Smell'),
        (BLADDER_DISCOMFORT, 'Bladder Discomfort'),
        (FOUL_SMELL_OF_URINE, 'Foul Smell of Urine'),
        (CONTINUOUS_FEEL_OF_URINE, 'Continuous Feel of Urine'),
        (PASSAGE_OF_GASES, 'Passage of Gases'),
        (INTERNAL_ITCHING, 'Internal Itching'),
        (TOXIC_LOOK_TYPHOS, 'Toxic Look (Typhos)'),
        (DEPRESSION, 'Depression'),
        (IRRITABILITY, 'Irritability'),
        (MUSCLE_PAIN, 'Muscle Pain'),
        (ALTERED_SENSORIUM, 'Altered Sensorium'),
        (RED_SPOTS_OVER_BODY, 'Red Spots Over Body'),
        (BELLY_PAIN, 'Belly Pain'),
        (ABNORMAL_MENSTRUATION, 'Abnormal Menstruation'),
        (DISCHROMIC_PATCHES, 'Dischromic Patches'),
        (WATERING_FROM_EYES, 'Watering from Eyes'),
        (INCREASED_APPETITE, 'Increased Appetite'),
        (POLYURIA, 'Polyuria'),
        (FAMILY_HISTORY, 'Family History'),
        (MUCOID_SPUTUM, 'Mucoid Sputum'),
        (RUSTY_SPUTUM, 'Rusty Sputum'),
        (LACK_OF_CONCENTRATION, 'Lack of Concentration'),
        (VISUAL_DISTURBANCES, 'Visual Disturbances'),
        (RECEIVING_BLOOD_TRANSFUSION, 'Receiving Blood Transfusion'),
        (RECEIVING_UNSTERILE_INJECTIONS, 'Receiving Unsterile Injections'),
        (COMA, 'Coma'),
        (STOMACH_BLEEDING, 'Stomach Bleeding'),
        (DISTENTION_OF_ABDOMEN, 'Distention of Abdomen'),
        (HISTORY_OF_ALCOHOL_CONSUMPTION, 'History of Alcohol Consumption'),
        (BLOOD_IN_SPUTUM, 'Blood in Sputum'),
        (PROMINENT_VEINS_ON_CALF, 'Prominent Veins on Calf'),
        (PALPITATIONS, 'Palpitations'),
        (PAINFUL_WALKING, 'Painful Walking'),
        (PUS_FILLED_PIMPLES, 'Pus Filled Pimples'),
        (BLACKHEADS, 'Blackheads'),
        (SCURRING, 'Scurring'),
        (SKIN_PEELING, 'Skin Peeling'),
        (SILVER_LIKE_DUSTING, 'Silver Like Dusting'),
        (SMALL_DENTS_IN_NAILS, 'Small Dents in Nails'),
        (INFLAMMATORY_NAILS, 'Inflammatory Nails'),
        (BLISTER, 'Blister'),
        (RED_SORE_AROUND_NOSE, 'Red Sore Around Nose'),
        (YELLOW_CRUST_OOZE, 'Yellow Crust Ooze'),
    )
    
    symptom1 = models.CharField(max_length=200, choices=SYMPTOM_CHOICES)
    symptom2 = models.CharField(max_length=200, choices=SYMPTOM_CHOICES)
    symptom3 = models.CharField(max_length=200, choices=SYMPTOM_CHOICES)
    symptom4 = models.CharField(max_length=200, choices=SYMPTOM_CHOICES)
    symptom5 = models.CharField(max_length=200, choices=SYMPTOM_CHOICES)
    
class Doctor(models.Model):
    General_Medicine='General Medicine'
    Pharmacology='Pharmacology'
    Dermatology='Dermatology'
    Vascular_Surgery='Vascular Surgery'
    Rheumatology='Rheumatology'
    Endocrinology='Endocrinology'
    Neurology='Neurology'
    Hepatology='Hepatology'
    Pulmonology='Pulmonology'
    Infectious_Disease='Infectious Disease'
    Immunology='Immunology'
    Orthopedics='Orthopedics'
    Cardiology='Cardiology'
    Gastroenterology='Gastroenterology'
    Urology='Urology'
    
    DEPARTMENT_CHOICES = (
        (General_Medicine, 'General Medicine'),
        (Pharmacology, 'Pharmacology'),
        (Dermatology, 'Dermatology'),
        (Vascular_Surgery, 'Vascular Surgery'),
        (Rheumatology, 'Rheumatology'),
        (Endocrinology, 'Endocrinology'),
        (Neurology, 'Neurology'),
        (Hepatology, 'Hepatology'),
        (Pulmonology, 'Pulmonology'),
        (Infectious_Disease, 'Infectious Disease'),
        (Immunology, 'Immunology'),
        (Orthopedics, 'Orthopedics'),
        (Cardiology, 'Cardiology'),
        (Gastroenterology, 'Gastroenterology'),
        (Urology, 'Urology'),
    )
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    
class History(models.Model):
    email=models.EmailField(verbose_name='email', max_length=255)
    symptom1 = models.CharField(max_length=200)
    symptom2 = models.CharField(max_length=200)
    symptom3 = models.CharField(max_length=200)
    symptom4 = models.CharField(max_length=200)
    symptom5 = models.CharField(max_length=200)
    diseases = models.CharField(max_length=1000, default='')
    departments = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=200)
    
    