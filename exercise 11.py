# make a def function
def reverse(number):
    # assign a variable that will make the number reverse with space
    reverse = ' '.join(str(number)[::-1])
    # print the reverse
    print(reverse)
    return True

# try the program
reverse(7536)