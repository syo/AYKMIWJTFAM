import json
from sodapy import Socrata

dataset_id = 'qbxx-ev3s'
page_offset = 0
results = []

################################


#client = Socrata(api_endpoint, app_token)
client = Socrata('data.cityofboston.gov', None)

street = raw_input('Enter the street you received the ticket on: ').upper()

print "RECEIVED INPUT '" + street + "'"

print "QUERYING FOR STREET"

tmp = ""

while (len(tmp) >= 1000 or page_offset == 0):
    tmp = client.get(dataset_id, q=street, offset=page_offset)
    results.append(tmp)
    page_offset += 1000


print "STREET QUERIED"
#jsonelem[elem_name][row_of_json][index_of_list]
#print test[0]

#test1 = json.dumps(test[0])

#print "\n\n\n"
#print test1

print "\n"

result_count = 0
for page in results:
    result_count += len(page)
    for row in page:
        print row['ticket_loc'] + " with a violation of: " + row['violation1']
print str(result_count) + " Results Found"

#print json.dumps(test)
