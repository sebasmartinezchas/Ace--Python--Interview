# write a program that finds the highest /greatest
# square lower that a certain other number

max_num = 500

# 2**2

# DRY -- don't repeat yourself!
for i in range(20):
    print(i**2)

max_num = 500
highest_square = 0

for i in range(max_num):
    square = i**2
    if square > max_num:
        break
    highest_square = square
print(highest_square)


def highest_square_under_a(max_num):

    highest_square = 0

    for i in range(max_num):
        square = i**2
        if square > max_num:
            break
        highest_square = square
    return highest_square


print(highest_square_under_a(500))
print(highest_square_under_a(5000))


def highest_square_under(max_num):

    if max_num <= 0:  # This is prevent the UnboundLocalError
        return 0

    highest_square = 0

    for i in range(max_num):
        square = i**2
        if square > max_num:
            break
        highest_square = square
    return i,highest_square


print(highest_square_under(500))

print(highest_square_under(1))

print(highest_square_under(0))  # UnboundLocalError: cannot access local variable 'i' where it is not associated with a value
