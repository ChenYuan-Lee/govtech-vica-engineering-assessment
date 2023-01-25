# GovTech Vica Engineering Assessment
Attempted by: Lee Chen Yuan

## Prerequisites
* This project uses MongoDB Community Edition on macOS (installation instructions can be found [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)).
* This project is built using Python 3.10.
* Install the project dependencies (you may want to perform this inside a virtual environment): `pip install -r requirements.txt`.

## Getting Started
1. [Run MongoDB Community Edition](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/#run-mongodb-community-edition)
   * For instance, to run MongoDB as a macOS service, run: `brew services start mongodb-community@6.0`
2. If this is your first time running this project, run the `populate_db.py` script to create 2 default admin users in the database.
3. Start the FastAPI server

## User Manual


* To shut down the service:
  * Terminate the FastAPI service
  * [Stop MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/#run-mongodb-community-edition)
    * For instance, to stop MongoDB from running as a macOS service, run: `brew services stop mongodb-community@6.0`