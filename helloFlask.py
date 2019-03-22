# flask 框架

from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def home():
  return 'home Page'

@app.route('/hello')
def hello(name=None):
  return render_template('hello.html',name = name)

@app.route('/about')
def about():
  return 'about page 哈哈'  

@app.route('/user/<username>')
def showUser():
  return 'User %s' % username

@app.route('/post/<int:post_id>')
def showPost():
  return 'Post %d' % post_id

if __name__ == '__main__':
  app.run()  