import sys
import os
import csv
import codecs
from elasticsearch import Elasticsearch

csvfile="data/crime.csv"

mapping = {
    "crime_map": {
        "properties": {
            "State": {"type": "keyword"},
            "Murder": {"type": "float","index": "not_analyzed"},
            "Rape": {"type": "float","index": "not_analyzed"},
            "Robbery": {"type": "float","index": "not_analyzed"},
            "Aggravated_assault": {"type": "float","index": "not_analyzed"},
            "Burglary": {"type": "float","index": "not_analyzed"},
            "Larceny_theft": {"type": "float","index": "not_analyzed"},
            "Motor_vehicle_theft": {"type": "float","index": "not_analyzed"}
        }
    }
}

es = Elasticsearch()
if not es.indices.exists("crime"):
    es.indices.create("crime")

es.indices.put_mapping(index="crime",doc_type="crime_map",body=mapping)

with open(csvfile) as csvdata:
    reader=csv.reader(csvdata,delimiter=",",quotechar='"')
    next(reader)
    for id, row in enumerate(reader):
        print(row)
        content = {
            "State":row[0],
            "Murder":row[1],
            "Robbery":row[2],
            "Aggravated_assault":row[3],
            "Burglary":row[4],
            "Larceny_theft":row[5],
            "Motor_vehicle_theft":row[6]
        }
        es.index(index="crime",doc_type="crime_map",id=id,body=content)
