#Python implementation for the python checker in the Advent of code 2020

def main():
    file = open("passwords.txt", "r")
    number_of_valid_passwords = 0
    passwords = file.readlines()
    file.close()
    for password_line in passwords:
       password_line = password_line.strip()
       password_line = password_line.split(' ')
       numbers = password_line[0]
       numbers = numbers.split('-')
       lower = int(numbers[0])
       upper = int(numbers[1])
       elements = password_line[1]
       elements = elements.split(':')
       password = password_line[2]
       if(password_check(lower, upper, elements[0], password)):
           number_of_valid_passwords = number_of_valid_passwords + 1

    print(number_of_valid_passwords)
           
           
def password_check(lower, upper, element, password):
    value = (password[lower-1] == element) ^ (password[upper-1] == element)
    return value


if __name__ == "__main__":
    main()
