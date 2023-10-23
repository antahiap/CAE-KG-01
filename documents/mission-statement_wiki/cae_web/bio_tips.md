- backend model - neo4j, orientDB
- frontend model - jsonDL, [openAPI](https://openapi-generator.tech/) ([typescript](https://openapi-generator.tech/docs/generators/typescript-axios/)), [graphql](https://www.howtographql.com/)
- database to frontend file format, json(fast to read) yaml(easy to edit)
- [openAPI.tools](https://openapi.tools/)?

### Display
- for re-usable visualization the data arriving at frontend has to have semantics, i.e. what data types each field has
- if it is 'just' display of one entry of a database SQL-table, the semantics is in the table
- if it is several objects with related objects, than a model for the data for the frontend is needed
- example development tree or embedding
  - frontend model of what is shown there, i.e. what is node or what is embedding point
  - each node / dot is a simulation, where additional information can be fetched / display for
  - additional information (pictures, curves, tables, ...) has separate frontend models
### Maintenance
- use CICD
- sync backend frontend model, [swagger](https://swagger.io/tools/swagger-editor/)

----

### orientDB start
create a model for your input data (ie XSD for XML)
- compile a parser from the model
- create a model for your output data (ie a graph for OrientDB)
- create an object-to-object mapper
- use an objet to relational mapper (ORM) to write into the database
	
if you use the right frameworks, almost no code needs to be written, just some models have to be created and the build system needs to be set up

the alternative is to manually convert everything into CSV and then import csv in OrientDB:
https://orientdb.com/docs/2.2.x/Import-from-CSV-to-a-Graph.html 

----

We have

    Analysis data from ModelCompare SimCompare DataViewer Neo4J data base (graph data of model)
    The results are stored in files and folders (except the data from graph, it is in Neo4J)

We want to

    Display the analysis results in a proper format on the web.
    Enable user to interact with the displayed data

Things we need to do

    Create a "Model" that represents what our data is and how to handle it by the WebAPI
    Create a "Model" for how the data should be displayed and how the user should interact with it
    Additional information on what should happen when user interacts with the displayed data

Examples

    To define Model for data in xml file , xlst is used
    To define Model for data in json files, openAPI / Swagger can be explored

Bio Tips

    Better to keep three different projects for Frontend, Backend and API. The build system will be complex but t will result in a good decoupled code