num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if num_2 == 0:
    print("A number can never be divided by zero(0)")

#Addition
sum = num_1 + num_2
#print("Sum is: "+ str(sum))

#Subtraction
diff = num_1 - num_2
#print("Division is: "+ str(diff))

#Multiplication
prud = num_1 * num_2
#print("Product is: "+ str(prud))

#Rounding to 2 decimal places
rounded_sum = round(sum, 2)
#print("Rounded Sum is: " + str(rounded_sum))

rounded_diff = round(diff, 2)
#print("Rounded Difference is: " + str(rounded_diff))

rounded_prud = round(prud, 2)
#print("Rounded Product is: " + str(rounded_prud))




if num_2 ==0:
    print("A number can never be divided by zero(0)")
else:
    #Division
    div = num_1 / num_2
    #print("Division is: "+ str(div))

#floor Divison
    floor_div = num_1 // num_2
    #print("Floor Dicision is: " + str(floor_div))

#Modulus
    modulus = num_1 % num_2
    #print("Modulus is: " + str(modulus))

    rounded_div = round(div, 2)
    #print("Rounded Division is: " + str(rounded_div))

    rounded_floor_div = round(floor_div, 2)
    #print("Rounded Floor Division is: " + str(rounded_floor_div))

    rounded_modulus = round(modulus, 2)
    #print("Rounded Modulus is: " + str(rounded_modulus))   


#f-strings
print(f"Sum is: {sum}")
print(f"Difference is: {diff}")
print(f"Product is: {prud}")
print(f"Division is: {div}")
print(f"Floor Division is: {floor_div}")
print(f"Modulus is: {modulus}")
print(f"Rounded Sum is: {rounded_sum}")
print(f"Rounded Difference is: {rounded_diff}")
print(f"Rounded Product is: {rounded_prud}")
print(f"Rounded Division is: {rounded_div}")
print(f"Rounded Floor Division is: {rounded_floor_div}")
print(f"Rounded Modulus is: {rounded_modulus}")