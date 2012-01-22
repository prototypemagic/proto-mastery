

pages = int(raw_input())
days = [int(x) for x in raw_input().split()]

amount_read = 0
amount_days = 0
zero_days = 0

for x in range(len(days)):
    amount_read += days[x]
    amount_days += 1
    if amount_days >= 8:
        amount_days = 0
    if days[x] == 0:
        zero_days += 1
    if amount_read >= pages:
        if zero_days >= 1:
            amount_days -= zero_days
        break


print amount_days
