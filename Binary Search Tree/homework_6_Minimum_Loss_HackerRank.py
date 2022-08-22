num_year = int(input())
price_list = list(map(int, input().split()))
year_index = {}
for i in range(len(price_list)):
    year_index[price_list[i]] = i

price_list = sorted(price_list)
min_ = -10e17
for i in range(len(price_list)-1):
    loss = price_list[i] - price_list[i+1]
    if year_index[price_list[i+1]] < year_index[price_list[i]]:
        min_ = max(min_, loss)
print(abs(min_))