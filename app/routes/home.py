from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later.
bp = Blueprint('home', __name__, url_prefix='/')

# We then define two new functions: index() and login().
# In each case, we add a @bp.route() decorator before the
# function to turn it into a route. Whatever the function
# returns becomes the response. And this time,
# we use the render_template() function to respond with a template instead of a string.


@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template('homepage.html', posts=posts)


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post page
    return render_template('single-post.html', post=post)
