import pandas as pd
path = "C:/Users/Laurits/Desktop/Kemi/Grundstoffer.csv"

df = pd.read_csv(path, delimiter=';')

def getInfo(char):
	for i in range(0, len(df)):
		if df.iloc[i][0] == char:
			print("Name:   ", df.iloc[i][1])
			print("Number: ", df.iloc[i][2])
			print("Mass:   ", df.iloc[i][3], "g/mol")
			return df.iloc[i][1:3]
	print("not valid")

def getMass(char):
	for i in range(0, len(df)):
		if df.iloc[i][0] == char:
			print(df.iloc[i][3])
			return df.iloc[i][3]
	print("not valid")

def getName(char):
	for i in range(0, len(df)):
		if df.iloc[i][0] == char:
			print(df.iloc[i][1])
			return df.iloc[i][1]
	print("not valid")

def getNumber(char):
	for i in range(0, len(df)):
		if df.iloc[i][0] == char:
			print(df.iloc[i][2])
			return df.iloc[i][2]
	print("not valid")




