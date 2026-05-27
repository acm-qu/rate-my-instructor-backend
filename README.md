# Rate My Instructor - Backend
For details about the project or contriubution guidelines check the [Main Repository](https://github.com/acm-qu/rate-my-instructor).  
## Application Folder Structure
app  
|- api: The brain of the application  
|- db: manages db sessions, seeding and crud operations  
|- |- repos: crud operation management  
|- models: contains the alembic generated migrations  
|- schemas: contains the pydantic models to tell alembic how the data should look like  
|- tests: contains testing scripts for every feature  
  
## Current Tech stack  
FastAPI, PostgreSQL, Redis, SQLAlchemy, Pydantic, Pytest
  
## How to Contribute
- Clone this repository
- Run `python3.14 -m venv .venv` & Activate the venv using `source .venv/bin/activate` (this is for macOS it might not work for Windows or Linux so google the alternative)
- Install requirements using `pip3 install -r app/requirements/common.txt`