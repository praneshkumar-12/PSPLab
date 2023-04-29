def gethistogram(file="words.txt"):
    freq = {}
    with open(file, "r") as filehandle:
        lines = filehandle.readlines()
        for line in lines:
            if line in freq.keys():
                freq[line] += 1
            else:
                freq[line] = 1
    filehandle.close()

    return freq


def findprefix(pref):
    freq = gethistogram()
    res = {}
    for name, count in freq.items():
        if name.startswith(pref):
            res[name] = count
    result = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))

    for name in result.keys():
        print(name)


if __name__ == "__main__":
    while True:
        try:
            prefix = input("Enter prefix: ")
            findprefix(prefix)
        except EOFError:
            break
