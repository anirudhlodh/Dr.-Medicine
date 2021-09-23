import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
text = input("Enter text: ")
# it will differentiat words and then give them tag
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent
sent = preprocess(text)
print(sent)
# allowing required tags only
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)
# making tree so that classification becomes easy
def ne_chunk(text):
    text = nltk.chunk.conlltags2tree(iob_tagged)
    return text
ne_tree = ne_chunk(pos_tag(word_tokenize(text)))
print(ne_tree)