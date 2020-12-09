from flask import Flask, render_template, abort, request, redirect, url_for, g, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/{}'.format(app.root_path, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'b2de7FkqvkMyqzNFzxCkgnPKIGP6i4Rc'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('book', lazy=True))
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('author', lazy=True))
    description = db.Column(db.Text, nullable=False)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100), nullable = False)

    def check_password(self,value): 
        return check_password_hash(self.password,value)


db.create_all()


@app.before_request
def load_user(): 
    user_id = session.get("user_id")
    g.user = User.query.get(user_id) if user_id is not None else None

def login_required(func): 
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if g.user is None: 
            return redirect(url_for("login", next = request.url))
        return func(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST": 
        username = request.form["username"]
        password = request.form["password"]

        error = None 

        user = User.query.filter_by(username=username).first()

        if user is None: 
            error = "Incorrect username."
        elif not user.check_password(password): 
            error = "Incorrect password."
        
        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("admin_categories"))

        flash(error)
    return render_template("admin/login.html")

@app.route("/logout")
def logout(): 
    session.clear()
    return redirect(url_for("login"))

@app.route("/register")
def register(): 
    user = User(username="admin", password=generate_password_hash("admin4books"))
    db.session.add(user)
    db.session.commit()     

    return redirect(url_for("login"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse(): 
    categories = Category.query.all()
    return render_template("browse.html", categories = categories)



@app.route("/category/<name>")
def category(name): 
    category = Category.query.filter(Category.name == name).first()
    books = Book.query.filter(Book.category_id == category.id)
    return render_template("category.html", category = category, books = books)

@app.route("/book/<book>")
def book(book): 
    book = Book.query.filter(Book.title == book).first()
    return render_template("book.html", book = book)

@app.route('/admin')
@app.route('/admin/categories')
@login_required
def admin_categories():
    categories = Category.query.all()
    return render_template('admin/category.html', categories=categories)

@app.route('/admin/book')
@login_required
def admin_books():
    books = Book.query.all()
    return render_template('admin/book.html', books=books)

@app.route('/admin/author')
@login_required
def admin_author():
    authors= Author.query.all()
    return render_template('admin/author.html', authors=authors)   

@app.route('/admin/create/category', methods=('GET', 'POST'))
@login_required
def create_category():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
    
        error = None
        
        if not name:
            error = 'Name is required.'

        if not description: 
            error = 'Description is required.'
            
        if error is None:
            category = Category(name=name, description = description)
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('admin_categories'))
    
        flash(error)

    categories = Category.query.all()
    return render_template('admin/category_form.html', categories=categories)

@app.route('/admin/create/book', methods=('GET', 'POST'))
@login_required
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_id = request.form['author_id']
        category_id = request.form['category_id']
        error = None
            
        if error is None:
            book = Book(title=title,description=description,author_id=author_id,category_id=category_id)
            print('book object: ', book)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('admin_books'))
    
        flash(error)

    books = Book.query.all()
    categories = Category.query.all()
    authors = Author.query.all()
    return render_template('admin/book_form.html', books=books, authors = authors, categories = categories)

@app.route('/admin/create/author', methods=('GET', 'POST'))
@login_required
def create_author():
    if request.method == 'POST':
        name = request.form['name']
    
        error = None
        
        if not name:
            error = 'Name is required.'
        
        if error is None:
            author = Author(name=name)
            db.session.add(author)
            db.session.commit()
            return redirect(url_for('admin_author'))
    
        flash(error)

    authors = Author.query.all()
    return render_template('admin/author_form.html', authors=authors)


@app.route('/admin/edit/category/<id>', methods=('GET', 'POST'))
@login_required
def edit_category(id):

    category = Category.query.get_or_404(id)

    if request.method == 'POST':
        category.name = request.form['name']
        category.description = request.form['description']

        error = None
        
        if not request.form['name']:
            error = 'Name is required.'
       
        if error is None:
            db.session.commit()
            return redirect(url_for('admin_categories'))
    
        flash(error)

    return render_template('admin/category_form.html', name=category.name, description=category.description)

@app.route('/admin/edit/author/<id>', methods=('GET', 'POST'))
@login_required
def edit_author(id):

    author = Author.query.get_or_404(id)

    if request.method == 'POST':
        author.name = request.form['name']

        error = None
        
        if not request.form['name']:
            error = 'Name is required.'
       
        if error is None:
            db.session.commit()
            return redirect(url_for('admin_author'))
    
        flash(error)

    return render_template('admin/author_form.html', name=author.name)

@app.route('/admin/edit/book/<id>', methods=('GET', 'POST'))
@login_required
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.description = request.form['description']
        book.author_id = request.form['author_id']
        book.category_id = request.form['category_id']

        error = None
            
        if error is None:
            db.session.commit()
            return redirect(url_for('admin_books'))
    
        flash(error)

    categories = Category.query.all()
    authors = Author.query.all()
    return render_template('admin/book_form.html', title = book.title, description = book.description, categories=categories, authors=authors, author_name = book.author.name, category_name = book.category.name)

@app.route('/admin/delete/category/<id>', methods=('GET', 'POST'))
@login_required
def delete_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        error = None
      
        if error is None:
            Category.query.filter_by(id=id).delete()
            db.session.commit()
            return redirect(url_for('admin_categories'))
    
        flash(error)

    return render_template('admin/category_deleteform.html', name=category.name)

@app.route('/admin/delete/book/<id>', methods=('GET', 'POST'))
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        error = None
      
        if error is None:
            Book.query.filter_by(id=id).delete()
            db.session.commit()
            return redirect(url_for('admin_books'))
    
        flash(error)

    return render_template('admin/book_deleteform.html', title=book.title)

@app.route('/admin/delete/author/<id>', methods=('GET', 'POST'))
@login_required
def delete_author(id):
    author = Author.query.get_or_404(id)
    if request.method == 'POST':
        error = None
      
        if error is None:
            Author.query.filter_by(id=id).delete()
            db.session.commit()
            return redirect(url_for('admin_author'))
    
        flash(error)

    return render_template('admin/author_deleteform.html', name=author.name)
