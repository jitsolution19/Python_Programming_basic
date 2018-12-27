#Write a program to use regular expression to count number in file
import re
file = open("Inputfile.txt","r")
contain = file.read()
print(contain)
print(re.findall(r'[A][A][A]',contain))
Counter = re.findall(r'[A][A][A]',contain)
print(len(Counter))
file.close

#print(re.split(r'(s*)','here are some words'))
#print(re.split(r'[A][A]','ADFFFAAASDEVFGGBCDCDDDDRFEDSAADFRVC'))
#print(re.split(r'A+','ADFFFAAASDEVFGGBCDCDDDDRFEDSAADFRVC'))
#print(re.findall(r'\d\w.*','Street 324 main flat 16 Aundh Pune 411007'))