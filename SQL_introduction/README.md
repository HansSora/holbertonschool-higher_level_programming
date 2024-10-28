# SQL Introduction

Welcome to the SQL Introduction project! This repository contains a series of SQL scripts designed to demonstrate fundamental database operations.

## Directory Structure

- [0-list_databases.sql](0-list_databases.sql)  
  Show all current databases.

- [1-create_database_if_missing.sql](1-create_database_if_missing.sql)  
  Create a database if it does not already exist.

- [2-remove_database.sql](2-remove_database.sql)  
  Remove a database if it exists.

- [3-list_tables.sql](3-list_tables.sql)  
  Show tables in the current database.

- [4-first_table.sql](4-first_table.sql)  
  Create a table named `first_table`.

- [5-full_table.sql](5-full_table.sql)  
  Show the structure of the `first_table`.

- [6-list_values.sql](6-list_values.sql)  
  List all rows in the `first_table`.

- [7-insert_value.sql](7-insert_value.sql)  
  Insert a new row into the `first_table`.

- [8-count_89.sql](8-count_89.sql)  
  Count the number of records with `id = 89` in the `first_table`.

- [9-full_creation.sql](9-full_creation.sql)  
  Create a `second_table` and insert initial data.

- [10-top_score.sql](10-top_score.sql)  
  List all records from `second_table` ordered by score.

- [11-best_score.sql](11-best_score.sql)  
  Show records with scores greater than or equal to 10.

- [12-no_cheating.sql](12-no_cheating.sql)  
  Update Bob's score to 10 in `second_table`.

- [13-change_class.sql](13-change_class.sql)  
  Remove records with a score of 5 or less from `second_table`.

- [14-average.sql](14-average.sql)  
  Compute the average score of all records in `second_table`.

- [15-groups.sql](15-groups.sql)  
  List the number of records with the same score in `second_table`.

- [16-no_link.sql](16-no_link.sql)  
  List all records in `second_table` where the name is not null.

## Usage

To execute any of the SQL scripts, simply run them against your MySQL database using your preferred SQL client.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to see.