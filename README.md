# domen


## Importing data

curl -XPUT http://35.229.165.129:9200/colonnes -H'Content-Type: application/json' -d '
{
 "mappings": {
  "doc": {
   "properties" : {
    "colonne_id" : {"type": "text"},
    "commentaire" : {"type": "text"},
    "data_type" : {"type": "text"},
    "data_type_pivot" : {"type": "text"},
    "donnees_perso" : {"type": "text"},
    "fk" : {"type": "text"},
    "longueur" : {"type": "text"},
    "nom_colonne_long" : {"type": "text"},
    "nom_court" : {"type": "text"},
    "agr_age_maxi" : {"type": "text"},
    "not_null" : {"type": "text"},
    "pk" : {"type": "text"},
    "table_id" : {"type": "text"}
   }
  }
 }
}
';

curl -H 'Content-Type: application/x-ndjson' -XPOST 'http://35.229.165.129:9200/colonnes/_bulk?pretty' --data-binary @colonnes_elastic.json