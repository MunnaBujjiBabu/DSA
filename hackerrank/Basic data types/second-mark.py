score = []

for i in range(int(input())):
    name = input()
    mark = float(input())
    score.append([name, mark])

# print(score)

sorted_score = []
#ordered score
for i in range(len(score)):
    if score[i][1] not in sorted_score:
        sorted_score.append(score[i][1])
sorted_score.sort()
# print(sorted_score)


low_score_name = []
second_low_score_name = sorted_score[1]
for i in range(len(score)):
    if score[i][1] == second_low_score_name:
        low_score_name.append(score[i][0])

low_score_name.sort()

print(low_score)
        

