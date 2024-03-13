#Write a program to copy data from one file to another
file = open("Input.txt","r")
contain = file.read()
file.close

file = open("output.txt","w")
file.write(contain)
file.close
