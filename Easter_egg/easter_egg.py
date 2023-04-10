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
    print("Invalid egg")
    invalid_egg = False
# Flag that captures if the amount of eggs ins valid or not
invalid_amount = False
if amount < 1:
    print("Invalid Amount")
    invalid_amount = True

# Check if the flags are not true
if invalid_amount == False and invalid_egg == False:
    due = 0
    if egg_type == "A":
        if amount > 50:
            print("The limit p/user of this egg is")

