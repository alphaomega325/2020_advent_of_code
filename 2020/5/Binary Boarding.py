
import math

def main():
    file = open("Binary_Boarding_Input.txt", "r")
    rows = 127
    columns = 7
    lines = file.readlines()
    file.close()

    seats = []
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
                    rows = math.ceil(upper)
                else:
                    rows = math.ceil(lower)
            elif(row[element] == "F"):
                upper = (lower - 1 + upper) // 2
            elif(row[element] == "B"):
                lower = (lower + upper + 1) // 2


        upper = 7
        lower = 0

        for element in range(len(column)):
            if(element == len(column) - 1):
                if(column[element] == "L"):
                    columns = math.ceil(lower)
                else:
                    columns = math.floor(upper)
            elif(column[element] == "L"):
                upper = (lower - 1 + upper) // 2
            elif(column[element] == "R"):
                lower = (lower + upper + 1) // 2
                
        

        seat_id = rows * 8 + columns

        if(seat_id > highest_seat_id):
            highest_seat_id = seat_id

        seats.append({"Seat":seat, "Row":rows, "Column":columns, "Seat ID":seat_id})
            

    print(f"Highest Seat ID {highest_seat_id}")
    print(f"Missing Seat ID without the front and back rows is {show_missing_seat_id(seats)}")
    
def show_missing_seat_id(seats):
    highest = lowest = seats[0]["Row"]
    for item in seats:
        if(lowest > item["Row"]):
            lowest = item["Row"]
        elif(highest < item["Row"]):
            highest = item["Row"]
            
    seats.sort(key=lambda item: item.get("Seat ID"))
    missing_seats = []
    
    for i in range(len(seats)):
        if(highest != seats[i]["Row"] and lowest != seats[i]["Row"]):
            if(seats[i]["Seat ID"] + 1 != seats[i+1]["Seat ID"]):
                 return seats[i]["Seat ID"]  + 1


if __name__ == "__main__":
    main()
