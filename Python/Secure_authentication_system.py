def input_password():
    password = input("Enter Your Password : ")
    global my_password
    my_password = password
    # Length of the Password 
    len_password = len(password)
    if(len_password<10):
        print("TOO SMALL PASSWORD")

    # Password Verification in term of length 
    while (len_password<10):
        password = input("Enter Your Password : ") 
        my_password = password
        len_password = len(password)
        if(len_password<10):
            print("TOO SMALL PASSWORD")
    
    password_verification(password)


def password_verification(password):
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
        verification_user_id_and_password(my_user_id,my_password)
# Calling of function to verify the username verification w.r.t to password whether three conscutive chararcter are not present in the password
        
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

def user_id_verification(user_id):
    len_user_id = len(user_id)
    for i in range (len_user_id):
        character_verifier = ord(user_id[i])
        if ((character_verifier>=97 and character_verifier<=122) or (character_verifier>= 65 and character_verifier<=90) or (character_verifier==95)):
            flag = 1
        else:
            flag = 0
            break
    if(flag == 1):
        print("USER ID Verified SuccessFully !")
    else:
        print("PLEASE TRY AGAIN !")
        user_id_input()


def user_id_input():
    user_id = input("Enter Your User ID : ")
    global my_user_id 
    my_user_id = user_id
    len_user_id = len(user_id)
    if(len_user_id<6):
        print("TOO SMALL USER ID ")
    while(len_user_id<6):
        user_id = input("Enter Your User ID : ") 
        my_user_id = user_id
        len_user_id = len(user_id)
        if(len_user_id<6):
            print("TOO SMALL USER ID ")
    
    user_id_verification(user_id)


def verification_user_id_and_password(user_id,password):
    flag = 1
    for i in range(len(user_id)-2):
        verifier = user_id[i]+user_id[i+1]+user_id[i+2]
        for j in range(len(password)-2):
            if(password[j]==verifier[0] and password[j+1]==verifier[1] and password[j+2]==verifier[2]):
                flag = 0
                break
        if(flag==0):
            break

    if(flag==1):
        print("Congratulations! You can keep this id and password anywhere. ... ")
    else:
        print("Your 3 consecutive character in user_id is present in the password\nSo, Please change it.",verifier)
        input_password()
        



    

print("Criteria For User ID : \nIt must contain alphabets(UPPER or LOWER Case) or underscore only ")

#Calling of User id Input Fuction to take input and verication whether it is possible or not 
    
user_id_input()

print("Criteria for the Password :\nLower Case character should be atleast 2\nUpper Case character should be atleast 2\nSpecial Case character should be atleast 2\nDigit character should be atleast 2\nNo space is allowed")

# Calling of Function to take input of password and verification 
input_password()


