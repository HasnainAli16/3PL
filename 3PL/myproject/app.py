from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('database.db')
cursor = db.cursor()

# Create the "products" table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    asin TEXT,
                    product_name TEXT,
                    fnsku TEXT
                  )''')
db.commit()

# Create the "shipments" table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS shipments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    shipment_name TEXT,
                    asin TEXT,
                    fnsku TEXT,
                    product_name TEXT,
                    variety TEXT,
                    quantity INTEGER,
                    status TEXT
                  )''')
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/catalog')
def catalog():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('catalog.html', products=products)

@app.route('/send-shipment', methods=['GET', 'POST'])
def send_shipment():
    if request.method == 'POST':
        # Handle shipment form submission
        # ...

        return redirect(url_for('in_progress_shipment'))

    return render_template('send_shipment.html')

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Handle add product form submission
        # ...

        return redirect(url_for('catalog'))

    return render_template('add_product.html')

@app.route('/dashboard')
def dashboard():
    # Retrieve necessary data for the dashboard
    # ...
    data = {}  # Replace with the actual data for the dashboard

    return render_template('dashboard.html', data=data)

@app.route('/in-progress-shipment')
def in_progress_shipment():
    # Retrieve in-progress shipment data
    cursor.execute("SELECT * FROM shipments WHERE status = 'in_progress'")
    shipments = cursor.fetchall()

    return render_template('in_progress_shipment.html', shipments=shipments)

@app.route('/completed-shipment')
def completed_shipment():
    # Retrieve completed shipment data
    cursor.execute("SELECT * FROM shipments WHERE status = 'completed'")
    shipments = cursor.fetchall()

    return render_template('completed_shipment.html', shipments=shipments)

if __name__ == '__main__':
    app.run(debug=True)
