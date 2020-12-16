import datetime

def form_list(filename:str):
    
    lines = []
    
    with open(filename, 'r') as file:
        templist = file.read().split('\n')
        lines = []

        for char in templist:
            lines.append(char.split())

        return lines
    
def get_date(date):                
    return datetime.datetime.strptime(date, '%d-%b-%Y')
        # print(date.year)   # 2016
        # print(date.month)  # 3
        # print(date.day)    # 25
        # print(date)  # 2016-03-25 00:00:00
        # print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

def only_daytotals(lines):
    
    daytotal = []
    
    for char in lines:
        char[1] = int(char[1])
        daytotal.append(char[1])
    
    return daytotal

def mean(lines):
    
    daytotal = only_daytotals(lines)
    total = 0
    
    for char in daytotal:
        total = total + char
    
    return total / len(lines)

def variance(lines):
    
    average = mean(lines)
    
    return sum([(x - average)**2 for x in only_daytotals(lines)]) / len(lines)

def rainy_day(lines):
    x = max(only_daytotals(lines))
    for char in lines:
        if x == char[1]:
            return f'{char[0]} {char[1]} inches of rain'


def rainy_year(lines):
    
    daytotals = only_daytotals(lines)
    yeartotals = []
    temptotal = daytotals[0]

    for i in range(1, len(lines)):

        date1 = get_date(lines[i][0])
        date2 = get_date(lines[i - 1][0])

        if date1.year == date2.year:
            temptotal = temptotal + daytotals[i]

        else:
            x = (date2.year, temptotal)
            yeartotals.append(x)

            temptotal = 0
    
    x = (date2.year, temptotal)
    yeartotals.append(x)
    maxvalue = 0

    
    for char in yeartotals:
        if char[1] > maxvalue:
            maxvalue = char[1]
            maxyear = char[0]

    return f'{maxyear} is the rainiest year at {maxvalue} inches.'
