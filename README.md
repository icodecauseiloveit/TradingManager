# TradingManager

TradingManager is a FastAPI-based application for managing users in a trading system. It includes features for creating, reading, updating, and deleting users, as well as listing all users.

## Project Structure

```
app/
├── main.py         # Main application (entry point)
├── models/         # SQLModel database models
│   ├── user.py
├── crud/           # Low-level CRUD operations
│   ├── user_crud.py
├── repo/           # High-level database operations
│   ├── user_repo.py
├── schemas/        # Pydantic schemas for validation
│   ├── user_schema.py
├── routes/         # API endpoints
│   ├── user_routes.py
├── database.py     # Database connection setup
├── security.py     # Password hashing & authentication
├── config.py       # Configurations
```

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/TradingManager.git
    cd TradingManager
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following:
    ```env
    DATABASE_URL=sqlite:///./test.db
    ```

5. Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```

## API Endpoints

- **Create User**: `POST /create-user/`
- **Read User**: `GET /users/{user_id}`
- **List Users**: `GET /list-users/`
- **Update User**: `PUT /update-user/{user_id}`
- **Delete User**: `DELETE /users/{user_id}`
- **Delete All Users**: `DELETE /del-all-users/`

## Example Requests

### Create User

```sh
curl -X POST "http://127.0.0.1:8000/create-user/" -H "Content-Type: application/json" -d '{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword"
}'
```

### Read User

```sh
curl -X GET "http://127.0.0.1:8000/users/1"
```

### List Users

```sh
curl -X GET "http://127.0.0.1:8000/list-users/"
```

### Update User

```sh
curl -X PUT "http://127.0.0.1:8000/update-user/1" -H "Content-Type: application/json" -d '{
  "username": "updateduser",
  "email": "updateduser@example.com",
  "password": "newpassword"
}'
```

### Delete User

```sh
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

### Delete All Users

```sh
curl -X DELETE "http://127.0.0.1:8000/del-all-users/"
```

## License

This project is licensed under the Creative Commons (CC) license.