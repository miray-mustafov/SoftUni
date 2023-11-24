import json
USERS_FILE_LOCATION='./data_base/users.txt'

def register(username,email,password):
    user_objdict={"username":username,"email":email, "password" : password}

    user_json=json.dumps(user_objdict)

    with open(USERS_FILE_LOCATION, 'r+') as file_users:
        for user_line in file_users:
            current_user_dict=json.loads(user_line.strip())
            if username == current_user_dict["username"]:
                return False
        file_users.write(user_json+'\n')
        return True


def login(username,password):
    with open(USERS_FILE_LOCATION,'r+') as file_users:
        for user_line in file_users:
            current_user_dict=json.loads(user_line.strip())
            if username == current_user_dict['username'] and password == current_user_dict['password']:
                return True
        return False