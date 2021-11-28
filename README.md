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

#### Step 2 bis WARNING :
- You must have a postgresql image in docker to run the project.
  - If you don't, you can find it [here](https://hub.docker.com/_/postgres/).

##### Step 3 :
- run
```shell
  docker compose build
```

##### Step 4 :
- run
```shell
  docker compose up
```

##### Step 5 :
- enter url [localhost](http://localhost:8000/)
  - If the link does not work, enter directly the url : 
```
    localhost:8000
```

##### Step 6 :
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
 
## Authors

---------------

##### Yvan Gimard & Thomas Burgard