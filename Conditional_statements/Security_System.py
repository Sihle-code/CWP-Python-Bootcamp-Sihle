# Smart Security System 
#Smart Security System: Create variables for has_keycard, knows_password, and is_admin. Allow access only if (has_keycard AND knows_password) OR is_admin is True.

has_password = True
has_keycard = False
is_admin = True
new_user = True 

# Auto-grant only if all credentials (adjust as needed)
if has_password and has_keycard and is_admin:
    print('Acccess granted')
elif  has_password and has_keycard and not is_admin:
    print("Access denied")
else:
    print('\n1. Enter password or keycard\n')
    print('\n2. Is Admin\n')
    print('\n3. New user\n')

choice = input('')

if choice == "1" and has_password and has_keycard:
    print("Access granted, you may proceed")
elif choice == "2" and is_admin:
    print("Hello Administrator, you may proceed...")
elif choice == "3" and new_user:
    print("Printing new user setup...")
else:
    print("Please reach out to your school facilitator for login inquiries")

