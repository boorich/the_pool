#strings
print "Provide a number x",
x = raw_input()
print "Provide a second number y",
y = raw_input()
z = x + y
print "%s + %s = %s, because raw_input() reads them in as strings" % (x, y, z)

#integers
print "Provide a number x",
x = int(raw_input())
print "Provide a second number y",
y = int(raw_input())
z = x + y
print "%s + %s = %s, because raw_input() reads tehm in as strings" % (x, y, z)