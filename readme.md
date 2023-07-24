
# Python Secret Manager

Python Secret Manager is a super simple command-line tool that allows you to manage secrets and environment variables. It provides a user-friendly menu to list existing keys, get the value of a key, set a new key, and quit the program.

## Prerequisites

Before running the Python Secret Manager, make sure you have the following installed:

- Python 3.x
- MySQL (if using MySQL as the backend for storing keys)

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/python-secret-manager.git
```

2. Change into the project directory:

```
cd python-secret-manager
```

3. Install the required dependencies:

```
pip install mysql-connector-python
```

4. Set up the MySQL database:

   - Create a new database named `providers`.
   - Set up a user with appropriate privileges on the `providers` database and note down the credentials.
   - Replace the database credentials in the `SecretManager` class in `secret_man.py`.

## Usage

To run the Python Secret Manager, execute the `main.py` script:

```
python main.py
```

### Menu Options

1. **List Keys (`ls`)**: Display a list of all the keys set so far.

2. **Get a Key (`get`)**: Get the value of a specific key.

3. **Set a Key (`set`)**: Set a new environment variable.

4. **Quit (`q`)**: Exit the program.

When choosing the "Set a Key" option, the script will prompt you to enter the name and value for the new environment variable.

## Notes

- The script uses a MySQL database to store the keys. You can modify the `SecretManager` class in `secret_man.py` to use a different database or storage mechanism if needed.
- Avoid setting sensitive data like database credentials directly in the script. Instead, use environment variables or a configuration file for better security.

## Contributing

Contributions to the Python Secret Manager are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
