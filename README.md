Vertigo Games – Data Engineer Case  
Part 1 – Backend API

In Part 1, I built and deployed a backend API for creating, deleting and viewing clans.

-----------------------------------------
 What I Did

- Created a REST API using FastAPI
- Designed a "clans" table in PostgreSQL
- Used SQLAlchemy as the ORM
- Managed schema changes with Alembic
- Containerized the application using Docker
- Deployed the API to Google Cloud Run
- Used Cloud SQL (PostgreSQL) as the production database
  
-----------------------------------------

Result

The API is publicly accessible, connected to Cloud SQL, and supports basic clan management operations.

Part 2 - Analytics & Visualization

In Part 2, I built a  analytics pipeline on top of raw  data.

What I Did
- Created a BigQuery dataset
- Uploaded and appended 17 CSV files into a single table called "user_events"
- Initialized dbt with the BigQuery adapter
- Built a dbt model to generate daily aggregated metrics
- Verified transformed tables directly in BigQuery
- Built a basic dashboard using Looker Studio

Result
- Raw event data was successfully transformed into daily metrics and visualized in a simple dashboard.

 -----------------------------------------
 
 
 Issues I Faced

- Uvicorn / FastAPI startup errors  
  - Fixed module paths and entrypoint configuration

- Database connection errors  
  - Switched between local TCP and Cloud SQL Unix socket depending on environment

- Migrations not applied  
  - Ensured Alembic ran against the correct database URL
 
- BigQuery CSV load errors
  -switched to manual upload and append
  
- Confusion with multiple CSV files →
  -used one table instead of many

- dbt connection issues
  -fixed dataset name, region (EU), and OAuth setup


