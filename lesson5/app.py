from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"{self.name}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=True)
    content = db.Column(db.Text)
    author = db.Column(db.String(20), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    def __repr__(self):
        return f"{self.title}"


@app.route('/posts')
def posts():
    post_list = Post.query.all()
    return render_template('posts_list.html', posts=post_list)


@app.route('/posts/<int:id>')
def post_by_id(id):
    post = Post.query.get_or_404(id)
    return render_template('posts_detail.html', posts=post)


@app.route('/categories')
def categories():
    categories_list = Category.query.all()
    return render_template('categories_list.html', categories=categories_list)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
