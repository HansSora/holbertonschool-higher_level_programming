# RESTful API Project

Welcome to the RESTful API Project! This repository contains Python scripts that implement various aspects of RESTful APIs using different frameworks.

## File Descriptions

### [task_02_requests.py](task_02_requests.py)
This script demonstrates how to fetch and save posts from a placeholder API using the `requests` library.

- **Functions**:
  - `fetch_and_print_posts()`: Fetches and prints posts from the API.
  - `fetch_and_save_posts()`: Fetches posts and saves selected data to a CSV file.

### [task_03_http_server.py](task_03_http_server.py)
A simple HTTP server implemented using Python's built-in `http.server` module.

- **Endpoints**:
  - `/`: Returns a welcome message.
  - `/info`: Provides API version and description in JSON format.
  - `/data`: Returns sample user data in JSON format.
  - `/status`: Returns a status message.
  - Any other path returns a 404 error.

### [task_04_flask.py](task_04_flask.py)
This script sets up a basic Flask application with a few endpoints.

- **Endpoints**:
  - `/`: Welcome message.
  - `/data`: Returns a list of usernames.
  - `/status`: Returns an "OK" message.
  - `/users/<username>`: Returns user information or an error if not found.
  - `/add_user`: Allows adding a new user via POST requests.

### [task_05_basic_security.py](task_05_basic_security.py)
Enhances the Flask API with basic authentication and JWT (JSON Web Token) support.

- **Endpoints**:
  - `/basic-protected`: Requires basic auth for access.
  - `/login`: Allows users to log in and receive a JWT.
  - `/jwt-protected`: Requires a valid JWT for access.
  - `/admin-only`: Restricted access for admin users.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to see.