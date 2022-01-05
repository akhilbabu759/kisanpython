from flask import Flask,render_template,request
from DBConnection import Db


app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        uname=request.form['username']
        password=request.form['password']
    else:
        return render_template("login.html")



@app.route('/approve_center')
def approve_center():
    qry = "select *from center"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/Approve Center.html",res=res)

@app.route('/approved_center_view')
def approved_center_view():
    qry = "select *from center"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/Approved Center View.html",res=res)

@app.route('/booking_master')
def booking_master():
    return render_template("admin/View Booking Master.html")

@app.route('/booking_master_report',methods=['GET','POST'])
def booking_master_report():
    if request.method=="POST":
        report=request.form['textarea']
    else:
        return render_template("admin/Booking Master Report.html")

@app.route('/complaint')
def complaint():
    qry = "select *from complaint"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/View Complaint.html",res=res)

@app.route('/complaint_replay',methods=['GET','POST'])
def complaint_replay():
    if request.method=="POST":
        reply=request.form['textarea']
    else:
        return render_template("admin/Complaint Replay.html")

@app.route('/feedback')
def feedback():
    qry = "select *from feedbackr"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/View feedback.html",res=rse)

@app.route('/rating')
def rating():
    qry = "select *from rating"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/view _rating.html",res=res)

@app.route('/product')
def product():
    qry = "select * from product"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/View Product.html",res=res)

@app.route('/booking')
def booking():
    qry = "select *from booking"
    obj = Db()
    res = obj.select(qry)
    return render_template("admin/View BOOKING.HTML",res=res)

@app.route('/payment')
def payment():
    return render_template("admin/View Payment.html")

@app.route('/user')
def user():
    qry= "select *from user"
    obj=Db()
    res=obj.select(qry)
    return render_template("admin/View User.html", res=res)

@app.route('/home')
def home():
    return render_template("admin/admin home.html")








if __name__ == '__main__':
    app.run()
