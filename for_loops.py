# https://www.w3schools.com/python/python_for_loops.asp
# range starts at the first value & ends BEFORE the last value
for a in range(0, 10):  # for(i=0; i++; i<10)
    print("a = {0}".format(a))
print()

for b in range(0, 1):
    print("b = {0}".format(b))
print()

for c in range(1, 10):
    print("c = {0}".format(c))
print()

# Error: NO RANGE
for d in range(1, 1):
    print("d = {0}".format(d))
print()

for e in range(1, 2):
    print("e = {0}".format(e))
print()

for f in range(0, 10, 2):
    print("f = {0}".format(f))
print()

for g in [0, 4, 22, -5]:
    print("g = {0}".format(g))
print()
