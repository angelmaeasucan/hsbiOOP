from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from datetime import datetime

# Object-Oriented Programming Implementation

class User:
    def __init__(self, name, email, role):
        self._name = name  # Encapsulation: private attribute
        self._email = email  # Encapsulation: private attribute
        self._role = role  # Encapsulation: private attribute

    # Getter methods for encapsulation
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_role(self):
        return self._role

    # Setter methods for encapsulation
    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_role(self, role):
        self._role = role

    # Abstraction: hide internal details
    def display_info(self):
        return f"Name: {self._name}, Email: {self._email}, Role: {self._role}"

    # Polymorphism: method to be overridden
    def display_role(self):
        return f"Role: {self._role}"

class Admin(User):  # Inheritance: Admin inherits from User
    def __init__(self, name, email):
        super().__init__(name, email, "admin")  # Call parent constructor

    # Polymorphism: overriding display_role method
    def display_role(self):
        return f"Role: Administrator - Full Access"

class Cashier(User):  # Inheritance: Cashier inherits from User
    def __init__(self, name, email):
        super().__init__(name, email, "cashier")  # Call parent constructor

    # Polymorphism: overriding display_role method
    def display_role(self):
        return f"Role: Cashier - Limited Access"

class BillingSystem:  # Main class for the billing system - Encapsulation
    def __init__(self):
        # Encapsulation: private attributes for data
        self._customers = [
            {'id': '0101', 'name': 'Juan', 'contact': '09223456789', 'address': 'Tubigon'},
            {'id': '0000', 'name': 'Jhonavie', 'contact': '09220987654', 'address': 'Clarin'},
            {'id': '0001', 'name': 'Angel', 'contact': '09123456789', 'address': 'Dagohoy'},
            {'id': '0002', 'name': 'Maria', 'contact': '09123452459', 'address': 'Danao'},
            {'id': '0003', 'name': 'John', 'contact': '09123456789', 'address': 'Mactan'},
            {'id': '0004', 'name': 'Jane', 'contact': '09123456789', 'address': 'Bantayan'},
            {'id': '0005', 'name': 'Heart', 'contact': '09958840258', 'address': 'Nahud'},
        ]

        self._products = [
            {'id': '1001', 'name': 'Laptop', 'category': 'Electronics', 'price': 45000, 'stock': 'Available', 'status': 'active'},
            {'id': '1010', 'name': 'Television', 'category': 'Electronics', 'price': 32000, 'stock': 'Available', 'status': 'active'},
            {'id': '1234', 'name': 'Refrigerator', 'category': 'Appliances', 'price': 23000, 'stock': 'Available', 'status': 'active'},
            {'id': '1235', 'name': 'Washing Machine', 'category': 'Appliances', 'price': 18000, 'stock': 'Available', 'status': 'active'},
            {'id': '14000', 'name': 'Printer', 'category': 'Electronics', 'price': 5000, 'stock': 'Not Available', 'status': 'active'},
            {'id': '1237', 'name': 'Blender', 'category': 'Appliances', 'price': 2000, 'stock': 'Available', 'status': 'active'},
            {'id': '1238', 'name': 'Toaster', 'category': 'Appliances', 'price': 1500, 'stock': 'Available', 'status': 'active'},
        ]

        self._sales = [
             {'id': '1', 'product': 'Television', 'quantity': 1, 'total': 32000, 'date': '2024-06-01', 'customer': 'Jhonavie', 'payment_type': 'cash'},
        ]

        self._bills = [
            {'id': 1, 'customer_id': '0000', 'customer': 'Jhonavie', 'amount': 32000, 'date': '2024-06-01', 'status': 'Paid', 'description': 'Television purchase', 'type': 'Full Payment'},
        ]

        self._activities = []

        self._user_credentials = {
            'admin': {'password': 'admin', 'role': 'admin'},
            'cashier': {'password': 'cashier', 'role': 'cashier'}
        }

        self._payments = []  # Assuming payments list exists

    # Abstraction: methods to access private data
    def get_customers(self):
        return self._customers

    def get_products(self):
        return self._products

    def get_sales(self):
        return self._sales

    def get_bills(self):
        return self._bills

    def get_activities(self):
        return self._activities

    def get_payments(self):
        return self._payments

    def get_user_credentials(self):
        return self._user_credentials

    # Encapsulated helper methods
    def log_activity(self, activity_type, description, user="System"):
        activity = {
            'id': len(self._activities) + 1,
            'type': activity_type,
            'description': description,
            'user': user,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self._activities.insert(0, activity)
        if len(self._activities) > 20:
            self._activities = self._activities[:20]

    def get_dashboard_metrics(self):
        total_customers = len(self._customers)
        total_sales = sum(s['total'] for s in self._sales)
        total_products = len(self._products)
        total_products_sold = sum(s['quantity'] for s in self._sales)
        pending_payments = sum(b['amount'] for b in self._bills if b['status'] == 'Unpaid')
        total_bills = len(self._bills)
        paid_bills = len([b for b in self._bills if b['status'] == 'Paid'])
        unpaid_bills = len([b for b in self._bills if b['status'] == 'Unpaid'])
        pending_bills = len([b for b in self._bills if b['status'] == 'Pending'])
        total_revenue = sum(b['amount'] for b in self._bills if b['status'] == 'Paid')
        return {
            'total_customers': total_customers,
            'total_sales': total_sales,
            'total_products': total_products,
            'total_products_sold': total_products_sold,
            'pending_payments': pending_payments,
            'total_bills': total_bills,
            'paid_bills': paid_bills,
            'unpaid_bills': unpaid_bills,
            'pending_bills': pending_bills,
            'total_revenue': total_revenue,
            'billing_data': self._bills,
            'activity_log': self._activities,
            'recent_activities': self._activities[:10],
            'recent_bills': self._bills[-5:]
        }

    # Methods for operations
    def add_customer(self, c_id, c_name, contact, address):
        if any(c['id'] == c_id for c in self._customers):
            return "Customer ID already exists!"
        self._customers.append({'id': c_id, 'name': c_name, 'contact': contact, 'address': address, 'status': 'Active'})
        self.log_activity('customer', f'Added: {c_name}', 'admin')
        return None

    def delete_customer(self, customer_id):
        self._customers[:] = [c for c in self._customers if c['id'] != customer_id]
        self.log_activity('customer', f'Deleted ID: {customer_id}', 'admin')

    def add_product(self, p_id, p_name, cat, prc, stk):
        if any(str(p['id']) == str(p_id) for p in self._products):
            return "Product ID already exists!"
        self._products.append({'id': p_id, 'name': p_name, 'category': cat, 'price': float(prc), 'stock': stk, 'status': 'active'})
        self.log_activity('product', f'Added: {p_name}', 'admin')
        return None

    def edit_product(self, product_id, name, price, category, stock):
        product = next((p for p in self._products if str(p['id']) == str(product_id)), None)
        if product:
            product['name'] = name
            product['price'] = float(price)
            product['category'] = category
            product['stock'] = stock
            self.log_activity('product', f'Edited: {name}', 'admin')
            return True
        return False

    def delete_product(self, product_id):
        self._products[:] = [p for p in self._products if str(p['id']) != str(product_id)]
        self.log_activity('product', f'Deleted ID: {product_id}', 'admin')

    def add_sale(self, prod_name, cust_name, cust_id, qty, pay_type, date):
        matched_prod = next((p for p in self._products if p['name'] == prod_name), None)
        if not prod_name or not cust_name or not qty or qty <= 0:
            return "Please select a product, customer and enter a valid quantity."
        if not matched_prod:
            return "Selected product not found."
        
        total_p = matched_prod['price'] * qty
        new_sale = {
            'id': len(self._sales) + 1,
            'customer_id': cust_id,
            'product': prod_name,
            'customer': cust_name,
            'quantity': qty,
            'total': total_p,
            'date': date,
            'payment_type': pay_type
        }
        self._sales.append(new_sale)
        
        if pay_type == 'cash':
            self._bills.append({
                'id': len(self._bills) + 1,
                'customer': cust_name,
                'amount': total_p,
                'date': date,
                'status': 'Paid',
                'description': f'Full payment {prod_name}',
                'type': 'Full Payment'
            })
        self.log_activity('sale', f'Added sale: {prod_name} to {cust_name}', 'admin')
        return None

    def add_bill(self, customer, customer_id, amount, date, status, bill_type, description):
        if not customer or not amount or not date:
            return "All fields are required!"
        try:
            amount = float(amount)
            new_id = max([b['id'] for b in self._bills], default=0) + 1
            if not customer_id:
                for c in self._customers:
                    if c['name'] == customer:
                        customer_id = c['id']
                        break
            self._bills.append({
                'id': new_id,
                'customer_id': customer_id,
                'customer': customer,
                'amount': amount,
                'date': date,
                'status': status,
                'description': description,
                'type': bill_type
            })
            self.log_activity('billing', f'Bill added for {customer}', 'admin')
            return None
        except ValueError:
            return "Invalid amount!"

    def add_payment(self, payment_data):
        self._payments.append(payment_data)
        self.log_activity('payment', f"Payment recorded: {payment_data['payment_id']}", 'admin')

    def authenticate_user(self, username, password):
        if username in self._user_credentials:
            if password == self._user_credentials[username]['password']:
                self.log_activity('login', f'User {username} logged in', username)
                role = self._user_credentials[username]['role']
                return role
        return None

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Use environment secret if available

# Create instance of BillingSystem - Abstraction
billing_system = BillingSystem()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get('username', '').strip().lower()
        password = request.form.get('password', '').strip()

        role = billing_system.authenticate_user(username, password)
        if role:
            session['username'] = username
            session['role'] = role
            if role == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif role == 'cashier':
                return redirect(url_for('cashier_dashboard'))
        else:
            error = "Invalid username or password!"
    return render_template('login.html', error=error)

@app.route('/admin')
def admin_dashboard():
    return render_template('admin/dashboard.html', **billing_system.get_dashboard_metrics())

@app.route('/cashier')
def cashier_dashboard():
    return render_template('cashier/dashboard.html', **billing_system.get_dashboard_metrics())

@app.route('/customer_management', methods=['POST', 'GET'])
def customer_management():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') == 'cashier' and request.method == 'POST' and 'save_customer' in request.form:
        return redirect(url_for('customer_management'))
    error = None
    search_query = ''
    if request.method == 'POST':
        if 'save_customer' in request.form:
            c_id = request.form.get('customerId', '').strip()
            c_name = request.form.get('customerName', '').strip()
            contact = request.form.get('contactNo', '').strip()
            address = request.form.get('address', '').strip()
            if not c_id or not c_name or not contact:
                error = "Customer ID, Name, and Contact are required!"
            else:
                error = billing_system.add_customer(c_id, c_name, contact, address)
                if not error:
                    return redirect(url_for('customer_management'))
        elif 'search_customer' in request.form:
            search_query = request.form.get('searchInput', '').strip().lower()
    
    customers = billing_system.get_customers()
    filtered = [c for c in customers if search_query in c['id'].lower() or search_query in c['name'].lower()] if search_query else customers
    template = 'cashier/customer.html' if session.get('role') == 'cashier' else 'admin/customer.html'
    return render_template(template, customers=filtered, error=error, search_query=search_query)

@app.route('/delete_customer/<customer_id>')
def delete_customer(customer_id):
    billing_system.delete_customer(customer_id)
    return redirect(url_for('customer_management'))

@app.route('/products', methods=['POST', 'GET'])
def products_management():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') == 'cashier' and request.method == 'POST' and 'save_product' in request.form:
        return redirect(url_for('products_management'))
    error = None
    search_query = ''
    if request.method == 'POST':
        if 'save_product' in request.form:
            p_id = request.form.get('productId', '').strip()
            p_name = request.form.get('productName', '').strip()
            cat = request.form.get('category', '').strip()
            prc = request.form.get('price', '').strip()
            stk = request.form.get('stock', '').strip()
            if not p_id or not p_name or not cat or not prc or not stk:
                error = "All fields are required!"
            else:
                try:
                    error = billing_system.add_product(p_id, p_name, cat, prc, stk)
                    if not error:
                        return redirect(url_for('products_management'))
                except ValueError: 
                    error = "Invalid Price format!"
        elif 'search_product' in request.form:
            search_query = request.form.get('searchInput', '').strip().lower()
            
    products = billing_system.get_products()
    filtered = [p for p in products if search_query in str(p['id']) or search_query in p['name'].lower()] if search_query else products
    template = 'cashier/product.html' if session.get('role') == 'cashier' else 'admin/product.html'
    return render_template(template, products=filtered, error=error, search_query=search_query)

@app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    products = billing_system.get_products()
    product = next((p for p in products if str(p['id']) == str(product_id)), None)
    if request.method == 'POST' and product:
        name = request.form.get('productName')
        price = request.form.get('price')
        category = request.form.get('category')
        stock = request.form.get('stock')
        billing_system.edit_product(product_id, name, price, category, stock)
        return redirect(url_for('products_management'))
    return render_template('admin/product.html', products=products, edit_product=product)

@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    billing_system.delete_product(product_id)
    return redirect(url_for('products_management'))

@app.route('/sales', methods=['GET', 'POST'])
def sales_management():
    if 'username' not in session:
        return redirect(url_for('login'))

    search_query = ''
    filtered = billing_system.get_sales()  # default display

    if request.method == 'POST':
        # =========================
        # ADD SALE
        # =========================
        if 'add_sale' in request.form:
            prod_name = request.form.get('product')
            cust_name = request.form.get('customer')
            cust_id = request.form.get('customer_id')
            qty = request.form.get('quantity')
            pay_type = request.form.get('payment_type')
            date = request.form.get('date')

            # safe convert quantity
            try:
                qty = int(qty)
            except:
                qty = 0

            error = billing_system.add_sale(prod_name, cust_name, cust_id, qty, pay_type, date)
            if error:
                return render_template(
                    'admin/sales.html' if session.get('role') != 'cashier' else 'cashier/sales.html',
                    sales=filtered,
                    products=billing_system.get_products(),
                    search_query=search_query,
                    error=error
                )
            return redirect(url_for('sales_management'))

        # =========================
        # SEARCH SALE
        # =========================
        elif 'search_sale' in request.form:
            search_query = request.form.get('searchInput', '').strip().lower()

            filtered = []
            for s in billing_system.get_sales():
                sale_id = str(s.get('id', '')).lower()
                customer = str(s.get('customer', '')).lower()
                product = str(s.get('product', '')).lower()
                cust_id = str(s.get('customer_id', '')).lower()

                if (
                    search_query in sale_id or
                    search_query in customer or
                    search_query in product or
                    search_query in cust_id
                ):
                    filtered.append(s)

    template = 'cashier/sales.html' if session.get('role') == 'cashier' else 'admin/sales.html'

    return render_template(
        template,
        sales=filtered,
        products=billing_system.get_products(),
        search_query=search_query
    )

@app.route('/delete_sale/<sale_id>', methods=['POST'])
def delete_sale(sale_id):
    sales = billing_system.get_sales()
    sales[:] = [s for s in sales if str(s.get('id')) != str(sale_id)]
    return redirect(url_for('sales_management'))

@app.route('/billing', methods=['GET', 'POST'])
def billing_management():
    if 'username' not in session:
        return redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        if 'add_bill' in request.form:
            customer = request.form.get('customer', '').strip()
            customer_id = request.form.get('customer_id', '').strip()
            amount = request.form.get('amount', '').strip()
            date = request.form.get('date', '').strip()
            status = request.form.get('status', 'Unpaid')
            bill_type = request.form.get('type', 'Manual')
            description = request.form.get('description', '').strip()
            
            error = billing_system.add_bill(customer, customer_id, amount, date, status, bill_type, description)
        search_query = request.form.get('searchInput', '').lower()
    else:
        search_query = ''
    
    bills = billing_system.get_bills()
    filtered_bills = [b for b in bills if search_query in b['customer'].lower()] if search_query else bills
    
    metrics = billing_system.get_dashboard_metrics()
    template = 'cashier/billing.html' if session.get('role') == 'cashier' else 'admin/billing.html'
    return render_template(template, bills=filtered_bills, 
                           total_bills=metrics['total_bills'], paid_bills=metrics['paid_bills'], 
                           unpaid_bills=metrics['unpaid_bills'], total_collected=metrics['total_revenue'],
                           outstanding_amount=sum(b['amount'] for b in bills if b['status'] != 'Paid'),
                           bills_json=json.dumps(filtered_bills), pending_bills=metrics['pending_bills'],
                           search_query=search_query, error=error)

@app.route('/update_bill_status/<int:bill_id>/<status>')
def update_bill_status(bill_id, status):
    bills = billing_system.get_bills()
    for b in bills:
        if b['id'] == bill_id:
            b['status'] = status
    return redirect(url_for('billing_management'))

@app.route('/delete_bill/<int:bill_id>')
def delete_bill(bill_id):
    bills = billing_system.get_bills()
    bills[:] = [b for b in bills if b['id'] != bill_id]
    return redirect(url_for('billing_management'))


# PAYMENT FORM
@app.route('/payment', methods=['GET', 'POST'])
def payment_form():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        payment_data = {
            "payment_id": request.form.get('payment_id'),
            "payment_date": request.form.get('payment_date'),
            "customer": request.form.get('customer'),
            "customer_id": request.form.get('customer_id'),
            "invoice_no": request.form.get('invoice_no'),
            "due_date": request.form.get('due_date'),
            "payment_type": request.form.get('payment_type'),
            "gcash_number": request.form.get('gcash_number'),
            "reference_number": request.form.get('reference_number'),
            "total_due": request.form.get('total_due'),
            "amount_paid": request.form.get('amount_paid'),
            "remaining_balance": request.form.get('remaining_balance'),
            "payment_status": request.form.get('payment_status'),
            "remarks": request.form.get('remarks'),
            "processed_by": request.form.get('processed_by')
        }

        # SAVE PAYMENT
        billing_system.add_payment(payment_data)
        print("\n===== PAYMENT RECORDED =====")
        print(payment_data)

        return redirect(url_for('payment_receipt', payment_id=payment_data['payment_id']))

    template = 'cashier/payment.html' if session.get('role') == 'cashier' else 'admin/payment.html'
    return render_template(
        template,
        customers=billing_system.get_customers(),
        bills=billing_system.get_bills(),
        payments=billing_system.get_payments(),
        now=datetime.now()
    )


@app.route('/payment_receipt/<payment_id>')
def payment_receipt(payment_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    payment = next((p for p in billing_system.get_payments() if p.get('payment_id') == payment_id), None)
    if payment is None:
        return redirect(url_for('payment_form'))

    return render_template('cashier/payment_receipt.html', payment=payment)

@app.route('/payment_success')
def payment_success():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    payments = billing_system.get_payments()
    last_payment = payments[-1] if payments else None
    template = 'cashier/payment.html' if session.get('role') == 'cashier' else 'admin/payment.html'
    return render_template(template, 
                         success_message="Payment Successfully Recorded!",
                         last_payment=last_payment,
                         customers=billing_system.get_customers(),
                         bills=billing_system.get_bills(),
                         payments=payments,
                         now=datetime.now())


# VIEW ALL PAYMENTS
@app.route('/payments')
def view_payments():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('payment_form'))

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    if request.method == 'POST':
        search_query = request.form.get('searchInput', '').lower()
    else:
        search_query = request.args.get('searchInput', '').lower()

    bills = billing_system.get_bills()
    payments = billing_system.get_payments()
    overdue_bills = [b for b in bills if b['status'] != 'Paid']
    payments_for_report = payments
    if search_query:
        overdue_bills = [b for b in overdue_bills if search_query in b['customer'].lower()]
        payments_for_report = [p for p in payments if search_query in p.get('customer', '').lower() or search_query in p.get('payment_id', '').lower() or search_query in p.get('invoice_no', '').lower()]

    total_overdue = len(overdue_bills)
    overdue_amount = sum(b['amount'] for b in overdue_bills)
    reminder_list = [f"Reminder for {b['customer']}: ₱{b['amount']} due on {b.get('due_date', b['date'])}" for b in overdue_bills]
    template = 'cashier/report.html' if session.get('role') == 'cashier' else 'admin/report.html'
    return render_template(template,
                           overdue_bills=overdue_bills,
                           reminder_list=reminder_list,
                           search_query=search_query,
                           total_overdue=total_overdue,
                           overdue_amount=overdue_amount,
                           payments=payments_for_report,
                           total_payments=len(payments_for_report),
                           total_payment_amount=sum(float(p.get('amount_paid', 0)) for p in payments_for_report))

@app.route('/users')
def users():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') != 'admin':
        return redirect(url_for('cashier_dashboard'))
    user_list = [{'username': k, **v} for k, v in billing_system.get_user_credentials().items()]
    return render_template('admin/user.html', users=user_list)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    billing_system.log_activity('system', 'System Start', 'System')
    app.run(debug=True)
    
handler = app