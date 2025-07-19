# Real-life logic combining multiple operators

is_logged_in = True
has_permission = True
age = 22

can_access = is_logged_in and has_permission and age >= 18
print("Can access model dashboard:", can_access)