def sorting_cheeses(**kwargs):
    kwargs=dict(sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]),kvp[0])))
    for cheese in kwargs:
        kwargs[cheese]=sorted(kwargs[cheese],reverse=True)
    result=""
    for cheese,pieces in kwargs.items():
        result+=cheese+'\n'+'\n'.join([str(x) for x in pieces])+'\n'

    return result



print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
