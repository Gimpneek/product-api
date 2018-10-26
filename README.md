# Installing the project
Run `make install` which will create a new virtualenv and install the requirements.

# Running the project locally
Running `make run` will run the server on port 5000

If you need to reset the data on the server you can run `make reset_db` which will delete the database and repopulate the data. You do not need to stop the server to do this.

# Testing the project
Run `make test` which will lint and run the unit_tests.