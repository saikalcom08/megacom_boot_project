#создать словарь {login:password}
# CRUD  - create_user, get_user_password, update_password, delete_user

users = {"user1" : "password1", "user2": "password2", "user3" : "password3", "user4": "password4"}

#creating user
def create_user():
    user = input('Enter user name to create: ')

    if user in users:
        print("Already exists!")
    else:
        password = input("Enter password: ")
        users[user] = password
    print(users)

#get_user_password
def get_user_password():
    user = input('Enter which user you want to get: ')
    print(users.get(user))
    
def update_password():
    user = input("Which user's password you want to update?")
    password = input("Enter password to update: ")
    users.update({user: password})
    print(users)
    
def delete_user():
    user = input('Enter which user you want to delete: ')
    del users[user]
    print(users)

create_user()
get_user_password()
update_password()
delete_user()