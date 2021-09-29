# { name : debt }
# добавить нового должника
# просмотреть долг должника
# погасить долг
# просмотреть список должников и сумму


debt_payers = {"user1" : 456, "user2" : 457, "user3" : 879, "user4" : 45454}

def add_debt_payer():
    payer = input("Add debt payer:")
    if payer in debt_payers:
        print("Already exists!")
        answer = input("Do you want to update the debt amount?")
        answer.lower()
        if answer == 'yes' :
            amount = input("Enter amount: ")
            debt_payers[payer] = amount
            print_dict()
        else:
            print_dict()
    else:
        amount = input("Enter amount: ")
        debt_payers[payer] = amount
        print_dict()

def get_debt_payer():
    payer = input("Which debt payer you want to get? :")
    if payer in debt_payers:
        print(debt_payers.get(payer))
    else:
        print("There is no user with such name.")
    
def zero_debt_payer():
    payer = input("Which user payed the debt :")
    if payer in debt_payers:
        debt_payers[payer] = 0
    else:
        print("Error! There is no user with such name.")
    
    
def print_dict():
    print(debt_payers)

add_debt_payer() 
get_debt_payer()
zero_debt_payer()
print_dict()

