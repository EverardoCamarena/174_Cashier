#Everardo Camarena
#cecs174 

def main():
    go=input(ask_if_continue)
    while go=='y':
        cashire()
        go=input(ask_if_continue)
    print('Good-bye')
def calculation(start,disp,change,unit,unit_str):
    amount=change//unit
    change=float('{0:.2f}'.format(change%unit))
    if amount !=0:
        if start:
            disp+='; '
        start=True
        disp+=str(int(amount))+unit_str
    return start,disp,amount,change
def cashire():
    due=float(input('Enter amount due: '))
    pay=float(input('Enter amount pay: '))
    change=float(input('{0:.2f}'.format(pay-due))
    disp=change
    start=False
    (start,disp,amount,change=calculate(start,disp,change,20, 'Twenties')
    (start,disp,amount,change=calculate(start,disp,change,10, 'Tens')
    (start,disp,amount,change=calculate(start,disp,change,5, 'Fives')
    (start,disp,amount,change=calculate(start,disp,change,1.00, 'Ones')
    (start,disp,amount,change=calculate(start,disp,change,.25, 'Quarters')
    (start,disp,amount,change=calculate(start,disp,change,.10, 'Dimes')
    (start,disp,amount,change=calculate(start,disp,change,.01, 'Pennies')
    (start,disp,amount,change=calculate(start,disp,change,.05, 'Nickels')
    return
main()
