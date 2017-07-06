#!/usr/bin/python
#_*_ coding:utf-8 _*_


print ''' Phone Directory '''
import re
import pdb
numbers = {}
flist = []

''' Menu for take User Input '''


def choice():

    print "1. Add Record."
    print "2. Remove Record."
    print "3. Find Record."
    print "4. Print Records"
    print "5. Quit."

    ch = input("Enter Your Selection: ")
    if ch == 1:
        add_record()
    elif ch == 2:
        remove_record()
    elif ch == 3:
        find_record()
    elif ch == 4:
        print_record()
    elif ch == 5:
        pass
    else:
        print "Please Enter Valid Input"

''' Create Record '''


def add_record():
    add_record = True
    print('''Add Name and Number''')
    name = raw_input("Enter the Name:")
    if not re.match("^[A-Za-z]*$", name):
        print "Error! Only letters allowed!"
        pass
        choice()
    no = raw_input("Enter a Phone Number: ")
    if not re.match("^[0-9]+$", no):
        print "Error! Only Numbers allowed!"
        pass
        choice()
    numbers[name] = no
    print("Record Added")
    for x in numbers.keys():
        print("Name is: ", x, "Number is:", numbers[x])
    choice()

''' Find Record '''


def find_record():
    print('''Find Record''')
    if not bool(numbers):
        print("\n Directory is Empty .. Please Add the Record")
    else:
        val = raw_input("Enter Name or Number: ")
        for k, v in numbers.iteritems():
            if k.count(val) or v.count(val):
                print("Name is:" + k + "\tNumber is:" + v)
                '''flist.append(k)
                # flist.append(v)
                print flist'''
            else:
                print("Record Not Found")
                break

    choice()

''' Print Record '''


def print_record():
    print('''Telephone Numbers:''')
    if not bool(numbers):
        print("\n Directory is Empty .. Please Add the Record")
        pdb.set_trace()
    else:
        for x in numbers.keys():
            print("Name is: ", x, "Number is:", numbers[x])
    choice()


''' Remove Record '''


def remove_record():
    print('''Remove Records''')
    ch = raw_input("Enter Name or Number")
    for k, v in numbers.items():
        if k.find(ch):
            del numbers[k]
            print "Record Removed"
        elif v.find(ch):
            del numbers[k]
            print "Record Removed"
        else:
            print "Record Not Found"
    choice()

choice()
