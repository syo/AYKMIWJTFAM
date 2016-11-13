from sodapy import Socrata

#client = Socrata(api_endpoint, app_token)
client = Socrata('data.cityofboston.gov', None)

dataset_id = 'qbxx-ev3s'

test = client.get(dataset_id, limit=2)

print test
