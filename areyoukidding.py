import json
import sys
from sodapy import Socrata
import folium
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

def printAll(row):
    for key in row.keys():
        print("Key: " + key + " Value: " + row[key])

def printResults():
    i = 1
    markers=[]
    for page in results:
        for row in page:
            to_print = "{}  {}\n".format(row['issue_time'],str(row['issue_date']))
            to_print += "Violation {}: {} Fine: ${}".format(row['violation_'],row['violation1'],row['fine_amt'])
            print("Ticket Number: {}  Location: {}".format(i,row['ticket_loc']))
            print(to_print)
            if 'lat' in row.keys() and 'long' in row.keys():
                print("Geolocation found: ({} , {})".format(row['lat'],row['long']))
                markers.append(([row['lat'],row['long']], to_print))
            i += 1
    makeMap(markers)
    print(reslen() + " Results Found")

def makeMap(markers):
    map_1 = folium.Map(location=[42.350489, -71.069099], zoom_start=10)
    for marker in markers:
        folium.Marker(location=marker[0], popup=marker[1]).add_to(map_1)
    map_1.save('tickets.html')

def queryStreet(street):
    client = Socrata('data.cityofboston.gov', None)
    tmp = ""
    page_offset = 0
    while (len(tmp) >= 1000 or page_offset == 0):
        tmp = client.get(dataset_id, q=street, offset=page_offset)
        results.append(tmp)
        page_offset += 1000

if __name__ == '__main__':
   queryStreet(input('Enter the street you received the ticket on: ').upper())
   printResults()