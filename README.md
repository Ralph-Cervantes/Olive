# Olive


## Approach 
- Create a server to handle api requests, a background worker to automatically fetch and clean external data and populate the database. 

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