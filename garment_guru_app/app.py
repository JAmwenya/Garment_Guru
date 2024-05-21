#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.database import StoreImage, FileStorage, create_session
from models.basket import Basket
from models.closet import Closet
from models.status import Status
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Push an application context so we can use `db.engine`
with app.app_context():
    db.create_all() # Create tables
    session = create_session(db.engine)
    file_storage = FileStorage(db.engine)
 
 # main page route
@app.route('/')
def garmentmain():
    images = file_storage.all()
    baskets = db.session.query(Basket).all()
    closets = db.session.query(Closet).all()
    users = db.session.query(User).all()
    statuses = db.session.query(Status).all()

    return render_template('garmentguru.html', images=images, baskets=baskets, closets=closets, users=users, statuses=statuses)

@app.route('/home')
def index():

    return render_template('landing_page.html')

@app.route('/basket/<int:page>')
def show_basket(page=1):
    # Query the database for images in the basket
    pagination = StoreImage.query.filter(StoreImage.basket_id.isnot(None)).paginate(page, per_page=10)
    return render_template('basket.html', pagination=pagination)

@app.route('/closet/<int:page>')
def show_closet(page=1):
    # Query the database for images in the closet
    pagination = StoreImage.query.filter(StoreImage.closet_id.isnot(None)).paginate(page, per_page=10)
    return render_template('closet.html', pagination=pagination)

# user route
@app.route('/user')
def show_user():
    users = db.session.query(User).all()
    return render_template('user.html', users=users)

# image upload route
@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    # Save the image to the database
    image_data = file.read()
    image_name = file.filename
    user_id = request.form.get('user_id', '')
    new_image = StoreImage(filename=image_name, image_data=image_data, user_id=user_id)
    file_storage.new(new_image)
    return 'File uploaded successfully'

#toggle route
@app.route('/toggle_status/<int:image_id>', methods=['POST'])
def toggle_status(image_id):
    # Retrieve the status of the garment
    status = Status.query.filter_by(image_id=image_id).first()
    if status:
        # Toggle the status
        status.is_clean = not status.is_clean
        # If the status is clean, move the garment to the closet
        if status.is_clean:
            closet = Closet.query.filter_by(image_id=image_id).first()
            if not closet:
                closet = Closet(image_id=image_id)
                db.session.add(closet)
            basket = Basket.query.filter_by(image_id=image_id).first()
            if basket:
                db.session.delete(basket)
        # If the status is dirty, move the garment to the basket
        else:
         
            basket = Basket.query.filter_by(image_id=image_id).first()
            if not basket:
                basket = Basket(image_id=image_id)
                db.session.add(basket)
            closet = Closet.query.filter_by(image_id=image_id).first()
            if closet:
                db.session.delete(closet)
    else:
        # Create a new status entry
        status = Status(image_id=image_id, is_clean=True)
        db.session.add(status)
    db.session.commit()
    # Redirect back to the previous page
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)    
