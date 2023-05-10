import re

user_input = input("Geben Sie eine Rechnung ein: ")

def calculate(user_input):
    nums = re.findall(r'\d+\.\d+|\d+', user_input)
    calc = re.findall(r'[+\-*/]', user_input)
    nums = [float(num) for num in nums]

    if len(nums) < 2 or len(calc) < 1 or len(nums) != len(calc) + 1:
        print("Fehler: Ungültige Eingabe.")
    else:
        result = nums[0]
        for i in range(len(calc)):
            if calc[i] == "+":
                result += nums[i+1]
            elif calc[i] == "-":
                result -= nums[i+1]
            elif calc[i] == "*":
                result *= nums[i+1]
            elif calc[i] == "/":
                if nums[i+1] == 0:
                    print("Fehler: Division durch Null ist nicht erlaubt.")
                    break
                result /= nums[i+1]
    return result

while True:
    print("Das Ergebnis ist:", calculate(user_input))