import hashlib
import pdb

def main(item):
    i = -1
    temp_item = item
    while(check_md5_5zeroes(temp_item)):
        i = i + 1
        temp_item = item + str(i)
        
    
    print(f"5 stars; {temp_item} : {i}")

    while(check_md5_6zeroes(temp_item)):
        i = i + 1
        temp_item = item + str(i)

    print(f"6 stars; {temp_item}: {i}")

def check_md5_5zeroes(item):
    hash = hashlib.md5(item.encode("utf-8")).hexdigest()
    if(hash[0:5] != "00000"):
          return True
    else:
          return False

def check_md5_6zeroes(item):
    hash = hashlib.md5(item.encode("utf-8")).hexdigest()
    if(hash[0:6] != "000000"):
          return True
    else:
          return False
          
if __name__ == "__main__":
    main("bgvyzdsv")
