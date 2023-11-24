def start_spring(**kwargs):
    type_element={}
    result=''
    for element,type in kwargs.items():
        if type not in type_element:
            type_element[type]=[]
        type_element[type].append(element)

    type_element = dict(sorted(type_element.items(), key=lambda kvp: (-len(kvp[1]),kvp[0])))
    for type in type_element:
        type_element[type]=sorted(type_element[type])

    for type,element in type_element.items():
        result+=type+':'+'\n-'+'\n-'.join(element)+'\n'
    return result

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

