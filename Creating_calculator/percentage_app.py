# Calculating percentage for students marks

m1 = float(input("Enter Marks in Maths: "))
m2 = float(input("Enter Marks in Networks: "))
m3 = float(input("Enter Marks in Programming: "))
m4 = float(input("Enter Marks in Project Management: "))
m5 = float(input("Enter Marks in Software Engineering: "))

# Add marks all together 
sum = m1 + m2 + m3 + m4 + m5
print(" The sum is:", sum)

percentage =(sum/500)*100
print("The Percentage Is:", percentage)

# Marks Allocation

if percentage>= 90:
    print("A+")
elif percentage>= 80:
    print("A")
elif percentage>= 70:
    print("B+")  
elif percentage>= 60:
    print("B")  
elif percentage>= 50:
    print("C+")  
elif percentage>= 40:
    print("C")
elif percentage>= 30:
    print("D+")
elif percentage>= 20:
    print("Failed")

               
               
               
               
                    
                 
