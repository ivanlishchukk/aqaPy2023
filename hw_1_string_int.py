#HW_1_string_int

#Task1
firstName = 'Ivan'
lastName = 'Lishchuk'

print(firstName + ' ' + lastName)
print(firstName.lower() + ' ' + lastName.lower())
print(firstName.upper() + ' ' + lastName.upper())


firstName = '\tIvan'
lastName = '\nLishchuk\t'
print(firstName + ' ' + lastName)

firstName = firstName.strip()
lastName = lastName.strip()
print(f"{firstName + ' ' + lastName}")

#Task2
actualUsd = 36.65453345
exchangeUahToUsd = actualUsd*1000
exchangeUahToUsd = round(exchangeUahToUsd, 2)

print(f"Поточний курс складає: {exchangeUahToUsd}")
