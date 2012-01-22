half = int(raw_input()) / 2
t    = [int(x) for x in raw_input()]

if t.count(4) + t.count(7) == len(t) and sum(t[half:]) == sum(t[:half]):
    print "YES"
else:
    print "NO"

