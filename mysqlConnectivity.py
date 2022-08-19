from dbconfig import dbconfig
import mysql.connector as connector


class dbHelper:
    def __init__(self) :
        #creating the connection with mysql database
        self.con = connector.connect(host=dbconfig['host'], port=dbconfig['port'], user=dbconfig['username'], password=dbconfig['password'], database='pytest')
            #connector.connect() method returns a mysql connection object
            #its stored in the "con" variable

        #create table
        #query
        query = 'CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY, first_name VARCHAR(100) , last_name VARCHAR(100) ,gender VARCHAR(1), marks INT DEFAULT 0)'
        #table "student" with fields = id, name, surname, gender,marks

        #cursor is used to execute query
        cursor = self.con.cursor()
        #execute the query
        cursor.execute(query)
          #the table is actually created

        
    ###inserting record into table######
    def insert(self, id , name, surname, gender) :
        #query 
        query = "INSERT INTO student(id, first_name, last_name , gender) VALUES({}, '{}' , '{}', '{}')".format(id, name, surname, gender)

        cursor = self.con.cursor()
        cursor.execute(query)

        #save the changes made to the database
        self.con.commit()

        print("Student added to the database")

    
    ###display all records##########
    def display(self):
        query = "SELECT * FROM student"
        cursor = self.con.cursor()
        cursor.execute(query)

        #now cursor has all the data but
        #print(cursor) will display the query
        #so we need to traverse thru the data
        #and print one row at a time
        for row in cursor:
            print(row)
        #each row will be displayed as a tuple
        # row[0] = Id of that student

        #commit() not needed as we arent amking any changes to the database 


    ###display user info##########
    def display_student_details(self, id):
        #get student info
        query = "SELECT * FROM student WHERE id = {}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)

        #print info
        for row in cursor:
            print("Name : " + row[1] + " " + row[2])
            print("Gender : " + row[3])
            if row[4] != 0 :
                print("Marks : " + (str)(row[4]) )
            else:
                print("Marks not entered.")


    ##delete record#########
    def delete(self, id):
        query = "DELETE FROM student WHERE id = {}".format(id)

        cursor = self.con.cursor()
        cursor.execute(query)

        self.con.commit()

        print("Student record deleted.")

    
    ##update record####
    #add marks
    def enterMarks(self, id, marks) :
        query = "UPDATE student SET marks={} WHERE id={}".format(marks, id) 

        cursor = self.con.cursor()
        cursor.execute(query)

        self.con.commit()

        print("Marks added.")
    