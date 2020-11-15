from flask import Flask,render_template,redirect,url_for,request,redirect
from mysql.connector import connect
from customer_signup import auth_login_customer,add_new_customer,get_cust_data
from retialer_signup import auth_login_retailer,add_new_retailer,get_ret_data,add_new_product


app = Flask(__name__)
#con = connect(host='127.0.0.1',user='root',password='',database='mrdoctor')
#cursor = con.cursor()



@app.route("/")
def default():
    return render_template('landing.html')


@app.route("/ta/public/")
def public_index_tamil(): #by default tamil
    return render_template('public/t_index.html')

@app.route("/public/")
def public_index(): #by default tamil
    return render_template('public/index.html')



#problems
@app.route("/public/allergy/")
def allergy(): 
    return render_template('public/allergy.html')

@app.route("/public/body-pain/")
def body_pain(): 
    return render_template('public/body_pain.html')

@app.route("/public/digestion/")
def digestion():
    return render_template('public/digestion.html')

@app.route("/public/flu/")
def flu(): 
    return render_template('public/flu.html')

@app.route("/public/headache/")
def headache(): 
    return render_template('public/headache.html')

@app.route("/public/injury/")
def injury():
    return render_template('public/injury.html')



#other static

@app.route("/public/nearby/")
def nearby():
    return render_template('public/nearby.html')

@app.route("/public/shop-cust/")
def shop_cust():
    return render_template('public/shop_cust.html')

@app.route("/public/library/")
def library():
    return render_template('public/library.html')

@app.route("/public/forum-public/")
def forum_public():
    return render_template('public/forum_public.html')

@app.route("/public/verify/")
def verify():
    return render_template('public/verify.html')


@app.route("/public/ta/digestion/")
def tamil_digest():
    return render_template('public/t_digestion.html')



#public login
@app.route("/public/login-public/",methods=['POST','GET'])
def public_login():
    return render_template('public/login_public.html')

@app.route("/public/login-public/customer/")
def public_dashboard():
    return render_template('public/shop_cust.html')



#doctor
@app.route("/doctor/")
def login_doc():
    return render_template('doctor/index.html')

@app.route("/doctor/login-doc/")
def doctor_login():
    return render_template('doctor/login_doc.html')

@app.route("/doctor/forum-doc/")
def forum_doc():
    return render_template('doctor/forum_doc.html')

@app.route("/doctor/library/")
def library_doc():
    return render_template('doctor/library.html')

@app.route("/doctor/nearby/")
def nearby_doc():
    return render_template('doctor/nearby.html')

@app.route("/doctor/verify/")
def verify_doc():
    return render_template('doctor/verify.html')

@app.route("/doctor/patient-record/")
def patient_record():
    return render_template('doctor/patient_record.html')




#retailer
@app.route("/retailer/")
def retailer_index():
    return render_template('seller/login_seller.html')

@app.route("/retailer/dashboard/")
def retailer_dashboard():
    return render_template('seller/shop_ret.html')

if __name__=="__main__":
    app.run(debug=True)
