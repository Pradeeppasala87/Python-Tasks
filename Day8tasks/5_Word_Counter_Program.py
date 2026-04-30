file = open("article.txt", "r")
text = file.read()

print("Characters:", len(text))
print("Words:", len(text.split()))
print("Lines:", len(text.split("\n")))

file.close()
