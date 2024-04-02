# Establishing the connection to database using sql
import mysql.connector as  conn
# Entering the hsot , user and passwd to connect
my_data_base = conn.connect(host="localhost",user='root',passwd='root')

my_data_base # name of the variable of connector of data base 
'''
when ever we need the data base we need to connect to call it
'''
print("Data Base Connection is SuccessFull")
my_cursor = my_data_base.cursor() # establishing cursor as my_cursor

my_cursor.execute("show databases")
print("Now it is showing my all Data-Bases present on my local Host")
print(my_cursor.fetchall())
my_cursor.execute("Create database if not exists student_db")
my_cursor.execute("Show databases")
print("Again")
print(my_cursor.fetchall())

# the above is commented beacuse the database has been created

my_cursor.execute('use student_db')


my_cursor.execute("CREATE TABLE IF NOT EXISTS student_data (id INT AUTO_INCREMENT PRIMARY KEY, student_name VARCHAR(255), father_name VARCHAR(255), mothers_name VARCHAR(255), mobile_number VARCHAR(255), email_id VARCHAR(255), blood_group CHAR(2))")


print("We are using the databse : student_db and table student_data")

# Name , email and Age as input to 
student_name = input("Enter Your Name : ")
father_name = input("Enter your Father's Name : ")
mothers_name = input("Enter your Mother's Name : ")
mobile_number = input("Enter your Mobile Number : ")
email_id = input("Enter your Email id : ")
blood_group =  input("Enter Your Blood Group : ")

insert_data = 'INSERT INTO student_data (student_name, father_name, mothers_name, mobile_number, email_id, blood_group) VALUES (%s, %s, %s, %s, %s, %s)'
values = (student_name, father_name, mothers_name, mobile_number, email_id, blood_group)
my_cursor.execute(insert_data, values)
my_data_base.commit()

print("Congratulations Your data has been added to SQL Database !  ..... ")



