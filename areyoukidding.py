from sodapy import Socrata

client = Socrata("https://data.cityofboston.gov/resource/cpdb-ie6e.json", None)

test = client.get("ticket_loc", limit=2)

print test
