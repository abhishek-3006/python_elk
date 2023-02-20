from elasticsearch7 import Elasticsearch

es = Elasticsearch("https://13.126.94.151:9200/", verify_certs=False, http_auth=('elastic', 'Dexanalytics@2022#'))  # Dexanalytics@2022#
val = "ctx._source['Client_name'] = '{0}'"
q = {
  "script": {
    "source": val.format("test")
  },
  "query": {
    "term": {
      "Nationality.keyword": "(a) a citizen of India"
    }
  }
}

es.update_by_query(body=q, index='dex_registration_dummy')
