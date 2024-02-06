contents = ["all of the "\
            "above.",
            "about what I said " \
            "earlier.",
            " I wish I could build " \
            "everything",
            "bye now"]

filenames = ["doc.txt", "report.txt", "love.txt" ]

for content, filename in zip(contents, filenames):
    file = open(f"Bonus 5/{filename}", "w")
    file.write(content)