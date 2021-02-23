import os
import re
import unidecode
import nltk
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords, gutenberg
from nltk.util import ngrams
import pickle
from prettytable import PrettyTable

#Step 2: Vocabulary construction
vocabulary = set()
docname = []
file_text = []
file_name = []
table = PrettyTable()

fields = []
fields.append("Document Name")

for fileid in gutenberg.fileids():
    f1 = open(f'Corpus/{fileid}','r')
    file_name.append({fileid})
    docname.append(fileid)
    text = f1.read().split(' ')
    str_text = ''
    str_text = ' '.join(text)
    file_text.append(str_text)
    for token in text:
        vocabulary.add(token)

vocab = list(vocabulary)

for i in range(1,11):
    fields.append(vocab[i])

print(fields)

table.field_names = fields

print("Length of vocabulary: ",len(vocab))
print("Number of Documents: ",len(docname))

#Step 3: unigram 
# bow = [[0 for i in range(len(vocab))] for j in range(len(docname))]

# for i in range(len(vocab)):
#   # print(i," ",vocab[i])
#   for j in range(len(docname)):
#       f1 = open(f'Corpus/{docname[j]}','r')
#       text = f1.read().split(' ')
#       for k in range(len(text)):
#           if(text[k]==vocab[i]):
#               bow[j][i]+=1

# print(bow)

# with open("test.txt","wb") as fp:
#   pickle.dump(bow,fp)

with open("test.txt","rb") as fp:
  b = pickle.load(fp)

# print(b)

#Step 4: n-gram
def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

print("bigram: ", extract_ngrams(file_text[0], 2))
print()

#Printing Unigram matrix
print("Term Document Matrix for Unigram")

for i in range(len(file_name)):
    nrow = []
    nrow.append(file_name[i])
    for j in range(1,11):
        nrow.append(b[i][j])
    table.add_row(nrow)

print(table)