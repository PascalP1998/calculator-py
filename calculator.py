nums = []

def calculate(nums):
    while True:
        try:
            num = input("Geben Sie eine Zahl ein (oder 'q', um die Eingabe zu beenden): ")
            if num == "q":
                break
            num = float(num)
            nums.append(num)
        except:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
    if len(nums) < 2:
        print("Fehler: Bitte geben Sie mindestens zwei Zahlen ein.")
    else:
        operation = input("Geben Sie die gewünschte Operation ein (+, -, *, /): ")

        if operation == "+":
            result = sum(nums)
        elif operation == "-":
            result = nums[0] - sum(nums[1:])
        elif operation == "*":
            result = 1
            for num in nums:
                result *= num
        elif operation == "/":
            if 0 in nums[1:]:
                print("Fehler: Division durch Null ist nicht erlaubt.")
            else:
                result = nums[0]
                for num in nums[1:]:
                    result /= num
        else:
            print("Fehler: Ungültige Operation.")
        return result

print("Das Ergebnis ist:", calculate(nums))