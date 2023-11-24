import os
while True:
    command=input()
    if command=="End":
        break
    command=command.split('-')
    operation,file_name=command[0:2]

    if operation=="Create":
        open(file_name,'w').close()
    elif operation=="Add":
        content=command[-1]
        with open(file_name,'a') as file:
            file.write(content+'\n')
    elif operation == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    elif operation=="Replace":
        if not os.path.exists(file_name):
            print("An error occurred")
            continue

        old,new=command[-2:len(command)]
        file =open(file_name, 'r')
        content=file.read()
        replaced_content=content.replace(old,new,100)
        file.close()
        file=open(file_name,'w')
        file.write(replaced_content)
        file.close()
