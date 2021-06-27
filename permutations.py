import itertools
import random

conditions = None
participants = None

def calc_score(matrix, mylist):
    scores = [0] * len(matrix)

    for r in range(0, len(matrix)):
        for j in range(0, len(mylist)):
            for k in range(0, len(mylist[j])):
                scores[r] += abs(k - matrix[r].index(mylist[j][k]))
                if k < (len(mylist[j]) - 1):
                    if mylist[j].index(matrix[r][k]) + 1 == mylist[j].index(matrix[r][k + 1]):
                        scores[r] -= 5
    return scores

conditions = int(input("Number of conditions: "))
conds = list(range(1, conditions+1))
print("Your conditions are: " + str(conds))

participants = int(input("Number of participants: "))

matrix = list(itertools.permutations(conds))

length = len(matrix)
print("Total possible permutations: " + str(len(matrix)))

start = random.randrange(length)
print("Starting sequence at position " + str(start) + " which is " + str([matrix[start]]))

go_again = True
while go_again:

    matrix = list(itertools.permutations([n+1 for n in range(0,conditions)]))

    print(len(matrix))

    mylist = [matrix[start]]
    matrix.remove(matrix[start])

    print("Added "+str(mylist[0])+" to start the list")

    for a in range(0, participants):

        random.shuffle(matrix)

        scores = calc_score(matrix, mylist)
        if scores == 0:
            scores = 1

        m = max(scores)
        mi = scores.index(m)

    #    for b in range(0, len(scores)):
    #        if scores[b] == m:
    #            print("Max score("+str(m)+"): "+str(matrix[b]))

    #    z = matrix.index((6,5,4,3,2,1))
    #    print("BTW: matrix["+str(z)+"] has a score of "+str(scores[z]))

        found = matrix[mi]

        mylist.append(found)
        matrix.remove(found)

        print("Added "+str(found)+" as it has the highest score of: "+str(m))

    go_again = False
    for i in range(0, conditions):
        counts = [0] * conditions
        for j in range(0, participants):
            counts[mylist[j][i] - 1] += 1
        print(str(i+1)+": "+str(counts))
        if (max(counts) - min(counts)) > 1:
            print("Distribution of conditions is not correct, making more changes")
            go_again = True

print(" ")
print("======================")
print("Final list:")

for elem in mylist:
    print(elem)

print("Count of each condition per position:")
for i in range(0, conditions):
    counts = [0] * conditions
    for j in range(0, participants):
        counts[mylist[j][i] -1] += 1
    print(str(i+1)+": "+str(counts))