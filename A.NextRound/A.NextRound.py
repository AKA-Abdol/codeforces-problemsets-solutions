n, k = map(int, input().split())
rank_list = [int(x) for x in input().split()]
advanced_participants_count = 0
reference_score = rank_list[k - 1]
for score in rank_list:
    if score > 0 and score >= reference_score:
        advanced_participants_count += 1

print(advanced_participants_count)
