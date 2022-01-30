# f = open("Exercise.txt","w")
# f.write("Test file")
# f.close()

# f = open("Exercise.txt","a")
# f.write("\n Appending the test file")
# f.close()

f = open("Exercise.txt","r")
# print(f.read())
print(f.readlines())
f.close()