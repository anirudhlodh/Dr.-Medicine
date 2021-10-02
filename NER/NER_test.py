# test the trained model
import spacy
nlp = spacy.load('NER/NER_dr_medicine')
test_text = "James went to buy Aspirin last year 2020"
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)