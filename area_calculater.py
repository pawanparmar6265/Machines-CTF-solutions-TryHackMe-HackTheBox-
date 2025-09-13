print("\n \n \n ")

print("Welcome to the Area Calculator! \n \n \n \n \n ")



while True: 

    user_input= int(input("Which shape's area you want to calculate \n 1. Circle \n 2. Trinagle \n 3. Rectangle \n 4. Square \n 5. exit \n Enter the number of the shape below : "
  ))

    if user_input == 5:
            print("Goodbye! Thanks for using the Area Calculator.")
            break
    elif user_input == 1 : 
        radius= float(input("Enter the value of radius : "))
        print("area_of_circle :",(22/7) * (radius**2)  )
    elif user_input == 2 : 
        base=float(input("Enter value of Base : "))
        height=float(input("Enter value of Height : "))
        print("area of Triangle :", 1/2 * base * height)
    elif user_input == 3 : 
        length=float(input("Enter the value of length : "))
        breadth=float(input("Enter the value of breadth : "))
        print ("area of rectangle : " , length * breadth)
    elif user_input == 4 : 
        side=float(input("Enter the value of side : "))
        print("area of square : ", side ** 2 )
    else : 
        print(" oops ! you choose the wrong option  ")