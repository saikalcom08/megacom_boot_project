def get_payment_from_day(dateVal):
    if dateVal < 5: 
        return 10
    elif  5 <=  dateVal  < 10: 
        return 6
    elif 10 < dateVal  < 50: 
        return 4
    elif dateVal  >= 50: 
        return 3        

def get_total_symbols(text):
    textCount = len(text) - text.count(" ")
    return textCount

def check_for_aplha(text):
    text_without = text.replace(" ", "")
    return text_without.isalpha()

def check_for_capital(text):
    text_without = text.replace(" ", "")
    return text_without[0].isupper()

def main():
    text = input('Текст рекламы: ')
    days = int(input('Дни: '))
    
    payment = get_payment_from_day(days)
    total_amount_symbols = get_total_symbols(text)
    
    print("Count of symbols: ", total_amount_symbols)  
    
    if not (check_for_aplha(text) and check_for_capital(text)):
        print("validation not passed")
    else:
        print("Your payment:", payment *  total_amount_symbols * days , "soms")
    
     
   
#if __name__ == ''__main__':
main()

