from openpyxl import Workbook, load_workbook
import random

workbook = load_workbook("User_information.xlsx")

worksheet = workbook["Sheet1"]

nameColumn = "A"
number = 1

while worksheet[f"{nameColumn}{number}"].value is not None :
    
    if worksheet[f"C{number}"].value is None:
        
        fullname = worksheet[f"{nameColumn}{number}"].value.split(" ")
        
        firstname = fullname[0]
        lastname = fullname[2]
        
        email = firstname + "." + lastname + "@gmail.com"
        password = "pass" + firstname[0] + lastname[0] + f"{random.randint(10, 99)}"
        
        worksheet[f"C{number}"].value = email
        worksheet[f"D{number}"].value = password
        
    
    number = number + 1
    


    
workbook.save("User_information.xlsx")


