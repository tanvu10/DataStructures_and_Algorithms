num_penguin = int(input())
name_list = []
name_dic = {
    'Emperor Penguin': 0,
    'Little Penguin': 0,
    'Macaroni Penguin': 0
}
for _ in range(num_penguin):
    name = input()
    name_dic[name] += 1
max_value = 0
for key, value in name_dic.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)