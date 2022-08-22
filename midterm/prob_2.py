cost, dollar, need = map(int, input().split())
def main():
    if need == 0 or cost == 0:
        return print(0)
    else:
        total_money_need = cost*sum([i for i in range(need+1)])
        money_borrow = total_money_need - dollar
        if money_borrow > 0:
            print(abs(money_borrow))
        else:
            print(0)

main()