import os
from PIL import Image
import PySimpleGUI as sg
from os.path import exists
import periodictable as pt
import numpy as np

directory = "C:/Users/Laurits/Desktop/Kemi/elementsImages/"

df = pd.read_csv(path, delimiter=';')

Gs = [[]]
for x in range(1,119):
	Gs.append([[x], pt.elements[x].name, pt.elements[x], pt.elements[x].mass])
	#print(x)

def getMass(num):
	return pt.elements[num].mass

def getName(num):
	name = pt.elements[num].name
	name = name.capitalize()
	return name

def getNumber(char):
	for i in range(1, 119):
		if char == str(Gs[i][2]):
			print(i)
			return i
	

def getImage(num):
	print("inputtet num: ", num)
	num = int(num)
	name = getName(num)
	print("name: ", name)
	file = directory + name + ".png"
	print("file: ",file)
	#img  = Image.open(file) 
	#img.show()
	return file

