import pymysql

# User Defined Functions/Methods

def connectdatabase():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Prasan2004',
        database='Prasan' )

def fetch(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def execute(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def display(connection, subject):
    query = "SELECT * FROM " + subject
    rows = fetch(connection, query)
    print("Data in " + subject + " table:")
    for row in rows:
        print(row)

def add(connection, subject):
    SNO = int(input("Enter serial number (sno): "))
    Topic = input("Enter topic: ")
    date_last_revised = input("Enter date last revised (YYYY-MM-DD): ")
    confidence_level = int(input("Enter confidence level: "))
    importance_level = int(input("Enter importance level: "))
    time_spent = float(input("Enter time spent (in hours): "))
    next_revision_date = input("Enter next revision date (YYYY-MM-DD): ")

    insert= ("INSERT INTO " + subject + " (sno, topic, date_last_revised, confidence_level, ""importance_level, time_spent, next_revision_date) VALUES (" + str(SNO) + ", '" + Topic + "', '" + date_last_revised + "', " + str(confidence_level) +  ", " + str(importance_level) + ", " + str(time_spent) + ", '" + next_revision_date + "')")
    execute(connection, insert)
    print("Data added successfully!")

def update(connection, subject):
    display(connection, subject)
	
    SNO = int(input("Enter 'sno' of the row you want to update in " + subject + ": "))
    Topic = input("Enter new topic: ")
    date_last_revised = input("Enter new date last revised (YYYY-MM-DD): ")
    confidence_level = int(input("Enter new confidence level: "))
    importance_level = int(input("Enter new importance level: "))
    time_spent = float(input("Enter new time spent (in hours): "))
    next_revision_date = input("Enter new next revision date (YYYY-MM-DD): ")

    update = ( "UPDATE " + subject +  " SET topic = '" + Topic + "', date_last_revised = '" + date_last_revised +  "', confidence_level = " + str(confidence_level) + ", importance_level = " + str(importance_level) + ", time_spent = " + str(time_spent) +  ", next_revision_date = '" + next_revision_date + "' WHERE sno = " + str(SNO))

    print("Data updated successfully!")

def main():
    connection = connectdatabase()
    
    while True:
        action = input("Do you want to select a subject or exit? (Subject: S , Exit:E)")
        
        if action == "E":
            print("Exiting the program.")
            break
        elif action == "S":
            subject = input("Enter the subject (Physics, Chemistry, Maths, English, Computer_Science): ")
            action = input("Do you want to add:A , update:U , show:S , or exit:E data in the table? ")
        
            if action == "A":
                add(connection, subject)
            elif action == "U":
                update(connection, subject)
            elif action == "S":
                display(connection, subject)
            elif action == "E":
                print("Exiting the program")
                break
            else:
                print("Invalid option")
        else:
            print("Invalid option")
    
    
    connection.close()



# Main Code
  
main()
