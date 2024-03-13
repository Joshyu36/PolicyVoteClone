from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and its associated view function
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
