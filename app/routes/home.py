from flask import Blueprint, render_template

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later. 
bp = Blueprint('home', __name__, url_prefix='/')

# We then define two new functions: index() and login(). 
# In each case, we add a @bp.route() decorator before the 
# function to turn it into a route. Whatever the function 
# returns becomes the response. And this time, 
# we use the render_template() function to respond with a template instead of a string.
@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')