
# both of these are the same, the main difference is that with the top one, you will know which index your currently on. this is because len(text) counts the number of characters while range() creates an iterable


# for i in range(len(string)):
    # print(text[i])

# for item in string:
    # print(item)



# index slicing:

# you can access a subset of your iterable by typing myiter[0:2:2], the first number is the index it starts on, the middle number is the index it ends and skips over and the last number is how it counts the index

# text = "Hello!"

# text[0:3] # -> "Hel"










com = input()

def reverse(com:str):
    # string "hello!"
    rev = ""
    for item in com:
        rev = item + rev
    return (rev)
  
        
    
    

def ispalindrome(com:str)-> bool:
        return reverse(com) == com
        


# print(reverse(com))

# print(ispalindrome(com))


# print("h" + "")


# com = "hello"

# print(com[4] + com[3] + com[2] + com[1] + com[0])

# if reverse(com) == "kayak":
    # print("maybe")
# else:
    # print("no")


# example string: "amogus! sussy balls"

#challenge 4


def reversemeta(com:str) -> str:
    final = ""
    start = 0
    for i in range(len(com)):
        if not com[i].isalnum():
            end = i
            final += reverse(com[start:end])
            final += com[i]
            start = i + 1
    return(final)

print(reversemeta(com))


# for i in range(len(com)):
    # print(com[i])





