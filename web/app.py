from flask import Flask, request, redirect,render_template, url_for

app = Flask(__name__)

#GET — used to send data back only
#POST — used to receive data

global user
user=''
target={}
@app.route('/home/<user>', methods=['GET', 'POST']) 
def home_page(user):
    if request.method == 'GET': #get data from previous redirect page (login_page)
        # target_calcories = request.values['']
        # target_proteins = request.values['']
        # target_fat = request.values['']
        # targeT_carbs = request.values['']
        return render_template("home.html", user=user)

    else:
        return render_template("home.html")

#Could Use
@app.route('/login', methods=['GET', 'POST']) 
def login_page():
    if request.method == 'POST': 
        user = request.values['username']
        # return render_template('home.html', user=user)
        return redirect(url_for("home_page",user=user))
    else:
        return render_template("login.html")
    

@app.route('/user')
def user_page():
    print(user)
    return render_template("user.html",user=user)


@app.route('/food',methods=['GET', 'POST'])
def food_page():
    print(user)
    return render_template("food.html",user=user)


@app.route('/charts',methods=['GET', 'POST'])
def chart_page():
    print(user)
    return render_template("chart.html",user=user)



if __name__ == '__main__':
    app.debug = True
    app.run()    