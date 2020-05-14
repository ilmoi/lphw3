from flask import Flask, render_template, url_for, request, make_response
from markupsafe import Markup, escape
import random

app = Flask(__name__)

#the basics!
@app.route('/blog')
def blog_post():
    return 'youve reached the brog post! congrats!'

# the basics, but this time function and url same name
@app.route('/login')
def login():
    return 'login'

# trying user input
@app.route('/blog/<post_id>')
def subpost(post_id):
    return 'post %d' % int(post_id)

#handling user input correctly with escape
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# trying post (postman)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form['username']
        return f'receiving your info! - looks like you sent {data}'
    else:
        return 'showing you the login form!'

# trying jinja2 and templates
@app.route('/moisejevs')
def moisejevs():
    return render_template('moisejevs.html')

# jinja2 with a variable
@app.route('/') #so this is a decorator! makes sense! its job is to tell flask what url should trigger the below code
def hello_world():
    greeting = 'Helloz Worldz'
    return render_template('index.html', greeting=greeting)

#cookies - setting it
@app.route('/setz_cookiez')
def setz_cookiez():
    resp = make_response(render_template('moisejevs.html'))
    resp.set_cookie('randomzzz',f'diz numberz {random.randint(1,11111)}')
    return resp

#cookies - getting it
@app.route('/getz_cookiez')
def getz_cookiez():
    randomzzz = request.cookies.get('randomzzz')
    return f'yourz numberz waz {randomzzz}'

#collecing data from form
@app.route('/hello', methods=['GET','POST'])
def hello():
    greeting = "Hello World!"

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template('index.html',greeting=greeting)
    else:
        return render_template('hello_form.html')

with app.test_request_context():
    print(url_for('blog_post'))
    print(url_for('login'))
    print(url_for('profile', username='ilja moi'))
    print(url_for('static', filename='style.css'))

if __name__ == "__main__":
    app.run()
