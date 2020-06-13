SUBS_FILE = "mortdecai.srt"
NEW_FILE = SUBS_FILE + ".fixed.srt"

def isPunctuation(char):
    return char == "." or char == "!" or char == "," or char == "?"

def moveFirstCharToEnd(line):
    return line[1:] + line[0]

def isAllLinePunctuations(line):
    for c in line:
        if not isPunctuation(c):
            return False
    return True

fIn = open(SUBS_FILE, "r")
fOut = open(NEW_FILE, "w")

for line in fIn:
    line = line.strip()
    if (line and not isAllLinePunctuations(line)):
        while (isPunctuation(line[0])):
            line = moveFirstCharToEnd(line)
    fOut.write(line + '\n')

fIn.close()
fOut.close()