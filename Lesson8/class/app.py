from flask import Flask
from flask import render_template
from db import POSTS

app = Flask(__name__)

@app.route('/')
def index():
    page_title = 'Mypage'
    name = 'Illia'
    return render_template('index.html',page_title = page_title, name = name)

@app.route('/hi')
def hola():
    names = ['Anton', 'Max', 'John', 'Mike','Luiz','Ann']
    return render_template('greetings.html', names = names)

@app.route('/posts')
@app.route('/posts/<int:post_id>')
def posts(post_id = None):
    if post_id:
        return render_template('post_body.html', post = POSTS[post_id -1])
    return render_template('posts.html', posts = POSTS)

if __name__ == '__main__':
    app.run(debug = True)
