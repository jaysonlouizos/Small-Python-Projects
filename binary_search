def sort_list(my_list,answer,search,high,low,guess):
    while True:
        guess = my_list[search]
        if guess == answer:
            return search
            break
            
        if guess < answer:
            low = search
            search = int((low + high)/2)

        elif guess > answer:
            high = search
            search = int((low + high)/2)

    return -1

def search_list(my_list,answer):
    my_list.sort()
    search = int(len(my_list) / 2)
    high = len(my_list)
    low = 0    
    guess = my_list[search]
    returnvalue = sort_list(my_list,answer,search,high,low,guess)
    return returnvalue

my_list = [1,2,3,4,5,6,7,8,9]
answer = 5
    
returnvalue = search_list(my_list,answer)
print(returnvalue)
