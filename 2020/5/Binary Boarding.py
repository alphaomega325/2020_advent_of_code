
import math

def main():
    file = open("Binary_Boarding_Examples.txt", "r")
    rows = 127
    columns = 7
    lines = file.readlines()
    file.close()

    highest_seat_id = 0
    
    for seat in lines:
        seat = seat.strip("\n")
        row = seat[0:7]
        column = seat[7:]
        upper = 127
        lower = 0
        for element in range(len(row)):
            if(element == len(row) - 1):
                if(row[element] == "B"):
                    rows = upper
                else:
                    rows = lower
            elif(row[element] == "F"):
                upper = math.ceil((lower + upper) / 2)
            elif(row[element] == "B"):
                lower = math.ceil((lower + upper) / 2)


        upper = 7
        lower = 0

        for element in range(len(column)):
            if(element == len(column) - 1):
                if(column[element] == "L"):
                    columns = lower
                else:
                    columns = upper
            elif(column[element] == "L"):
                upper = math.ceil((lower + upper) / 2)
            elif(column[element] == "R"):
                lower = math.ceil((lower + upper) / 2)
                
        

        seat_id = rows * 8 + columns

        if(seat_id > highest_seat_id):
            highest_seat_id = seat_id
        print(f"{seat}: row {rows}, column {columns}, seat ID {seat_id}")
        
            

    print(f"Highest Seat ID {highest_seat_id}")
    
    

    




if __name__ == "__main__":
    main()
