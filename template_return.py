from flask import Flask, redirect, url_for, request,render_template , jsonify
app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login1')
def login_form():
    return render_template("login.html")
 
@app.route('/login', methods=['POST'])
def login():
    # Get the login data from the request form
    username = request.form['username']
    password = request.form['password']

    # For demonstration, let's just print the login data
    print(f"Username: {username}, Password: {password}")
    return jsonify({'message': 'Login successful', 'redirect': '/dashboard'})
 
 
if __name__ == '__main__':
    app.run(debug=True)
