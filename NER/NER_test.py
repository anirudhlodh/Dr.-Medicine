# test the trained model
import spacy
nlp = spacy.load('NER/NER_dr_medicine')
test_text = "10010 TABLETS aspirin TABLETS BP 500 mg Dolo MICRO"
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)