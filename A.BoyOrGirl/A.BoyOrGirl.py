username = input()
alphabet_flag = [0] * 26
for char in username:
    alphabet_flag[ord(char) - ord('a')] = 1

print(sum(alphabet_flag))