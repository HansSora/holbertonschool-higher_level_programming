# Python Object-Relational Mapping (ORM) Project

This project demonstrates various techniques for interacting with a MySQL database using both raw SQL queries and SQLAlchemy ORM. The examples include basic database queries, using parameterized queries, and working with SQLAlchemy models.

## Files

- [0-select_states.py](0-select_states.py):  
  A script that lists all states from the database `hbtn_0e_0_usa`, ordered by their `id`.
  
- [1-filter_states.py](1-filter_states.py):  
  A script that lists all states from the database `hbtn_0e_0_usa` where the state name starts with "N", ordered by `id`.

- [2-my_filter_states.py](2-my_filter_states.py):  
  A script that lists all states from the database `hbtn_0e_0_usa` based on a user-provided state name filter, ordered by `id`.

- [3-my_safe_filter_states.py](3-my_safe_filter_states.py):  
  A safer version of `2-my_filter_states.py` that uses parameterized queries to prevent SQL injection.

- [4-cities_by_state.py](4-cities_by_state.py):  
  A script that lists all cities along with their associated states, ordered by city `id`.

- [5-filter_cities.py](5-filter_cities.py):  
  A script that lists all cities in a specific state, ordered by city `id`.

- [model_state.py](model_state.py):  
  A script defining a SQLAlchemy `State` model, which maps to the `states` table in a MySQL database.

- [7-model_state_fetch_all.py](7-model_state_fetch_all.py):  
  A script that fetches all records from the `states` table using SQLAlchemy and prints them ordered by `id`.

- [8-model_state_fetch_first.py](8-model_state_fetch_first.py):  
  A script that fetches the first state from the `states` table using SQLAlchemy and prints its `id` and `name`.

- [9-model_state_filter_a.py](9-model_state_filter_a.py):  
  A script that fetches all states whose name contains the letter "a", ordered by `id`.

- [10-model_state_my_get.py](10-model_state_my_get.py):  
  A script that fetches the `id` of a state based on a user-provided state name. Prints "Not found" if no matching state is found.

- [11-model_state_insert.py](11-model_state_insert.py):  
  A script that inserts a new state ("Louisiana") into the `states` table and prints its `id`.

- [12-model_state_update_id_2.py](12-model_state_update_id_2.py):  
  A script that updates the name of the state with `id` 2 to "New Mexico".

- [13-model_state_delete_a.py](13-model_state_delete_a.py):  
  A script that deletes all states whose name contains the letter "a".

- [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py):  
  A script that lists all cities in the `states` table, along with their state names, ordered by city `id`.

  ## Contributing

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.