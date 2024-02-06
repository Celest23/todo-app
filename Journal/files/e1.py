import glob
#tells you which files are in your folder
myfiles = glob.glob("*txt")
print(myfiles)
#reads you whats in those txt
for filepath in myfiles:
    with open(filepath,"r") as file:
        print(file.read())