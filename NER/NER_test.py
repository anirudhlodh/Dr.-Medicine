# code by Utkarsh Saxena
# test the trained model
import spacy
def listToString(s): 
    str1 = " " 
    return (str1.join(s))  
nlp = spacy.load('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/NER/NER_dr_medicine_new.spacy')
test_text = "ABILIFY10mg aripiprazol 28Tabletten A"
doc = nlp(test_text)
print("Entities in '%s'" % test_text)
for ent in doc.ents:
    print(ent.label_, " -- ", ent.text)


    
