
def main():
    file = open("Passports.txt", "r")
    passports = file.readlines()
    file.close()

    line_number = 0
    line = ['']
    valid_passports = 0
    while(len(passports) > line_number):
        del(line)
        line = []

        while(len(passports) != line_number and passports[line_number] != "\n"):
            line.append(passports[line_number])
            line_number += 1

        
        line_number += 1
        passport = passport_conversion(line)
        complete_passport = validate_passport(passport)
            
        if(complete_passport):
            valid_passports += 1

    print(valid_passports)

def validate_passport(passport):
    valid = True
    for key, value in passport.items():
        if(key == "byr"):
            if(not(value.isnumeric())):
               return False
            value = int(value)
            if(not(value >= 1920 and value <= 2002)):
                return False
        elif(key == "iyr"):
            if(not(value.isnumeric())):
               return False
            value = int(value)
            if(not(value >= 2010 and value <= 2020)):
                return False
        elif(key == "eyr"):
            if(not(value.isnumeric())):
               return False
            value = int(value)
            if(not(value >= 2020 and value <= 2030)):
                return False
        elif(key == "hgt"):
            if(value[-2:] == "cm"):
               value = value.strip("cm")
               if(not(value.isnumeric())):
                  return False
               value = int(value)
               if(not(value >= 150 and value <= 193)):
                    return False
            else:
                value = value.strip("in")
                if(not(value.isnumeric())):
                   return False
                value = int(value)
                if(not(value >= 59 and value <= 76)):
                    return False
        elif(key == "hcl"):
            if(len(value) != 7):
                return False
            elif(not(value[0] == "#")):
                return False
            number_value = 0
            characters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
            for i in range(1, len(value), 1):
                for character in characters:
                    if(value[i] == character):
                        number_value += 1
                        break

            if(number_value != 6):
                return False
        elif(key == "ecl"):
            valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            valid = False
            for valids in valid_ecl:
                if(value == valids):
                    valid = True
                    break
            if(not(valid)):
                return False
        elif(key == "pid"):
            if(len(value) != 9):
                return False
            characters = ["0","1","2","3","4","5","6","7","8","9"]
            number_value = 0
            for i in range(len(value)):
                for character in characters:
                    if(value[i] == character):
                        number_value += 1
                        break
            if(number_value !=9):
                return False
        elif(key == "cid"):
            pass

    return valid
            
    
def passport_conversion(lines):
    passport = {"byr":"", "iyr":"", "eyr":"", "hgt":"", "hcl":"", "ecl":"", "pid":"", "cid":""}
    for line in lines:
        line = line.strip("\n")
        line = line.split(" ")
        for element in line:
            element = element.split(":")
            if(len(element) == 2):
                passport[element[0]] = element[1]

    return passport





if __name__ == "__main__":
    main()
