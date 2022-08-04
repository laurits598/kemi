import data as d
import dataSubstances as ds

mol = 6.022 * 10**23

def molarMasse(m, n):
	M = m/n
	return M

def massOfFormula(arr):
	mass = 0
	for elem in arr:
		print(elem[0])
		m = M.getMass(elem[0])
		n = elem[1]
		mass += m*n
	print(round(mass,2), "g/mol")
	return mass

def massPercentage(id, arr):
	for i in arr:
		if i[0] == id:
			p = d.getMass(id) * i[1]
	mass = 0
	for elem in arr:
		m = d.getMass(elem[0])
		n = elem[1]
		mass += m*n

	percentage = 100 * (p / mass)
	
	print(round(percentage, 1), "%")
	return percentage


def sort(s):
	arr = list(s)
	for x in range(0, len(arr)):
		if arr[x].islower():
			arr[x-1] = arr[x-1]+arr[x]
			arr[x] = ""
	res = [ele for ele in arr if ele != '']
	#print(res)
	# hvis tal er større end 9
	
	for i in range(2,len(res)):
		temp = ""
		if res[i].isdigit():
			temp = res[i]
			res[i] = res[i-1]
			res[i-1] = temp
	res2 = [ele for ele in res if ele != '']
	print(res2)
	return res

def helper(s):
	string = ""
	if s == 'O':
		string = "oxid"
		return string
	elif s == 'S':
		string = "sulfid"
		return string
	elif s == 'Cl':
		string = "klorid"
		return string
	else:
		string = str.lower(d.getName(s))
		string += "id"
		return string

def prefix(digit):
	string = ""
	arr = ["mono", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca"]
	string = arr[int(digit)-1]
	return string

def nameFormula(s):
	arr = sort(s)
	name = ""
	temp = ""
	for ele in arr:
		if ele == arr[0]:
			name = d.getName(ele)
		elif ele == arr[len(arr)-1]:
			temp = helper(ele)
			name += temp
		elif ele.isdigit():
			temp = prefix(ele)
			name += temp
		else:
			temp = str.lower(d.getName(ele))
			name += temp
	print(name)
	return name
			
#nameFormula("CHO")


print(ds.getStand("Ag+(aq)"))
print(ds.getStand("Ca(s)"))

