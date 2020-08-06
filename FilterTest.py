def is_even(x):
    if x % 2 == 0:
        return True


a = [1, 3, 10, 45, 6, 50]
print(a)

f1 = filter(is_even, a)  # is_even won't
print(list(f1))

f2 = [i for i in a if i % 2 == 0]
print(list(f2))
