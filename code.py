from experta import *
import random

priority=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
diseaseName=[]
symptom_map = {}
d_desc_map = {}
diseases_symptoms = []
diseases_list = []
d_treatment_map = {}



#global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map,priority_list

class generateFacts(KnowledgeEngine):
    """symptoms=""
    diseaseName=[]
    def __init__(self,symptoms,diseaseName):
        self.symptoms=symptoms
        self.diseaseName=diseaseName
        random.shuffle(priority_list)"""
    random.shuffle(priority)
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="unknown_disease")
        
    @Rule(Fact(action="unknown_disease"), NOT(Fact(sore_throat=W())), salience=priority[0])
    def funtion0(self):
        self.declare(Fact(sore_throat=input("Sore Throat ")));
        
    @Rule(Fact(action="unknown_disease"), NOT(Fact(sunken_eyes=W())), salience=priority[1])
    def funtion1(self):
        self.declare(Fact(sunken_eyes=input("Sunken Eyes ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(restlessness=W())), salience=priority[2])
    def funtion2(self):
        self.declare(Fact(restlessness=input("Restlessness ")));

    @Rule(Fact(action="unknown_disease"),NOT(Fact(headache=W())),salience=priority[3])
    def function3(self):
        # self.declare(Fact(headache=symptoms[diseaseName.index(strings)]))
        self.declare(Fact(headache=input("headache: ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(fatigue=W())), salience=priority[4])
    def funtion4(self):
        self.declare(Fact(fatigue=input("Fatigue ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(cough=W())), salience=priority[5])
    def funtion5(self):
        self.declare(Fact(cough=input("Cough ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(nausea=W())), salience=priority[6])
    def funtion6(self):
        self.declare(Fact(nausea=input("Nausea ")));
        
    @Rule(Fact(action="unknown_disease"), NOT(Fact(hallucination=W())), salience=priority[7])
    def funtion7(self):
        self.declare(Fact(hallucination=input("Hallucination ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(fainting=W())), salience=priority[8])
    def funtion8(self):
        self.declare(Fact(fainting=input("Fainting ")));

    @Rule(Fact(action="unknown_disease"), NOT(Fact(chest_pain=W())), salience=priority[9])
    def funtion9(self):
        self.declare(Fact(chest_pain=input("ChestPain ")));

    @Rule(Fact(action="unknown_disease"), NOT(Fact(blurred_vision=W())), salience=priority[10])
    def funtName10(self):
        self.declare(Fact(blurred_vision=input("Blurred vision ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(fever=W())), salience=priority[11])
    def funtName11(self):
        self.declare(Fact(fever=input("Fever ")));

    @Rule(Fact(action="unknown_disease"), NOT(Fact(back_pain=W())), salience=priority[12])
    def funtion12(self):
        self.declare(Fact(back_pain=input("BackPain ")));
    
    @Rule(Fact(action="unknown_disease"), NOT(Fact(low_body_temperature=W())), salience=priority[13])
    def funtName13(self):
        self.declare(Fact(low_body_temp=input("Low body temperature ")));

    

    

    

    @Rule(Fact(action='unknown_disease'), Fact(sore_throat="no"),  Fact(hallucination="no"), Fact(sunken_eyes="no"),
          Fact(back_pain="no"), Fact(chest_pain="no"), Fact(nausea="no"), Fact(restlessness="no") , Fact(cough="no"),
          Fact(fainting="yes"), Fact(fatigue="no"), Fact(headache="no"), Fact(low_body_temp="yes"),
          Fact(fever="no"),  Fact(blurred_vision="no"))
    def disease0(self):
        self.declare(Fact(disease="Hypothermia"))
        


    @Rule(Fact(action='unknown_disease'),Fact(low_body_temp="no"),Fact(blurred_vision="no"),Fact(sunken_eyes="no"),
           Fact(fainting="no"), Fact(sore_throat="yes"),  Fact(restlessness="no"),
          Fact(chest_pain="no"),  Fact(headache="yes"), Fact(cough="yes"), Fact(nausea="no"),
           Fact(hallucination="no"), Fact(back_pain="no"),Fact(fatigue="no"), Fact(fever="yes"))
    def disease1(self):
        self.declare(Fact(disease="Sinusitus"))
        
        
    @Rule(Fact(action='unknown_disease'),Fact(restlessness="no"), Fact(sunken_eyes="no"),Fact(back_pain="no"), 
          Fact(cough="no"),Fact(chest_pain="yes"), Fact(fainting="no"), Fact(sore_throat="no"), 
            Fact(headache="yes"),Fact(low_body_temp="no"), Fact(nausea="no"),Fact(fever="no"), 
          Fact(blurred_vision="yes"), Fact(hallucination="no"), Fact(fatigue="yes"))
    def disease2(self):
        self.declare(Fact(disease="Hypertension"))
    
    
    @Rule(Fact(action='unknown_disease'), Fact(back_pain="no"), Fact(hallucination="no"), Fact(headache="no"),
           Fact(sore_throat="no"), Fact(fatigue="no"), Fact(nausea="no"),
           Fact(fever="yes"), Fact(restlessness="no"), Fact(sunken_eyes="no"),Fact(low_body_temp="no"),
          Fact(blurred_vision="no"),Fact(cough="yes"), Fact(chest_pain="yes"),Fact(fainting="no"))
    def disease3(self):
        self.declare(Fact(disease="Arthritis"))
    
    
    @Rule(Fact(action='unknown_disease'),  Fact(fainting="no"), Fact(nausea="yes"),Fact(hallucination="no"),
          Fact(cough="no"),  Fact(headache="no"),Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(fever="no"), Fact(sunken_eyes="no"),  Fact(low_body_temp="no"),Fact(back_pain="no"),
          Fact(chest_pain="no"), Fact(low_body_temp="no"),Fact(blurred_vision="yes"))
    def disease4(self):
        self.declare(Fact(disease="Diabetes"))
      
        
    @Rule(Fact(action='unknown_disease'), Fact(fever="no"),Fact(blurred_vision="no"),Fact(fainting="no"),
          Fact(cough="yes"), Fact(sore_throat="no"), Fact(hallucination="no"),  Fact(chest_pain="yes"), 
          Fact(low_body_temp="no"),  Fact(sunken_eyes="no"), Fact(nausea="no"),Fact(headache="no"),
            Fact(back_pain="no"),Fact(restlessness="yes"),Fact(fatigue="no"),)
    def disease5(self):
        self.declare(Fact(disease="Asthma"))
    
    
    @Rule(Fact(action='unknown_disease'),Fact(nausea="yes"),Fact(back_pain="no"), Fact(sore_throat="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(blurred_vision="no"), Fact(headache="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"),  Fact(fatigue="yes"),  Fact(fever="yes"), Fact(sunken_eyes="no"), 
          Fact(chest_pain="no"),Fact(hallucination="no"))
    def disease6(self):
        self.declare(Fact(disease="Heat Stroke"))
        
        
    @Rule(Fact(action='unknown_disease'),  Fact(restlessness="no"), Fact(back_pain="yes"), Fact(fatigue="yes"),
          Fact(cough="no"),Fact(blurred_vision="no"), Fact(fainting="no"),Fact(chest_pain="no"), Fact(sore_throat="no"), Fact(hallucination="no"), 
          Fact(low_body_temp="no"), Fact(fever="no"),  Fact(nausea="no"),
          Fact(sunken_eyes="no"),Fact(headache="no"))
    def disease7(self):
        self.declare(Fact(disease="Alzheimers"))


    @Rule(Fact(action='unknown_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease8(self):
        self.declare(Fact(disease="Hyperthyroidism"))
    
    

    @Rule(Fact(action='unknown_disease'),Fact(sore_throat="no"), Fact(headache="no"),  Fact(chest_pain="no"),
          Fact(cough="no"),Fact(back_pain="no"), Fact(fever="yes"),Fact(fainting="no"), Fact(hallucination="yes"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"),  Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(fatigue="no"))
    def disease9(self):
        self.declare(Fact(disease="Tuberculosis"))

    
    @Rule(Fact(action='unknown_disease'), Fact(hallucination="no"), Fact(back_pain="no"), Fact(nausea="yes"), 
          Fact(cough="no"), Fact(fainting="no"),  Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(chest_pain="yes"),Fact(fever="no"), Fact(sunken_eyes="no"),
          Fact(blurred_vision="no"), Fact(sore_throat="no"),Fact(headache="no"),)
    def disease10(self):
        self.declare(Fact(disease="Heart Disease"))
        
    
    @Rule(Fact(action='unknown_disease'),  Fact(back_pain="no"), Fact(fatigue="yes"), 
          Fact(cough="no"),  Fact(nausea="yes"),Fact(fainting="no"), Fact(sore_throat="no"), Fact(chest_pain="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"),Fact(restlessness="no"),Fact(headache="no"), Fact(sunken_eyes="no"),
          Fact(blurred_vision="no"),Fact(hallucination="no"))
    def disease11(self):
        self.declare(Fact(disease="Jaundice"))

    

    

    

    

    

   


    #For_indirect _match
    @Rule(Fact(action='unknown_disease'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(hallucination=MATCH.hallucination),
          Fact(blurred_vision=MATCH.blurred_vision), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
                    low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
               fever, sunken_eyes, nausea, blurred_vision]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if (temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        print("Most probably it is: ",max_disease)
        print("Disease Description: ",d_desc_map[max_disease])
        print("Some Treatments: ",d_treatment_map[max_disease])


    #For_direct_match
    @Rule(Fact(action='unknown_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("You are most probably suffering with %s\n" % (id_disease))
        print("Disease description :\n")
        print(disease_details + "\n")
        print("Medications: \n")
        print(treatments + "\n")

def get_details(disease):
    return d_desc_map[disease]

def get_treatments(disease):
    return d_treatment_map[disease]

def openDiseaseList(diseaseName):
    for disease in diseaseName:
        disease_s_file = open("Symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        #print(disease_s_data)
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

if __name__=="__main__":
    print("Welcome to your medical diagnosis:")
    print("Please enter your details below: ")
    print("Name:")
    Name=input()
    print("Age:")
    Age=input()
    while(True):
        try:
            Age=int(Age)
            break
        except:
            print("Age not an integer, please reenter")
            Age=input()
    print("Gender: M/F/O ")
    Gender=input()
    print("Please answer the following questions: yes/no")
    diseaseName = ["Jaundice", "Alzheimers", "Arthritis", "Tuberculosis", "Asthma", "Sinusitis", "Heart Disease",
                   "Diabetes", "Hyperthyroidism", "Heat Stroke", "Hypothermia", "Hypertension"]

    openDiseaseList(diseaseName)

    engine=generateFacts()
    while(True):
        engine.reset()
        engine.run()
        continueAsk=input("Want to diagnose another disease?")
        if(continueAsk=="no"):
            exit()
