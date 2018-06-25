# domen


## Importing data

curl -XPUT http://ELASTIC_HOST:9200/colonnes -H'Content-Type: application/json' -d '
{
 "mappings" : {
  "_default_" : {
   "properties" : {
    "Colonne ID" : {"type": "string", "index" : "not_analyzed" },
    "Commentaire" : {"type": "string", "index" : "not_analyzed" },
    "Data type" : {"type": "string", "index" : "not_analyzed" },
    "Data type pivot" : {"type": "string", "index" : "not_analyzed" },
    "Données perso" : {"type": "string", "index" : "not_analyzed" },
    "FK" : {"type": "string", "index" : "not_analyzed" },
    "Longueur" : {"type": "string", "index" : "not_analyzed" },
    "Nom Colonne long" : {"type": "string", "index" : "not_analyzed" },
    "Nom court" : {"type": "string", "index" : "not_analyzed" },
    "agr_age_maxi" : {"type": "string", "index" : "not_analyzed" },
    "Not null" : {"type": "string", "index" : "not_analyzed" },
    "PK" : {"type": "string", "index" : "not_analyzed" },
    "Table ID" : {"type": "string", "index" : "not_analyzed" }
   }
  }
 }
}
';