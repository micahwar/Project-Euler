with open("p022_names.txt", "r") as f:
    data = [x[1:][:-1] for x in f.read().split(",")]
data.sort()

def getScore(pos, nme):
    nscore = 0
    for char in nme:
        nscore += ord(char) - 64
    nscore = nscore * pos
    return nscore

score = []
for i, name in enumerate(data):
    score.append(getScore(i+1, name))
    
print(sum(score))
