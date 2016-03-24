#database.py
import sys,shelve

def store_person(db):
    """
    Query user for data and store it in the shelf object.
    """
    pid=input("Enter unique ID number:")
    person={}
    person['name']=input("Enter name:")
    person['age']=input("Enter age:")
    person['phone']=input("Enter phone number:")

    db[pid]=person

def lookup_person(db):
    """
    Query user for ID and desired field,and fetch the corresponding data from the shelf object.
    """
    pid=input("Enter ID number:")
    field=input('What would you like to know?(name,age,phone,all(show all information for person))')
    field=field.strip().lower()
    if field=='all':
        print("The information for person you lookup:")
        print('Pid: ',pid)
        print('Name: ',db[pid]['name'])
        print('Age: ',db[pid]['age'])
        print('Phone :',db[pid]['phone'])
    elif field in ['name','age','phone']:
        print(field.capitalize()+':',db[pid][field])
    else:
        print_help()

def print_help():
    print('The available comands are:')
    print('store   :Stores information about a person')
    print('lookup  :Looks up a person form ID number')
    print('quit    :Save changes and exit')
    print('?       :Print tips message')

def enter_command():
    cmd=input("Enter command(? for help):")
    cmd=cmd.strip().lower()
    return cmd

def main():
    #database=shelve.open('C:\\Users\\Ying\\Desktop\\database.dat')
    database=shelve.open('/home/abelit/Documents/database.dat')
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()

if __name__=='__main__':
    main()
