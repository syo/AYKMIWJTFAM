import json
from sodapy import Socrata
#from easygui import *
#from Tkinter import *

#from tkinter import *

dataset_id = 'qbxx-ev3s'
results = []

#client = Socrata(api_endpoint, app_token)
#jsonelem[elem_name][row_of_json][index_of_list]

def reslen():
    ct = 0
    for page in results:
        ct += len(page)
    return str(ct)

def printResults():
    for page in results:
        for row in page:
            print row['ticket_loc'] + " with a violation of: " + row['violation1']
    print reslen() + " Results Found"

def queryStreet(street):
    client = Socrata('data.cityofboston.gov', None)
    tmp = ""
    page_offset = 0
    while (len(tmp) >= 1000 or page_offset == 0):
        tmp = client.get(dataset_id, q=street, offset=page_offset)
        results.append(tmp)
        page_offset += 1000


if __name__ == '__main__':
   #streetname = enterbox("Enter street name: ", "Are You Kidding Me?")
   '''root = Tk()
   label = Label( root, text="Enter street name: ")
   E = Entry(root, bd =5)
   print E.get()
   submit = Button(root, text ="Submit", command = getDate)
   label.pack()
   E.pack()
   submit.pack(side =BOTTOM)
   root.mainloop()'''
   queryStreet(raw_input('Enter the street you received the ticket on: ').upper())
   printResults()
