def open_csv(csvfile:str) -> list:
    # return csv_content, keys run this command to pull the csvfile you would like to work on

    with open(csvfile, 'r') as file:
        
        lines = file.read().split('\n')
        keys = lines.pop(0)
        keys = keys.split(',')
        
        csv_content = []
        
        for char in lines:
            newdict = {}
            newlist = char.split(',')
            counter = 0
        
            for char in newlist:
                newdict.update({keys[counter]:newlist[counter]})
                counter = counter + 1
        
            csv_content.append(newdict) 

    return csv_content, keys


def update_file(csvfile:str,keys:list,csv_content:list):
    # run this function when all updates are made to contact list to save it to a CSV file
    
    with open(csvfile, 'w') as file:

        csv = ''

        for char in keys:

            if char == keys[len(keys) - 1]:
                csv = csv + f'{char}\n'

            else:
                csv = csv + char + ','

        
        for char in csv_content:
            lines = ''

            for x in char:

                if x == (list(char)[len(char) - 1]):
                    csv = csv + lines + f'{char[x]}\n'
    
                else:
                    lines = lines + char[x] + ','
        
        csv = list(csv)
        csv.pop()
        csv = ''.join(csv)
        
    
        file.write(csv)
    

def add_user(keys:list,csv_content:list,attributes:tuple):
    # takes in a tuple and converts it to a dictionary values in csv_content using keys list as keys 
        
    first_key = keys[0]
    tempdict = {}
    
    for char in csv_content:
        if char[first_key] == attributes[0]:
            return print('That user already exists.') 
               
    for i in range(len(attributes)):
        tempdict.update({keys[i]:attributes[i]})

    
    return csv_content.append(tempdict)


def find_user(keys:list,csv_content:list,name:str) -> dict:
    # returns the entry of a user by the first key

    first_key = keys[0]
    
    for char in csv_content:
        if name in char[first_key]:
            return char  


def update_attribute(keys:list,csv_content:list,name:str,attribute:str,value:str):
    # updates an attribute of a user in current csv_content
    
    first_key = keys[0]
    
    update_dict = {attribute:value}
    
    for i in range(len(csv_content)):
        if name in csv_content[i][first_key]:
            return csv_content[i].update(update_dict)


def delete_record(keys:list,csv_content:list,delete_user:'str'):
    # deletes current csv_content entry by using 'name' key
    
    first_key = keys[0]
    
    for i in range(len(csv_content)):
        if delete_user in csv_content[i][first_key]:
            return csv_content.pop(i)
