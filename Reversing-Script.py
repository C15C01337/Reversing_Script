#Devloped By C15C01337 (Bishal Aryal)
#Follow me on Twitter username @C15C01337
data_input = input("Enter a value:")
while True:
    if data_input == 'DONE' or data_input == 'd' or data_input =='done':
        break
    reversed_string= data_input[::-1]
    print(reversed_string)

    data_input = input("Enter a value:")