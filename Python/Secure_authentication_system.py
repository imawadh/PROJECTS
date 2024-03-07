def input_password():
    password = input("Enter Your Password : ")

    # Length of the Password 
    len_password = len(password)
    if(len_password<10):
        print("TOO SMALL PASSWORD")


    # Password Verification in term of length 
    while (len_password<10):
        password = input("Enter Your Password : ") 
        len_password = len(password)
        if(len_password<10):
            print("TOO SMALL PASSWORD")
    
    count(password)




def count(password):
    # Initialising the count as 0 for counting the presence of character
    count_upper_case = 0
    count_lower_case = 0
    count_digits = 0
    count_space = 0
    count_special_character = 0
    '''
    len password is here for the looping purpose which will help us to count the number of upper_case -- 65 to 90 , lower_case 97 to 122 , digits (48-57), special_charcter (32-47 / 58-64 / 91-96 / 123-126) i.e; the required criteria
    '''
    len_password = len(password)

    for j in range(len_password):
        if(ord(password[j])>=97 and ord(password[j])<=122):
            count_lower_case+=1  
        elif(ord(password[j])>=65 and ord(password[j])<=90):
            count_upper_case+=1      
        elif(ord(password[j])>=48 and ord(password[j])<=57):
            count_digits+=1
        elif(ord(password[j])==32):
            count_space+=1
        else:
            count_special_character+=1
    

    '''
    print(f"Upper Case : {count_upper_case}\nLower case : {count_lower_case}\nDigits : {count_digits}\nSpecial Charcter : {count_special_character}")

    # Printing the count of Each Charcter in the string password
    '''
    if(count_lower_case>=2 and count_upper_case>=2 and count_digits>=2 and count_special_character>=2 and count_space == 0):
        print()
        print("Congratulations ! Your Password has been Verified.... ")
        print("You can put this as your password")

    else:
        if(count_space != 0):
            print("Sorry! Space is not allowed in the Password")
            input_password()

        elif(count_lower_case<2):
            print("Sorry! Lower Case Count Criteria Falied.")
            input_password()

        elif(count_upper_case<2):
            print("Sorry! Upper Case Count Criteria Falied.")
            input_password()

        elif(count_digits<2):
            print("Sorry! Digit Count Criteria Falied.")
            input_password()
        
        else:
            print("Sorry! Special Character Count Criteria Falied.")
            input_password()


print("Criteria for the Password :\nLower Case character should be atleast 2\nUpper Case character should be atleast 2\nSpecial Case character should be atleast 2\nDigit character should be atleast 2\nNo space is allowed")

input_password()
