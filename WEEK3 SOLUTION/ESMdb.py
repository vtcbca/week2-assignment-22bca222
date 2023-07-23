#Write a python script to perform CRUD operation on following table of "ESM.db" database.

import sqlite3

con=sqlite3.connect("ESM.db")

#1.create table

tbl="create table IF NOT EXISTS employee(eid int primary key,ename text,dept text,basic int,branch text)"
c=con.cursor()
c.execute(tbl)
con.commit()

#2.insert record directly.

ins="insert into employee values(1,'om','HR',11000,'Surat'),\
                                (2,'sai','IT',15000,'Mumbai'),\
                                (3,'ram','IT',13000,'Delhi'),\
                                (4,'radha','Account',1000,'Kolkata'),\
                                (5,'kishan','Inventory',12000,'Surat');"
c.execute(ins)
con.commit()

#2.insert record using tuple

instpl=[(101,'krishna','HR',11000,'bardoli'),
        (102,'shyam','Inventory',13000,'vapi'),
        (103,'radha','kolkata',13000,'Delhi'),
        (104,'ram','IT',10000,'surat'),
        (105,'komal','HR',9000,'mumbai')]
q="insert into employee values(?,?,?,?,?)"
c.executemany(q,instpl)
con.commit()

#2.insert record through user

l=[]
for i in range(1):
    eid=int(input("Enter Employee ID:"))
    ename=input("Enter Employee NAME:")
    dept=input("Enter Employee DEPARTMENT:")
    basic=int(input("Enter Employee Basic Salary:"))
    branch=input("Enter Employee Branch Name:")
    t=(eid,ename,dept,basic,branch)
    l.append(t)
c.executemany(q,l)
con.commit()

#3.update record who are from "surat" with increment in salary 10%

q3="update employee set basic=basic+(basic*10)/100 where branch='surat'"
c.execute(q3)
con.commit()

#4. print all records.

q4="select * from employee"
c.execute(q4)
print("\n\n\n OUTPUT OF QUERY NO:-4 \n")
print(c.fetchall())
con.commit()

#5. Print records where dept is 'HR' and 'IT'.

q5="select * from employee where dept='HR' or dept='IT'"
c.execute(q5)
r5=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-5 \n")
print(r5)
con.commit()

#6.print record in sorting order of department.

q6="select*from employee order by dept"
c.execute(q6)
r6=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-6 \n")
print(r6)
con.commit()

#7.print record where basic is >6000

q7="select*from employee where basic>6000"
c.execute(q7)
r7=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-7 \n")
print(r7)
con.commit()

#8.print record where employee name second character is"r".

q8="select * from employee where ename like '_r%'"
c.execute(q8)
r8=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-8 \n")
print(r8)
con.commit(
    )
#9.Grouping record of employee who are from "Account" and "Inventory".

q9="select dept,count(*) from employee \
    group by dept having dept IN('Account','Inventory')"
c.execute(q9)
r9=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-9 \n")
print(r9)
con.commit()

#10.Print all records based on branch name in descending order.

q10="select*from employee order by branch desc"
c.execute(q10)
r10=c.fetchall()
print("\n\n\n OUTPUT OF QUERY NO:-10 \n")
print(r10)
con.commit()
con.close()












