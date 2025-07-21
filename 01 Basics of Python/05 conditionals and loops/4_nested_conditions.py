# if inside another if

is_logged_in = True
has_access = True

if is_logged_in:
    if has_access:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("Please log in first.")