

nameone = raw_input()
nametwo = raw_input()

mixed = raw_input()

combined_names = list(nameone) + list(nametwo)
mixed = list(mixed)

combined_names.sort()
mixed.sort()


if combined_names == mixed:
    print "YES"
else:
    print "NO"
