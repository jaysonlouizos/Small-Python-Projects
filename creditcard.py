def identify_card(card):
    card = list(card)
    temp = []

    for i in card:
        i = int(i)
        temp.append(i)
    
    card = temp
    check_digit = card.pop()
    reverse = card[::-1]
    temp = reverse[::2] * 2
    for i in range(len(reverse)):
        if i % 2 == 0:
            reverse[i] = reverse[i] * 2
            if reverse[i] > 9:
                reverse[i] = reverse[i] - 9
    
    card = sum(reverse)
    card = card % 10
    if card == check_digit:
        return True
    else:
        return False
    

