from flask import (
    Flask,
    render_template,
)
from db import POSTS
app = Flask(__name__)

# MVC - Model View Controller
# Model - True, View - Controller, Controller - Template


# html_hello = """
# <html>
#     <head>
#         <title>Main Page</title>
#     </head>
#     <body>
#         <a href='https://google.com'> <h1> Список товаров</h1> </a>
#     </body>
# </html>
# """


@app.route('/')
def index():
    page_title = 'MyPage'
    name = 'Anton'
    return render_template('index.html', page_title=page_title, name=name)


@app.route('/hi')
def hola():
    names = ['Anton', 'Max', 'John', 'Mike', 'Luiz', 'Ann']
    return render_template('greetings.html', names=names)


@app.route('/posts')
@app.route('/posts/<int:post_id>')
def posts(post_id=None):

    if post_id:
        return render_template('post_body.html', post=POSTS[post_id-1])
    return render_template('posts.html', posts=POSTS)




if __name__ == '__main__':
    app.run(debug=True)
