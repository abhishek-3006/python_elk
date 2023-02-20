import datetime

from elasticsearch7 import Elasticsearch

es = Elasticsearch("https://13.126.94.151:9200/", verify_certs=False, http_auth=('elastic', 'Dexanalytics@2022#'))  # Dexanalytics@2022#

# now = datetime.datetime.now()
timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
q = {
  "@timestamp": timestamp,
  "Client_name": "new",
  "Correspondence City": "Bandra"
}
es.index(document=q, index='dex_registration_dummy', id='1')
