#Python implementation for the python checker in the Advent of code 2020

def main():
    file = open("passwords.txt", "r")
    number_of_valid_passwords = 0
    number_of_valid_passwords_index = 0
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
        elements = elements[0]
        password = password_line[2]
        if(password_check(lower, upper, elements, password)):
            number_of_valid_passwords = number_of_valid_passwords + 1

        if(password_check_index(lower, upper, elements, password)):
            number_of_valid_passwords_index = number_of_valid_passwords_index + 1

    print(f"First Solution: {number_of_valid_passwords} \nSecond Solution: {number_of_valid_passwords_index}")
           
           
def password_check(lower, upper, element, password):
    number = password.count(element)
    if(lower <= number <= upper):
        return True
    else:
        return False

def password_check_index(lower, upper, element, password):
    value = (password[lower-1] == element) ^ (password[upper-1] == element)
    return value


if __name__ == "__main__":
    main()
