import nltk
from nltk.corpus import gutenberg
import unidecode
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from prettytable import PrettyTable

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# emma = nltk.corpus.gutenberg.words('austen-emma.txt')
# print(emma)

#print(gutenberg.fileids())

for fileid in gutenberg.fileids():
	print(fileid)
	tokens = gutenberg.words(fileid)

	#Step 1: Preprocessing 
	
	#-------- Normalization --------
	#remove periods
	newlist = []
	for i in tokens:
		newlist.append(i.replace('.',''))

	#take only alphanumeric tokens
	newlist = [i for i in newlist if i.isalpha()]

	#lowercase
	newlist = [i.lower() for i in newlist]

	#remove hyphens 
	newlist1 = []
	for i in newlist:
		newlist1.append(i.replace('-',''))

	#removing accents
	normalize = [unidecode.unidecode(i) for i in newlist1]

	# ----------- Lemmatization ---------
	lemmatizer = WordNetLemmatizer() 
	lemmatize = [lemmatizer.lemmatize(i) for i in normalize]

	# --------- Stopword Removal --------
	preprocessed = [i for i in lemmatize if i not in stopwords.words('english')]

	#---------- Storing the preprocessed data --------
	f1 = open(f'corpus/{fileid}','w')
	for word in preprocessed:
		f1.write(word)
		f1.write(" ")