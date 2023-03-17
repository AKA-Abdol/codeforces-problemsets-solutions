n = int(input())
solved_questions = 0
for i in range(n):
    votes = [int(x) for x in input().split()]
    if sum(votes) > 1:
        solved_questions += 1

print(solved_questions)
