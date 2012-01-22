
half = int(raw_input()) / 2 #What is inputted is the amount of characters in the 'ticket'. 
ticket = raw_input()        #I am just popping it straight into what will be half of the ticket size


t = [] ## List for the 'ticket' to be broken up into
for x in range(len(ticket)):
    t.append(int(ticket[x]))

if t.count(4) + t.count(7) == len(t) and sum(t[half:]) == sum(t[:half]):
    print "YES"
else:
    print "NO"

