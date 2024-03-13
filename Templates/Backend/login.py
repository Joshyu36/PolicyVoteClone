from flask import Flask, render_template, request, redirect, url_for

class LoginApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dummy user data (replace with your authentication logic)
        self.users = {'admin': 'password'}

        # Routes
        self.add_url_rule('/', 'index', self.index)
        self.add_url_rule('/login', 'login', self.login, methods=['POST'])
        self.add_url_rule('/success', 'success', self.success)

    def index(self):
        return render_template('login.html')

    def login(self):
        username = request.form['username']
        password = request.form['password']

        if username in self.users and self.users[username] == password:
            # Redirect to a success page or dashboard
            return redirect(url_for('success'))
        else:
            # Render login page with an error message
            return render_template('login.html', error='Invalid username or password')

    def success(self):
        return 'Login Successful!'


