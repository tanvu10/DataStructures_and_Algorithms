def Berland_Fashion(num_but, check_list_button):
    if num_but == 1:
        if sum(check_list_button) == 1:
            return 'YES'
        else:
            return 'NO'
    else:
        if sum(check_list_button) < num_but - 1:
            return 'NO'
        else:
            return 'YES'

# n = int(input())
# nb = list(map(int, input().split()))
# print(Berland_Fashion(n, nb))
