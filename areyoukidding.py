import json
from sodapy import Socrata

#client = Socrata(api_endpoint, app_token)
client = Socrata('data.cityofboston.gov', None)

dataset_id = 'qbxx-ev3s'

street = raw_input('Enter the street you received the ticket on: ').upper()

print "RECEIVED INPUT '" + street + "'"

print "QUERYING FOR STREET"
test = client.get(dataset_id, street_nam=street)
print "STREET QUERIED"
#jsonelem[elem_name][row_of_json][index_of_list]
#print test[0]

#test1 = json.dumps(test[0])

#print "\n\n\n"
#print test1

print "\n"

for row in test:
    print row['ticket_loc'] + " with a violation of: " + row['violation1']
print str(len(test)) + " Results Found"

#print json.dumps(test)
