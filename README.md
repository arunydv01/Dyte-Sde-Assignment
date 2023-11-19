<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<div align="center">

<h3 align="center">Log Searcher</h3>

  <p align="center">
	Dyte SDE Assessment
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Log Searcher 10K][product-screenshot]](https://github.com/dyte-submissions/november-2023-hiring-Enhancifire)

Log Ingester and Query Tool built using Django for Dyte SDE Assessment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* Django
* PostgreSQL
* SQLite3
* Docker

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project can be run using a local SQLite database, or using Docker. Both methods are described below.

### Prerequisites

- Python 3.10 or higher
- Docker (optional)

### Installation

#### Without Docker


1. Create virtual environment
   ```sh
   python -m venv .env
   ```
2. Activate the environment
   ```sh
   source .env/bin/activate.fish # for fish shell
   ```

3. Install requirements
   ```sh
    pip install -r requirements.txt
   ```

4. Run migrations
   ```sh
    python manage.py migrate
    ```

5. Run the server
   ```sh
    python manage.py runserver 3000
   ```

#### With Docker


1. Switch branch to docker
    ```sh
    git checkout docker
    ```
2. Start DB and build docker image
    ```sh
    docker compose up db -d
    ```

3. Build and Start the server
    ```sh
    docker compose up server --build
    ```
4. Run migrations
    ```sh
    docker compose exec server python manage.py migrate
    ```
5. Access the server at `localhost:3000`


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Access the server at `localhost:3000`

Endpoints:
- '/': Home page
  Query interface is accessible here

- '/logs/': Ingest point for logs
  POST request to add individual logs to the database

- '/logsearch/': Search endpoint for logs
  Query interface accesses this endpoint to search for logs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## System Design

![DB Diagram][db-diagram]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features Implemented

**Ingestor:**

- [X] Develop a mechanism to ingest logs in the provided format.
- [X] Ensure scalability to handle high volumes of logs efficiently.
- [X] Mitigate potential bottlenecks such as I/O operations, database write speeds, etc.
- [X] Make sure that the logs are ingested via an HTTP server, which runs on port `3000` by default.

**Query Interface:**

- [X] Offer a user interface (Web UI or CLI) for full-text search across logs.
- [X] Include filters based on:
    - level
    - message
    - resourceId
    - timestamp
    - traceId
    - spanId
    - commit
    - metadata.parentResourceId
- [X] Aim for efficient and quick search results.

**Advanced Features:**

- [X] Allow combining multiple filters.
- [X] Provide real-time log ingestion and searching capabilities.
- [X] Distributed systems or cloud-based solutions can ensure robust scalability.
- [ ] Implement role-based access to the query interface.
- [ ] Implement search within specific date ranges.
- [ ] Utilize regular expressions for search.


## Identified Issues

- Manual migration for Postgres required in docker usecase.
- Possible bottleneck of single threaded django instance.
- Static metadata field parameter. Adding additional data to metadata requires conversion from foreign key to BSON.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

