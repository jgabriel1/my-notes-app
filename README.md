# my-notes-app
Simple notes app backend using Python's FastAPI framework.

## Route "/":
* **User login (GET)**: return 200, list of all of their notes;

* **User sign up (POST)**: return 201, user id (random hex code);


## Route "/notes":
* **Create note (POST)**: return 201, id of created note (integer);

* **Edit note (PUT)**: return 204, no body;

* **Delete note (DELETE)**: return 204, no body;