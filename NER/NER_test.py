# code by utkarsh saxena
# test the trained model
import spacy
nlp = spacy.load('NER/NER_dr_medicine_new.spacy')
<<<<<<< HEAD
test_text = "1015 Capsules R> Atorvastatin And Aspirin Capsules Ecosprin-AV 75 sqiR4T-3c9ox lorvastatinAnd Aspirin Capsules TJIN"
=======
test_text = "i bought Paracetamol"
>>>>>>> 08a1af87a8b0e82d491a6bd682cba53a546ba24d
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)