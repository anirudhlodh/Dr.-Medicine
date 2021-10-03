import random
import pandas as pd
import spacy
import re
from spacy.training import Example
spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")
df = pd.read_csv("NER/dataset/drug_review_dataset_with_sentiment.csv")
def process_review(review):
    processed_token = []
    for token in review.split():
        token = ''.join(e.lower() for e in token if e.isalnum())
        processed_token.append(token)
    return ' '.join(processed_token)
all_drugs = df['drugName'].unique().tolist()
all_drugs = [x.lower() for x in all_drugs]
all_drugs
df['review']
LABEL = 'DRUG'
count = 0
TRAIN_DATA = []
for _, item in df.iterrows():
    ent_dict = {}
    if count < 1000:
        review = process_review(item['review'])
        #Locate drugs and their positions once and add to the visited items.
        visited_items = []
        entities = []
        for token in review.split():
            if token in all_drugs:
                for i in re.finditer(token, review):
                    if token not in visited_items:
                        entity = (i.span()[0], i.span()[1], 'DRUG')
                        visited_items.append(token)
                        entities.append(entity)
        if len(entities) > 0:
            ent_dict['entities'] = entities
            train_item = (review, ent_dict)
            TRAIN_DATA.append(train_item)
            count+=1
nlp = spacy.load('en_core_web_sm')  # load existing spaCy model
ner = nlp.get_pipe('ner')
ner.add_label(LABEL)

optimizer = nlp.create_optimizer()

# get names of other pipes to disable them during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):  # only train NER
    for itn in range(20):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.35, sgd=optimizer, losses=losses)
        print(losses)
# nlp.tokenizer = None
nlp.to_disk('NER/NER_dr_medicine_new.spacy')
