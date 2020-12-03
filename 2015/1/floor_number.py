#Floor calculator for the advent of code 2015

def main():
    file = open("floor.txt", "r")
    floors = file.readline()
    file.close()
    floor = 0
    first_enter_basement = -1
    for i in range(len(floors)):
        if(floors[i] == '('):
            floor += 1
        elif(floors[i] == ')'):
            floor -= 1
            if(floor < 0 and first_enter_basement == -1):
                first_enter_basement = i + 1
            
    print(f"Santa Arrived at {floor}, and first entered the basement at {first_enter_basement}")


if __name__ == "__main__":
    main()
