def My_functions(n):
    return lambda a: a* n

doubler = My_functions(2)
tripler = My_functions(3)

print(doubler(12))
print(tripler(12))



# x = lambda value_a, value_b : value_a + 10**value_b
#
# print(x(2, 2))