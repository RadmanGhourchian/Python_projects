score_list = []
bigger_sum_scores = []

for i in range(1, 11):
    score = float(input("Enter your score : "))
    score_list.append(score)

avg = sum(score_list) / len(score_list)
for i in range(len(score_list)):
    if score_list[i] >= avg:
        bigger_sum_scores.append(score_list[i])

bigger_sum_scores.sort()
print("Your average score is : ", avg)
print("Scores bigger than average of the whole scores are : ", bigger_sum_scores)