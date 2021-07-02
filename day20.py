import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Singapore@22",
    database="Employee"
)
cur = conn.cursor()
sql =("INSERT INTO Employee(Name,Emp_ID,Salary)VALUES(%s,%s,%s)")
values = [("sneha","12","80000"),
          ("kumar","22","60000"),
          ("rohini","54","70000"),
          ("kiran","24","50000")]
cur.executemany(sql,values)
conn.commit()

#query to get the maximum and minimum salary from employees table
cur.execute("SELECT MIN(Salary),MAX(Salary) FROM Employee")
myresult = cur.fetchall()
for i in myresult:
    print(i)
    
#query to get the number of employees working with the company
cur.execute("SELECT COUNT(DISTINCT Name) FROM Employee")
result = cur.fetchall()
for i in result:
    print(i)
    
#query to get the first 3 characters of first name from employees table
cur.execute("SELECT DISTINCT SUBSTRING(Name,1,3) FROM Employee")
res = cur.fetchall()
for i in res:
    print(i)
