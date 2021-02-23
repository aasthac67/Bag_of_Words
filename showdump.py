import pickle

with open("test.txt","rb") as fp:
	b = pickle.load(fp)

print(b)