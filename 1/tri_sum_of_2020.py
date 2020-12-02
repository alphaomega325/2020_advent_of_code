#This is a sum of 2020 using the python language

def main():
    answer = 2020
    file = open("input.txt", "r")
    numbers = file.readlines()
    for element in range(len(numbers)):
        numbers[element] = int(numbers[element])
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for l in range(j + 1, len(numbers)):
                if(equals_sum(numbers[i], numbers[j], numbers[l], answer)):
                    print(numbers[i] * numbers[j] * numbers[l])
    
        
def equals_sum(sum1, sum2, sum3, answer):
    if((sum1 + sum2 + sum3) == answer):
        print(sum1 + sum2 + sum3)
        return True
    else:
        return False


if __name__ == "__main__":
    main()
    
