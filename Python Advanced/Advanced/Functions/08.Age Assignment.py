def age_assignment(*args,**kwargs):
    name_age_dict={}
    for name in args:
        flett=name[0]
        name_age_dict[name]=kwargs[flett]
    return name_age_dict


# print(age_assignment("Peter", "George", G=26, P=19))