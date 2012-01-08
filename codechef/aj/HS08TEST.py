withdraw, balance = [x for x in raw_input().split()]
withdraw = int(withdraw)
balance = float(balance)

if withdraw % 5 == 0 and withdraw + .5 <= balance: 
    balance -= .5 + withdraw

print "%.2f" % balance
