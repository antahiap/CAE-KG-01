from SPARQLWrapper import SPARQLWrapper, JSON


# sparql = SPARQLWrapper(
#     "http://vocabs.ardc.edu.au/repository/api/sparql/"
#     "csiro_international-chronostratigraphic-chart_geologic-time-scale-2020"
# )

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
# sparql = SPARQLWrapper("https://query.dbpedia.org/sparql")

sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
sparql.setQuery("""
    PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>
    PREFIX schema: <http://schema.org/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbo:    <http://dbpedia.org/ontology/>
    PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX bd: <http://www.bigdata.com/rdf#>


    SELECT distinct STR(?vehicle)
    WHERE
    {
      ?uri dbo:industry dbr:Automotive_industry.
      ?uri rdfs:label ?vehicle.
Filter (lang(?vehicle)="en")
    }
    """)


# # SELECT *
# # WHERE {
# #     ?veh a dbr:Vehicle;
# #     ?veh rdfs:comment ?cm.
# # }
# # ORDER BY ?veh
# # LIMIT 100
# # """
# #             )

try:
    ret = sparql.queryAndConvert()

    print(ret)
    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
