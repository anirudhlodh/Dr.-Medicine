# test the trained model
import spacy
nlp = spacy.load('NER/NER_dr_medicine_new.spacy')
test_text = "paracetamol"
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)