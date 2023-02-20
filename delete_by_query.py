from elasticsearch7 import Elasticsearch

es = Elasticsearch("https://13.126.94.151:9200/", verify_certs=False, http_auth=('elastic', 'Dexanalytics@2022#'))  # Dexanalytics@2022#

q = {
  "query": {
    "match": {
      "Client_name": "new"
    }
  }
}
es.delete_by_query(body=q, index='dex_registration_dummy')
