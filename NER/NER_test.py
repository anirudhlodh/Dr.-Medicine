# code by utkarsh saxena
# test the trained model
import spacy
nlp = spacy.load('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/NER/NER_dr_medicine_new.spacy')
test_text = "abilify 10mg aripiprazol 28 tabletten"
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)

print(doc.ents[0])