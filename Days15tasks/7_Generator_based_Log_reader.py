def read_file():
    file = open("log.txt", "r")
    for line in file:
        yield line
    file.close()

count = {}

for line in read_file():
    if "error" in line:
        count["error"] = count.get("error", 0) + 1

print(count)
