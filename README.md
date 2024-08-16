# rick-and-morty

### Requirements:
1. Endpoint, which return random character from the work of Rick and Morty series
2. Endpoint get `search_string` as an argument and return list of all characters, 
   who contains the search `search_string` in the name.
3. On regular basis, app downloads data from external service to inner DB.
4. Requests of implemented API should work with local DB


### Technologies to use:
1. Public API: https://rickandmortyapi.com/documentation.
2. Use Celery as task scheduler for data synchronization for Rick and Morty API.
3. Python, Django, Orm, PostgresSQL, GIT.
4. All endpoints should be documented via Swagger.
