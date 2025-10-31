# Olive


## Approach 
- To handle an unreliable external service, I decided to create an api to handle requests to the backend, a database 
to store the external service data, and a background worker to periodically fetch, clean and populate the database. The user
will use the client to hit our endpoints that then queries the database to ensure reliability and performance.  

## Usage: 
Ensure docker is installed before running 
Enter the command:
- make start

Allow the background worker several seconds on spinning up to populate the database on first run.

Available commands 
- make build (build the images)
- make up (start the containers)
- make down (stop the containers)
- make remove-tables (drop the tables)
- make create-tables (create the tables)