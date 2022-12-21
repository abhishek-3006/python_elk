import csv
from datetime import datetime
import json
import config
from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200", verify_certs=False, basic_auth=('elastic', 'fJJMZzHP9QBeImzrX3Ex'))

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
obj = es.get(index='kibana_sample_data_flights', id='3M1OGoUBKTO7F7eW1VHZ')
print(obj)
# search_obj = es.search(index='kibana_sample_data_flights', pretty=True, query={"Carrier": 'ES-Air'})
# with open("elk.json", "w") as outfile:
#     outfile.write(json.dumps(search_obj.body, indent=4))

es.indices.create(
    index="laptop-demo",
    settings=config.configurations["settings"],
    mappings=config.configurations["mappings"],
)

with open("laptops-demo.csv", "r") as fi:
    reader = csv.DictReader(fi, delimiter=",")

    actions = []
    for row in reader:
        action = {"index": {"_index": 'laptop-demo', "_id": int(row["id"])}}
        doc = {
            "id": int(row["id"]),
            "name": row["name"],
            "price": float(row["price"]),
            "brand": row["brand"],
            "attributes": [
                {"cpu": row["cpu"]},
                {"memory": row["memory"]},
                {"storage": row["storage"],
                 },
            ],
        }
        actions.append(action)
        actions.append(doc)

    es.bulk(index='laptop-demo', operations=actions)
