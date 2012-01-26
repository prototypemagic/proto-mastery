
half = int(raw_input()) / 2 #What is inputted is the amount of characters in the 'ticket'. 
t = map(int, raw_input())  #I am just popping it straight into what will be half of the ticket size
print "YES" if t.count(4) + t.count(7) == len(t) and sum(t[half:]) == sum(t[:half]) else print "NO"

