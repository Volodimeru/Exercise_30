def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(l):
#all vanity plates must start with at least two letters.
        if l[0].isdigit() or l[1].isdigit() :
            return False
#may contain a maximum of 6 characters and a minimum of 2 characters.
        if not 2 <= len(l) <= 6:
            return False
#The first number used cannot be a 0
        i = 0
        while i < len(l):
            if l[i].isalpha() == False:
                if l[i] == "0":
                    return False
                else:
                     break
            i += 1
# Numbers cannot be used in the middle of a plate
        for i in range(len(l)):
            if l[i].isdigit():
                if not l[i:].isdigit():
                    return False
#No periods, spaces, or punctuation marks are allowed..
        if not l.isalnum():
            return False
        else:
            return True

            
if __name__=="__main__":
    main()