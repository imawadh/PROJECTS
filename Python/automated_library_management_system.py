    
print("For Manager of Library type --> Manager in any case : ")
print("As a user of Library Books Type your Name : ")

def add_books():
    global book_list
    book_list = [[101,"Think and Grow Rich", "Napolean Hill",5],[102,"Making India Awesome",'Chetan Bhagat',10],[103,'A bunch of old letters','Jawahar Lal Nehru',5],[104,'Ananadath','Bankim Chandra Chatterjee',7]]
    
    print(f"This is the list of {len(book_list)} books already present in the library")
    print()

    for i in book_list:
        print(i)
    print()
    book_id = int(input("Enter Book ID : "))
    book_name = input("Enter Book name : ")
    book_writer = input("Enter name of the book writer : ")
    book_quantity = int(input("Enter the qunatity of BOOKS : "))
    new_book = [book_id,book_name,book_writer,book_quantity]
    book_list = book_list.append(new_book)
    print("The set of books available in the library currently is : \n")
    print()
    print(book_list)
    for j in book_list:
        print(j)
    print()
    who_are_you()


def  who_are_you():
    who_are_you_input = input("Enter Who are You ? --- ")
    who_are_you_input = who_are_you_input.lower()
    if(who_are_you_input=='manager'):
        print("You are using the library as Manager.")
        print("You can add books to the library now for the user.")
        print("Type in Yes or No to add Books")
        input_by_manager = input("Do you want to add books to the library : ")
        input_by_manager = input_by_manager.lower()
        if(input_by_manager=='yes'):
            add_books()
        


    else:
        global user
        who_are_you_input = who_are_you_input.capitalize()
        user = who_are_you_input
        print("You are using the Library as Book reader.")

who_are_you()
# print(f"Your name is {user} and you are here to use Library Books")
# print("Basic Instructions Regarding Library Books :\n3Books are allowed per user.\nBook taken by the reader from the library need to be submitted within 14 days.")
