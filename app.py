from flask import Flask, render_template,url_for

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route("/")
def home():
    return render_template('index.html')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
