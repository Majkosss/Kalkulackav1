import math

def kalkulacka():
    print("Vítejte v kalkulačce!")
    
    while True:
        num1 = float(input("Vložte první číslo: "))
        result = num1
        while True:
            operator = input("Vložte operátora (+, -, *, /, mocnina, odmocnina) nebo 'konec' pro výpočet výsledku: ")
            
            if operator == "konec":
                break
            
            if operator == "odmocnina":
                result = math.sqrt(result)
            else:
                num2 = float(input("Vložte další číslo: "))
                
                if operator == "+":
                    result += num2
                elif operator == "-":
                    result -= num2
                elif operator == "*":
                    result *= num2
                elif operator == "/":
                    result /= num2
                elif operator == "mocnina":
                    result **= num2
                else:
                    print("Tenhle operátor není podporován.")
                    continue
        
        print("Výsledek:", result)
        
        choice = input("Chcete pokračovat? (ano/ne): ")
        if choice.lower() != "ano":
            break
    
    print("Děkuji za používání kalkulačky. - Inspirováno Googlem.")

kalkulacka()
