def add_new_customer(request,cursor,con):
    #select id from customers ORDER BY id DESC LIMIT 1
    cursor.execute("""select id from customers ORDER BY id DESC LIMIT 1""")
    last_id = cursor.fetchall()[0][0]
    new_id = 'c'+str(int(last_id[-1])+1)
    cursor.execute("""INSERT INTO `customers`(`id`, `name`, `phone`, `password`) VALUES ('{}','{}','{}','{}')"""
    .format(new_id,request.form['signup_name'],request.form['signup_phone'],request.form['signup_pass']))
    #con.commit()


def auth_login_customer(request,cursor):
    #SELECT `password`,`id` FROM `customers` WHERE phone = '9876543210'
    cursor.execute(""" SELECT `password`,`id` FROM `customers` WHERE phone = '{}'""".format(request.form['signin_phone']))
    password_ids = cursor.fetchall()
    if(len(password_ids)>0):
        if(password_ids[0][0]==request.form['signin_pass']):
            return password_ids[0][1]
        else:
            return False
    else:
        return False   

def get_cust_data(cursor,x):
    pass