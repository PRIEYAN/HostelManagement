from flask import Flask, request, url_for, render_template, session , redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///login.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)




with app.app_context():
    db.create_all()  
    #sample data in database
    new_user = User(username="prieyan", email="prieyan@gmail.com", password="12345")
    db.session.add(new_user)
    db.session.commit()



# Main route and other route
@app.route('/')
def main():
    auth = session.get('username')                  
    return render_template('index.html', auth=auth)

@app.route('/roomProblem')
def roomProblem():
    auth=session.get('username') is not None
    if auth:
        username=session.get('username')
        return render_template('roomProblem.html',auth=auth,username=username)
    else:
        return render_template('login.html')

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, email=email, password=password).first()
        
        if user:
            session['username'] = user.username 
            return redirect(url_for('main') )  
        else:
            message = "Invalid credentials. Please try again."
            return render_template('login.html', message=message,)
    return render_template('login.html')






@app.route('/logout', methods=['GET'])
def done():
    session.pop('username', None)  
    return redirect(url_for('main'))




if __name__ == "__main__":
    app.run(debug=True, port=5000)
