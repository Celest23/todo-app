filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace(".", "-") + ".txt" for filemane in filenames]

print(filenames)