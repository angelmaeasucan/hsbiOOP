from app import User, Admin, Cashier, BillingSystem

print("="*60)
print("TESTING ALL 4 PILLARS OF OBJECT-ORIENTED PROGRAMMING")
print("="*60)

# ENCAPSULATION TEST
print("\n1. ENCAPSULATION: Private attributes with getters/setters")
print("-" * 60)
user = User('John Doe', 'john@email.com', 'cashier')
print(f'User Name (via getter): {user.get_name()}')
print(f'User Email (via getter): {user.get_email()}')
print(f'User Role (via getter): {user.get_role()}')
user.set_name('Jane Doe')
print(f'After set_name: {user.get_name()}')

# INHERITANCE TEST
print("\n2. INHERITANCE: Admin and Cashier inherit from User")
print("-" * 60)
admin = Admin('Administrator', 'admin@email.com')
cashier = Cashier('Cashier User', 'cashier@email.com')
print(f'Admin inherits display_info: {admin.display_info()}')
print(f'Cashier inherits display_info: {cashier.display_info()}')

# POLYMORPHISM TEST
print("\n3. POLYMORPHISM: Same method, different outputs")
print("-" * 60)
print(f'User display_role(): {user.display_role()}')
print(f'Admin display_role(): {admin.display_role()}')
print(f'Cashier display_role(): {cashier.display_role()}')

# ABSTRACTION TEST
print("\n4. ABSTRACTION: BillingSystem hides implementation details")
print("-" * 60)
bs = BillingSystem()
metrics = bs.get_dashboard_metrics()
print(f'Total Customers: {metrics["total_customers"]}')
print(f'Total Products: {metrics["total_products"]}')
print(f'Total Bills: {metrics["total_bills"]}')
print(f'Total Revenue: PHP {metrics["total_revenue"]:,.2f}')
print(f'Activity Log Entries: {len(metrics["activity_log"])}')

print("\n" + "="*60)
print("ALL 4 PILLARS SUCCESSFULLY IMPLEMENTED IN app.py!")
print("="*60)
