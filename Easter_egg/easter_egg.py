"""
In this project my task is to do a program that helps a factory of chocolate 
eggs to sell eggs. This factory makes three types of easter eggs:
• Single (A): with a unit value of R$ 12.00, limit per order 50.
• Stuffed (B): with a unit value of R$ 15.50, limit per order 30.
• With a surprise (C): with a unit value of R$21.30, limit per order 20.
"""
# Inicializing important caracters
limit_A = 50
price_A = 12.00
limit_B = 30
price_B = 15.00
limit_C = 20
price_C = 21.30

# Print the menu tu the user
print("         MENU:\n"
      "==========================\n"
      "Types of eggs:     Value:\n"
      "Single(A)          $12.00\n"
      "Stuffed(B)         $15.50\n"
      "Surprise(C)        $21.30\n"
      "==========================\n")

# Ask the user for a Type and the quantity of eggs he/she wants
egg_type = input("Type of the egg: ").upper()
amount = int(input("Amount of effs wanted: "))

# Creating flags:
# Flag that captures if the type of the egg is valid or not
invalid_egg = False
if egg_type == "A" or egg_type == "B" or egg_type == "C":
    pass
else:
    print("\n***Invalid egg***")
    invalid_egg = True
# Flag that captures if the amount of eggs ins valid or not
invalid_amount = False
if amount < 1:
    print("\n***Invalid Amount***")
    invalid_amount = True


# Check if the flags are not true
if invalid_amount == False and invalid_egg == False:
    # Print a divider to divide the order from the result
    print()
    if egg_type == "A":
        if amount > limit_A:
            print("The limit p/user of this egg is", limit_A)
        else:
            print(f"order = {amount} egg(s) of type \n{egg_type} (simple)")
            print(f"total value = R${(amount * price_A):.2f}")
    if egg_type == "B":
        if amount > limit_B:
            print("The limit p/user of this egg is", limit_B)
        else:
            print(f"Order = {amount} egg(s) of type \n{egg_type} (stuffed)")
            print(f"total value = R${(amount * price_B):.2f}")
            
    if egg_type == "C":
        if amount > limit_C:
            print("The limit p/user of this egg is ", limit_C)
        else:
            print(f"Order = {amount} egg(s) of type \n{egg_type} (with surprise)")
            print(f"total value = R${(amount * price_C):.2f}")

