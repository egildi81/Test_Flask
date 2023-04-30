from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_id = request.form['author']
        book = Book(title=title, description=description, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!')
        return redirect(url_for('books'))
    return render_template('add_book.html', authors=authors)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        flash('Author added successfully!')
        return redirect(url_for('authors'))
    return render_template('add_author.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
