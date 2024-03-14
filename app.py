from flask import Flask
from Templates.Backend.login import LoginApp
from database import Database, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
# Create a Flask application instance
app = Flask(__name__)
login_app = LoginApp()

# Instantiate Database object
db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

# Define a route and its associated view function
@app.route('/')
def hello():
    db.connect()

    # Example: execute a SELECT query
    rows = db.execute_query('SELECT * FROM admins_users')

    # Close the database connection
    db.close()

    return str(rows)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
