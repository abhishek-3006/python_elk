from elasticsearch import Elasticsearch
import json
es = Elasticsearch("https://localhost:9200", verify_certs=True, ca_certs='C:/elasticsearch-8.5.0/config/certs/http_ca.crt', basic_auth=('elastic', 'fJJMZzHP9QBeImzrX3Ex'))

# search_obj = es.search(index='demo', pretty=True, size=100, query={"term": {"brand.keyword": "Lenovo"}})  # basic search
search_obj = es.search(index='demo', pretty=True, size=200, query={"match": {"name": {"query": "mode", "fuzziness": 2, "prefix_length": 1}}})  # fuzzy search
with open("elk.json", "w") as outfile:
    outfile.write(json.dumps(search_obj.body, indent=4))