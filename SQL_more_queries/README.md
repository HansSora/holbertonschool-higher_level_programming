# SQL More Queries

Welcome to the SQL More Queries project! This repository contains a series of SQL scripts designed to demonstrate advanced database operations, including user management, table creation, and complex queries.

## Directory Structure

- [0-privileges.sql](0-privileges.sql)  
  List privileges for specific users.

- [1-create_user.sql](1-create_user.sql)  
  Create a MySQL user `user_0d_1` with all privileges.

- [2-create_read_user.sql](2-create_read_user.sql)  
  Create the database `hbtn_0d_2` and user `user_0d_2` with select privileges.

- [3-force_name.sql](3-force_name.sql)  
  Create a table `force_name` with a non-nullable name.

- [4-never_empty.sql](4-never_empty.sql)  
  Create a table `id_not_null` with a default value for `id`.

- [5-unique_id.sql](5-unique_id.sql)  
  Create a table `unique_id` with a unique constraint on `id`.

- [6-states.sql](6-states.sql)  
  Create the database `hbtn_0d_usa` and a `states` table.

- [7-cities.sql](7-cities.sql)  
  Create a `cities` table that references the `states` table.

- [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql)  
  List all cities in California from the `hbtn_0d_usa` database.

- [9-cities_by_state_join.sql](9-cities_by_state_join.sql)  
  List all cities along with their corresponding state names.

- [10-genre_id_by_show.sql](10-genre_id_by_show.sql)  
  Show genre IDs associated with TV shows.

- [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql)  
  List all TV shows and their genre IDs from the database.

- [12-no_genre.sql](12-no_genre.sql)  
  List all TV shows without any linked genre.

- [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql)  
  List all genres and the number of shows linked to each.

- [14-my_genres.sql](14-my_genres.sql)  
  List all genres of the show *Dexter*.

- [15-comedy_only.sql](15-comedy_only.sql)  
  List all Comedy shows in the database.

- [16-shows_by_genre.sql](16-shows_by_genre.sql)  
  List all shows and their associated genres.

## Usage

To execute any of the SQL scripts, simply run them against your MySQL database using your preferred SQL client.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to see.