configurations = {
    "settings": {
        "index": {"number_of_replicas": 2},
        "analysis": {
            "filter": {
                "ngram_filter": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15,
                },
            },
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "ngram_filter"],
                },
            },
        },
    },
    "mappings": {
        "properties": {
            "id": {"type": "long"},
            "name": {
                "type": "text",
                "analyzer": "standard",
                "fields": {
                    "keyword": {"type": "keyword"},
                    "ngrams": {"type": "text", "analyzer": "ngram_analyzer"},
                },
            },
            "brand": {
                "type": "text",
                "fields": {
                    "keyword": {"type": "keyword"},
                },
            },
            "price": {"type": "float"},
            "attributes": {
                "type": "nested",
                "properties": {
                    "attribute_name": {"type": "text"},
                    "attribute_value": {"type": "text"},
                },
            },
        }
    },
}