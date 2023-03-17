username = input()
alphabet_flag = [0] * 26
for char in username:
    alphabet_flag[ord(char) - ord('a')] = 1

is_male = sum(alphabet_flag) % 2
if is_male:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')