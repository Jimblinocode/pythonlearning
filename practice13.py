com = input()

def reverse(com:str):
    # string "hello!"
    rev = ""
    for item in com:
        rev = item + rev
    return (rev)
  
        
    
    

def ispalindrome(com:str):
        if reverse(com) == com:
            return bool (True)
        else:
            return bool (False)


# print(reverse(com))

print(ispalindrome(com))


# print("h" + "")


# com = "hello"

# print(com[4] + com[3] + com[2] + com[1] + com[0])

# if reverse(com) == "kayak":
    # print("maybe")
# else:
    # print("no")

