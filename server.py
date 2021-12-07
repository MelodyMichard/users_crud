from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users = User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')
    
@app.route('/user/get/<int:id>')
def get(id):
    return render_template("show_user.html", user = User.get({"id": id}))

@app.route('/user/update-user/<int:id>')
def updateUser(id):
    return render_template("update_user.html", user = User.get({"id": id}))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')   

@app.route('/user/delete/<int:id>')
def delete(id):
    User.delete({"id": id})
    return redirect('/users')   

if __name__=="__main__":
    app.run(debug=True)