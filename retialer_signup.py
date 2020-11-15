def add_new_retailer(request,cursor,con):
    #select id from customers ORDER BY id DESC LIMIT 1
    cursor.execute("""select id from retailers ORDER BY id DESC LIMIT 1""")
    last_id = cursor.fetchall()[0][0]
    new_id = 'r'+str(int(last_id[-1])+1)
    cursor.execute("""INSERT INTO `retailers`(`id`, `name`, `phone`, `password`) VALUES ('{}','{}','{}','{}')"""
    .format(new_id,request.form['signup_name'],request.form['signup_phone'],request.form['signup_pass']))
    con.commit()


def auth_login_retailer(request,cursor):
    #SELECT `password`,`id` FROM `customers` WHERE phone = '9876543210'
    cursor.execute(""" SELECT `password`,`id` FROM `retailers` WHERE phone = '{}'""".format(request.form['signin_phone']))
    password_ids = cursor.fetchall()
    if(len(password_ids)>0):
        if(password_ids[0][0]==request.form['signin_pass']):
            return password_ids[0][1]
        else:
            return False
    else:
        return False   
    

def get_ret_data(cursor,x):
    #SELECT * FROM `retailers` WHERE id="r2"
    cursor.execute("""SELECT `name` FROM `retailers` WHERE id='{}'""".format(x))
    Name = cursor.fetchall()[0][0]
    data = {}
    data['Name'] = Name

    #get summary
    cursor.execute("""SELECT * FROM `products` WHERE id='{}' and Is_Avaliable='0'""".format(x))
    summary = cursor.fetchall()
    data['sold_count'] = len(summary)
    avg = 0
    for i in summary:
        avg = avg + int(i[1])
    avg = int(avg/len(summary))
    data['total_earning'] = avg
    #get avl product
    cursor.execute("""SELECT * FROM `products` WHERE id='{}' and Is_Avaliable='1'""".format(x))
    data['ava_pro'] = cursor.fetchall()
    return data

def add_new_product(request,cursor,con,ret_id):
    '''
    images = ['Guduchi_powder','Amukkura_churanam','Ashwagandha','Triphala','product']
    found = False
    for i in range(len(images)):
        if(request.files['myfile'].find(images[i]) > -1):
            found = True
            break
    '''
    cursor.execute("""INSERT INTO `products`(`name`, `price`, `quantity_remain`, `id`, `Is_Avaliable`)
     VALUES ('{}','{}','{}','{}','{}')""".format(request.form['name']
    ,request.form['price'],request.form['quantity'],ret_id,'1'))
    con.commit()