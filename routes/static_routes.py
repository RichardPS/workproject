# 3rd Party
from bottle import get
from bottle import route
from bottle import static_file
from bottle import view

# Routes
# Static files routes
@get('/<filename:re:.*\.js>')
def javascript(filename):
    """Static route for javascript."""
    return static_file(filename, root='static/js')


@get('/<filename:re:.*\.css>')
def stylesheet(filename):
    """Static route for stylesheets."""
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def image(filename):
    """Static route for images."""
    return static_file(filename, root='static/images')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def font(filename):
    """Static route for fonts."""
    return static_file(filename, root='static/fonts')

# Public page routes
@route('/')
@view('index')
def index(page_title='Home Page'):
    return dict(page_title=page_title)

@route('/sds')
@view('sds')
def sds(page_title='Service Delivery Screen'):
    return dict(page_title=page_title)

# Private page routes
@route('/admin')
@view('template')
def admin(page_title='Admin Area'):
    return dict(page_title=page_title)
