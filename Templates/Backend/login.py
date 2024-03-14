from flask import Flask, render_template, request, redirect, url_for

class LoginApp():
    def __init__(self):
        # Dummy user data (replace with your authentication logic)
        self.users = {'admin': 'password'}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
app = Flask(__name__)

# Instantiate LoginBackend
login_backend = LoginApp()

# Define routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if login_backend.login(username, password):
        # Redirect to a success page or dashboard
        return redirect(url_for('success'))
    else:
        # Render login page with an error message
        return render_template('login.html', error='Invalid username or password')

@app.route('/success')
def success():
    return 'Login Successful!'
    


