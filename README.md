# CeresiaWebApp

---------------

A Desktop application for the Ceresia Object called Cerescope.
This project has been realized in the context of a course on databases in 2021 at CNAM.

The project is built with the Django.

It works with a POSTGRESQL database.

## Project contents

---------------

- [x] Ceresia_web_app
- [x] .gitignore
- [x] Dockerfile
- [x] LICENSE
- [x] README.md
- [x] compose.sh
- [x] docker-compose.yml
- [x] requirements.txt
- [x] Ceresia_CdC.pdf
- [x] Ceresia_Conception.pdf

## Initialize the project with Docker

---------------

##### Step 1 :
- Clone or download the repository

##### Step 2 :
- Go to the project root directory 
  
##### Step 3 :
- run
```shell
  docker compose up
```

##### Step 4 :
- enter url [localhost](http://127.0.0.1:8000/)
  - If the link does not work, enter directly the url : 
```
    127.0.0.1:8000
```

##### Step 5 :
- Enjoy the alpha version of Ceresia Web App

## Features

---------------

###### Hikes
 - List of all hikes ordered by name
 - Two forms to filter by name or county
###### Species ( Cerescope page )
 - List of all species ordered by name
 - One form to filter by name
 ###### Success ( Work in progress => Static success)
 - See all success
###### History
- add a history with the name of the hike and the date at which you did it or you want to do it  
- Delete a history
- Delete all histories

# Important notes

---------------

### Data import on docker compose
- When your first go on the site, a python script runs to add all the data in the base
- Dockers's behaviour regarding django modules causes an issue when our script runs twice. We found a solution with fixtures, but we didn't have enought time to implement them (we ran into an encoding issue). Because of this, we added a try/except within all functions importing data. This is a temporary fix and prevent our fields from being duplicated. We know this isn't optimal and plan to improve it later.

### Triggers
- Regarding triggers, you'll notice that none are present in our code. We'll explain why : Django already includes a number of pre-built triggers linked to models. Meaning that before any field is about to be added to the database, a trigger checks if the data is valid : does is have the same type as described in the model, and so on.
- You may notice that some fields in our models have an "onCascade=delete" attribute. This means that whenever a primary key is currently used as a foreign key in another table, it can't be deleted to prevent errors. Inversely, it allows the deletion of a field if it contains a foreign key, because it won't affect the rest of the data.
 
## Authors

---------------

##### Yvan Gimard & Thomas Burgard
