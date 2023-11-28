from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to My Flask App'

@app.route('/about')
def about():
    return 'About Us'

@app.route('/profile/<username>')
def profile(username):
    return f'Profile Page for {username}'

if __name__ == '__main__':
    app.run(debug=True)

