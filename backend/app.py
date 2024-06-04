from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/scraping'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

@app.route('/scrape', methods=['POST'])
def scrape_product():
    url = request.json['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        title = soup.find('h1', class_='product-title').text.strip()
        description_html = soup.find('div', class_='product-short-description').prettify()
        price = soup.find('span', class_='amount').text.strip()
        category = "Beds"

        # Create new Product instance
        new_product = Product(
            title=title,
            description=description_html,
            price=price,
            category=category
        )
        
        # Add to session and commit to database
        db.session.add(new_product)
        db.session.commit()

        product_details = {
            'title': title,
            'description': description_html,
            'price': price,
            'category': category
        }

        return jsonify(product_details)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't already exist within an application context
    print('Server is running on port 5000')
    serve(app, host='0.0.0.0', port=5000)
