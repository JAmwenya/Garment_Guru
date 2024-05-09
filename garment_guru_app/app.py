#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models.database import StoreImage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

# index route
@app.route('/')
def index():
    return render_template('garmentguru.html')

# landing page route
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    user_id = request.form['user_id']
    file = request.files['file']
    image_data = file.read()
    image_name = file.filename
    new_upload = StoreImage(filename=image_name, user_id=user_id, image_data=image_data)
    db.session.add(new_upload)
    db.session.commit()
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
