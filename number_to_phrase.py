def unit_to_phrase(unit:int):
    ones = {

        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
    }
    tens = {

        2 : 'twenty',
        3 : 'thirty',
        4 : 'fourty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninty',
    }
    
    if unit < 20:
    
        return ones[unit]
    
    elif unit > 20 and unit < 100:
        
        tens_digit = unit//10
        ones_digit = unit%10
        
        if ones_digit == 0:
            return tens[tens_digit]
        
        else:
            return tens[tens_digit] + ones[ones_digit]
    
    elif unit >= 100:
    
        hundreds_digit = unit //100
        tens_digit = (unit//10) - (hundreds_digit * 10)
        ones_digit = unit%10

        if tens_digit == 1:
            ones_digit = ones_digit + 10
            return ones[hundreds_digit] + 'hundred' + ones[ones_digit]

        elif ones_digit == 0 and tens_digit == 0:
            return ones[hundreds_digit] + 'hundred'

        elif tens_digit == 0:
            return ones[hundreds_digit] + 'hundred' + ones[ones_digit]
        
        elif ones_digit == 0: 
            return ones[hundreds_digit] + 'hundred' + tens[tens_digit]
        
        return ones[hundreds_digit] + 'hundred' + tens[tens_digit] + ones[ones_digit]

    else: 
        return -1

print(unit_to_phrase(101))
