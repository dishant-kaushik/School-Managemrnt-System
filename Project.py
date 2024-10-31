import os
import platform
import mysql.connector
import pandas as pd    

def selection():
    db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
    cursor = db.cursor()
    print('---------------------------\nWELCOME TO SHREE RAM SCHOOL\n-----------------------------')
    print("1. STUDENT MANAGEMENT")
    print('2. EMPLOYEE MANAGEMENT')
    print('3. FEE MANAGEMENT')
    print('4. EXAM MANAGEMENT')

    ch = int(input("\nEnter your choice(1-4):"))
    if ch ==1:
        print('\nWELCOME TO OUR SCHOOL\n')
        print('a. NEW ADMISSION')
        print('b. UPDATE STUDENT DETAILS')
        print('c. ISSUE TC')
        c = input("Enter your choice(a-c):")
        print("\nInitially the details are...\n")

        display1()

        if c =='a':
            insert1()
            print('\nModified details are..\n')
            display1()
        elif c =='b':
            update1()
            print('\nModified details are..\n')
            display1()
        elif c == 'c':
            delete1()
            print('\nModified details are..\n')
            display1()
        else:
            print("Enter the correct choice")

    elif ch ==2:
        print('\nWELCOME TO OUR SCHOOL\n')
        print('a. NEW EMPLOYEE')
        print('b. UPDATE SSTAFF DETAILS')
        print('c. DELETE EMPLOYEE')
        c = input("Enter your choice(a-c):")
        print("\nInitially the details are...\n")

        display2()

        if c =='a':
            insert2()
            print('\nModified details are..\n')
            display2()
        elif c =='b':
            update2()
            print('\nModified details are..\n')
            display2()
        elif c == 'c':
            delete2()
            print('\nModified details are..\n')
            display2()
        else:
            print("Enter the correct choice")
    
    elif ch == 3:
        print('\nWELCOME TO OUR SCHOOL\n')
        print('a. NEW FEE')
        print('b. UPDATE STUDENT FEE')
        print('c. EXAM FEE')
        c = input("Enter your choice(a-c):")
        print("\nInitially the details are...\n")

        if c =='a':
            insert3()
        elif c =='b':
            update3()
        elif c == 'c':
            delete3()
        else:
            print("Enter the correct choice")
    
    elif ch == 4:
        print('\nWELCOME TO OUR SCHOOL\n')
        print('a. EXAM DETAILS')
        print('b. UPDATE DETAILS')
        print('c. DELETE DETAILS')
        c = input("Enter your choice(a-c):")

        if c =='a':
            insert4()
        elif c =='b':
            update4()
        elif c == 'c':
            delete4()
        else:
            print("Enter the correct choice")

    else:
        print("!!!....Please Enter correct choice....!!!")

    def insert1():
        std_name = input("Enter name of Student:")
        ad_num = int(input("Enter Admission Number:"))
        DOB = input("Enter Date of Birth(yyyy-mm-dd):")
        cls = input("Enter class for admission:")
        city = input("Enter your City Name:")
        db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
        cursor = db.cursor()
        sql = "INSERT INTO student(std_name,ad_num,DOB,cls,city)VALUES('%s','%d','%s','%s','%s')"%(std_name,ad_num,DOB,cls,city)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

    def display1():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                DOB = c[2]
                cls = c[3]
                city = c[4]
                print("(std_name=%s,ad_num = %d, DOB = %s, cls = %s, city= %s)"%(std_name,ad_num,DOB,cls, city))
        except:
            print("Unable to fetch data")
            db.close()

    def update1():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                DOB = c[2]
                cls = c[3]
                city = c[4]
        except:
            print("Error: Unable to fetch data")
        print()
        tempst = int(input("Enter Admission Number:"))
        temp = input("Enter new class:")
        try:
            sql = "Update Student set cls =  %s where ad_num = '%d'"%(temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.clode()

    def delete1():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                DOB = c[2]
                cls = c[3]
                city = c[4]
        except:
            print("Error: Unable to fetch data")

        temp = int(input("\nEnter admission number to be deleted:"))
        try:
            sql = "delete from student where ad_num = '%d'"%(temp)
            ans = input("Are you sure you want to delete the record(y/n):")
            if ans =='y'or ans =='Y':
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print(e)
            db.close()

    def insert2():
        ename = input("Enter Employee name:")
        empno = int(input("Enter Employee Number:"))
        job = input("Enter Designation:")
        hiredate = input("Enter joining Date:")
        db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
        cursor = db.cursor()
        sql = "INSERT INTO emp(ename,empno, job, hiredate)VALUES('%s','%d','%s','%s')"%(ename,empno,job,hiredate)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

    def display2():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM emp"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                ename = c[0]
                empno = c[1]
                job = c[2]
                hiredate = c[3]
                print("(ename=%s,empno = %d, job = %s, hiredate = %s)"%(ename,empno,job,hiredate))
        except:
            print("Unable to fetch data")
            db.close()

    def update2():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM emp"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                ename = c[0]
                empno = c[1]
                job = c[2]
                hiredate = c[3]
        except:
            print("Error: Unable to fetch data")
        print()
        tempst = int(input("Enter Employee Number:"))
        temp = input("Enter new Designation :")
        try:
            sql = "Update emp set job =  %s where empno = '%d'"%(temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.clode()

    def delete2():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM emp"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                ename = c[0]
                empno = c[1]
                job = c[2]
                hiredate = c[3]
        except:
            print("Error: Unable to fetch data")

        temp = int(input("\nEnter employee number to be deleted:"))
        try:
            sql = "delete from emo where empno = '%d'"%(temp)
            ans = input("Are you sure you want to delete the record(y/n):")
            if ans =='y'or ans =='Y':
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print(e)
            db.close()

    def insert3():
        admno = int(input("Enter admission number :"))
        fee = float(input("Enter Fee Amount:"))
        month = input("Enter Month:")
        db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
        cursor = db.cursor()
        sql = "INSERT INTO fee(admno,fee, month)VALUES('%d','%d','%s')"%(admno,fee,month)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()
    
    def display3():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM fee"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                admno  = c[0]
                fee = c[1]
                month = c[2]
                print("(admno=%d,fee = %s, month = %s)"%(admno,fee,month))
        except:
            print("Unable to fetch data")
            db.close()
  
    def update3():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM fee"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                admno = c[0]
                fee = c[1]
                month = c[2]
        except:
            print("Error: Unable to fetch data")
        print()
        tempst = int(input("Enter Admission Number:"))
        temp = input("Enter new Class:")
        try:
            sql = "Update fee set month =  %s where admno = '%d'"%(temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.clode()
    
    def delete3():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM fee"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                admno = c[0]
                fee = c[1]
                month = c[2]
        except:
            print("Error: Unable to fetch data")

        temp = int(input("\nEnter Admission number to be deleted:"))
        try:
            sql = "delete from students where admno = '%d'"%(temp)
            ans = input("Are you sure you want to delete the record(y/n):")
            if ans =='y'or ans =='Y':
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print(e)
            db.close()

    def insert4():
        std_name = input("Enter name of Student:")
        ad_num = int(input("Enter Admission Number:"))
        per = float(input("Enter the percentage:"))
        res = input("Enter Result:")
        db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
        cursor = db.cursor()
        sql = "INSERT INTO student(std_name,ad_num,per,res)VALUES('%s','%d','%s','%s')"%(std_name,ad_num,per,res)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

    def display4():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM exam"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                per = c[2]
                res = c[3]
                print("(std_name=%s,ad_num = %d, per = '%s', res = '%d')"%(std_name,ad_num,per,res))
        except:
            print("Unable to fetch data")
            db.close()

    def update4():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM fee"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                per = c[2]
                res = c[3]
        except:
            print("Error: Unable to fetch data")
        print()
        tempst = int(input("Enter Admission Number:"))
        temp = input("Enter new Result:")
        try:
            sql = "Update student set res =  %s where admno = '%d'"%(temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.clode()

    def delete4():
        try:
            db = mysql.connector.connect(user = 'root', password = 'Great', host = "localhost", database = 'mysql')
            cursor = db.cursor()
            sql = "SELECT * FROM exam"
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                std_name = c[0]
                ad_num = c[1]
                per = c[2]
                res = c[3]
        except:
            print("Error: Unable to fetch data")

        temp = int(input("\nEnter Admission number to be deleted:"))
        try:
            sql = "delete from exam where admno = '%d'"%(temp)
            ans = input("Are you sure you want to delete the record(y/n):")
            if ans =='y'or ans =='Y':
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print(e)
            db.close()
    selection()



