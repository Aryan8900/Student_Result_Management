print(" ####### Student Result Management #######")

# Storing the details in Dictionary....
Student_Book={}

while True:
  
  print("1. Add Student")
  print("2. View Student")
  print("3. Update Marks")
  print("4. Delete Student")
  print("5. Calculate Marks")
  print("6. Access Student Details")
  print("7. Exit")
  
# ------------ USER CHOICE --------
  choice=input("Enter your work to do: ")

# ------------- ADD NEW STUDENT -----------
  if choice == "1":
    # Entering Student Details to store....
    Student_Id=input("Enter Student ID: ")
    if Student_Id in Student_Book:
      print("Student Details already exist:")
    else:
      Student_Name=input("Enter Name of student: ")
      Python_Marks=int(input("Enter marks of python: "))
      Java_Marks=int(input("Enter marks of java: "))
      DSA_Marks=int(input("Enter marks of DSA: "))
      Student_Book[Student_Id]={
        "Name":Student_Name,
        "Marks":
        {
          "Python":Python_Marks,
          "Java":Java_Marks,
          "DSA":DSA_Marks
        }
      }
      print("Student Added Successfully!!")

# -------------- VIEW STUDENT DETAILS -------
  elif choice =="2":
     # Viewing Students details....
    Id=input('Enter Student ID to view details: ')
    if Id in Student_Book:
      View_Student=Student_Book.get(Id,'No details found!! Please enter correct ID')
      print(View_Student)
    else:
      print("Id not Found!!")

# ------------- UPDATE MARKS ------------
  elif choice == "3":
     # Update Marks ....
    Student_Id=input("Enter student ID to update marks: ")
    Subject=input("Enter Subject Name to Update: ")
    if Student_Id in Student_Book:
      if Subject in Student_Book[Student_Id]["Marks"]:
        New_Marks=int(input("Enter values to update: "))
        Student_Book[Student_Id]["Marks"][Subject]=New_Marks
        print("Marks Added Successfully!!")
      else:
        print("Subject not Found!!")
    else:
      print("Enter correct student id..")
      
# ------------ DELETE STUDENT DETAILS -----
  elif choice == "4":
    # Delete Student Details...
    Student_Id_Delete=input("Enter student ID to delete: ")
    if Student_Id_Delete in Student_Book:
      del Student_Book[Student_Id_Delete]
    else:
      print("Student not found to delete!!")

# ------------ Calculate Result --------
  elif choice == "5":
    Student_Id=input("Enter Student Id to calculate marks:")
    Total_Marks=0
    if Student_Id in Student_Book:
      Marks=list(Student_Book[Student_Id]["Marks"].values())
      for i in Marks:
        Total_Marks+=i
      print("Total Marks of Student: ",Total_Marks)
      
    # ------- Percentage Calculation ------
      Percentage=(Total_Marks*100)/300
      print("Student's Percentage is",Percentage,"%")
      
    # ------- Average Calculation ------
      Average = Total_Marks/3
      print("The Average of Student's Marks is",Average)

    # -------- Grading Student's Result -----
      if Percentage >= 95:
        print("Grade: A+")
      elif Percentage >= 95:
        print("Grade: A")
      elif Percentage >= 90:
        print("Grade: B")
      elif Percentage >= 80:
        print("Grade: C")
      elif Percentage >= 70:
        print("Grade: D")
      else:
        print("Fail !!")
    else:
      print("Student Not Found!!")
      
# ------------- Accessing Student Book -----------
  elif choice == "6":
  # Accessing all student details:
    for Student_Id, Student_Details in Student_Book.items():
      print(Student_Id,Student_Details)

# ------------- Exit System -----------
  elif choice == "7":
    print("Program Ended!!")
    break
