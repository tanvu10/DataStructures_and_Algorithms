list_word = list(input())
count = 1
for i in list_word:
    if 65 <= ord(i) <= 90:
        count+=1
print(count)