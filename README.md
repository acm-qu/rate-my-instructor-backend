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

## TODOs
- Replace `sqlalchemy.url` value with the deployed db url