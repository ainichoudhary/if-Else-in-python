

# if else

weight = int (input ('weight :'))
unit = input('(L)bs or (K)g : ')
if unit.upper() == "L":
    converted = weight * 0.45
    print (f"you are {converted} kilos")
else:
    converted = weight /0.45
    print(f"you are {converted} pounds")


name = "qu"
if len(name) < 3:
    print("name must be greater than 3")
elif len(name) > 50:
    print("name is to long")
else:
    print("name look good")



temp = 30
if temp > 20:
    print("its hot day")
else:
    print("its not hot day")



has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("eligible for loan")


price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : ${down_payment} ")




is_hot = False
is_cold = False

if is_hot:
    print("its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("its cold day")
    print(" wear warm cloth")
else:
    print("lovely day")

# basic

first = 'qurat'
last = 'ul ain'
message = first + ' [' + last + ' ] is a code'
# msg = f' {first} [{ last}] is a coder'
print(message)


birth_year = input('birth year')
age = 2023 - int(birth_year)
print(age)

weight_lbs = input('weight(lbs)')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)








