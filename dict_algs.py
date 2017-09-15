ivan ={
    'name': 'ivan',
    'age': 34,
    'children': [{
        'name': 'vasya',
        'age': 12,
    },{
        'name': 'petya',
        'age': 10,
    }],
}

darya ={
    'name': 'darya',
    'age': 41,
    'children': [{
        'name': 'kirill',
        'age': 21,
    },{
        'name': 'pavel',
        'age': 15,
    }],
}

emps = [ivan,darya]

def poisk(dict,age):
    for note in dict:
        childrens=note['children']
        for child in childrens:
            if child['age']>age:
                print(note['name'])
None

poisk(emps,18)