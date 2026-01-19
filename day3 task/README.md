# FastAPI MongoDB OAuth2 Authentication API

A modern, asynchronous REST API built with **FastAPI** and **MongoDB** that provides user authentication using OAuth2 with JWT tokens. This project demonstrates best practices for building scalable APIs with secure authentication mechanisms.

## 🌟 Features

- **FastAPI Framework**: Modern Python web framework for building APIs with automatic interactive documentation
- **Asynchronous Operations**: Non-blocking I/O using Motor (async MongoDB driver)
- **MongoDB Integration**: Cloud-based MongoDB with Atlas for data persistence
- **OAuth2 Authentication**: JWT-based token authentication for secure endpoints
- **Password Security**: Bcrypt hashing for secure password storage
- **Data Validation**: Pydantic models for request/response validation
- **Email Validation**: EmailStr validation for user email fields
- **User Registration & Login**: Complete authentication flow
- **Protected Endpoints**: Role-based access to user-specific endpoints

## 📁 Project Structure

```
day3 task/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── deps.py            # Dependency injection (JWT verification)
│   │   └── routes/
│   │       ├── auth.py        # Authentication endpoints (login)
│   │       └── user.py        # User endpoints (register, get profile)
│   ├── core/
│   │   ├── config.py          # Configuration and environment variables
│   │   ├── database.py        # MongoDB connection setup
│   │   └── security.py        # Password hashing and JWT token creation
│   ├── crud/
│   │   ├── __init__.py
│   │   └── user.py            # Database operations (create, authenticate)
│   ├── models/
│   │   └── user.py            # Data transformation helpers
│   └── schemas/
│       ├── user.py            # User request/response schemas
│       └── token.py           # Token response schema
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MongoDB Atlas account (free tier available)
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "day3 task"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the project root with the following variables**
   ```env
   MONGO_USERNAME=your_mongodb_username
   MONGO_PASSWORD=your_mongodb_password
   MONGO_CLUSTER=your_cluster.mongodb.net
   MONGO_DB_NAME=your_database_name
   
   JWT_SECRET=your_super_secret_key_change_this_in_production
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

### Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- **Interactive API Docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API Docs (ReDoc)**: `http://localhost:8000/redoc`

## 📚 API Endpoints

### Authentication Routes

#### **User Login**
```http
POST /auth/token
```
**Request Body (Form Data):**
```json
{
  "username": "user@example.com",
  "password": "yourpassword"
}
```
**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```
**Status Codes:**
- `200 OK` - Login successful
- `401 Unauthorized` - Invalid credentials

---

### User Routes

#### **User Registration**
```http
POST /users/
```
**Request Body (JSON):**
```json
{
  "email": "newuser@example.com",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "email": "newuser@example.com"
}
```
**Status Codes:**
- `200 OK` - User created successfully
- `400 Bad Request` - Email already exists or invalid email format

---

#### **Get Current User Profile**
```http
GET /users/me
```
**Headers:**
```
Authorization: Bearer <access_token>
```
**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "email": "user@example.com"
}
```
**Status Codes:**
- `200 OK` - User data retrieved
- `401 Unauthorized` - Invalid or missing token

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | Latest | Web framework for building APIs |
| `uvicorn` | Latest | ASGI server to run FastAPI |
| `motor` | 3.7.1 | Async MongoDB driver |
| `python-jose[cryptography]` | Latest | JWT token encoding/decoding |
| `passlib[bcrypt]` | Latest | Password hashing |
| `python-dotenv` | Latest | Environment variable management |
| `pydantic[email]` | Latest | Data validation with email support |

## 🔐 Security Features

### Password Hashing
Passwords are hashed using **bcrypt** before storage. When a user logs in, the provided password is compared against the stored hash without ever storing plain text passwords.

### JWT Authentication
- Users receive a **JSON Web Token (JWT)** upon successful login
- Tokens expire after 30 minutes (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`)
- Protected endpoints verify the token and extract the user ID
- Tokens are signed with `HS256` algorithm

### Email Validation
Email addresses are validated using Pydantic's `EmailStr` to ensure valid email format.

## 📝 Example Usage

### 1. Register a New User
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "secure123"}'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john@example.com&password=secure123"
```

### 3. Access Protected Endpoint
```bash
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer <your_token_here>"
```

## 🗄️ Database Schema

### Users Collection
```json
{
  "_id": ObjectId,
  "email": "user@example.com",
  "hashed_password": "$2b$12$abcd1234..."
}
```

## 🛠️ Core Components

### `app/core/config.py`
Manages all configuration variables loaded from environment file. Handles MongoDB connection string construction with URL-encoded credentials.

### `app/core/database.py`
Initializes the Motor async MongoDB client and provides the database instance for dependency injection.

### `app/core/security.py`
Contains security utilities:
- `hash_password()` - Bcrypt password hashing
- `verify_password()` - Password verification
- `create_access_token()` - JWT token creation

### `app/crud/user.py`
Database operations (CRUD):
- `create_user()` - Insert new user with hashed password
- `authenticate_user()` - Verify credentials and return user

### `app/api/deps.py`
Dependency injection for protected routes, including JWT token verification.

### `app/api/routes/auth.py`
Authentication endpoints for user login and token generation.

### `app/api/routes/user.py`
User management endpoints for registration and profile retrieval.

## 🚦 Common Issues & Solutions

### Motor Library Import Error
**Problem**: `Import "motor" could not be resolved`
**Solution**: Ensure virtual environment is activated and dependencies installed
```bash
pip install -r requirements.txt
```

### MongoDB Connection Failed
**Problem**: Connection timeout or authentication error
**Solution**: 
- Verify credentials in `.env` file
- Ensure IP address is whitelisted in MongoDB Atlas
- Check cluster name and database name

### Invalid Email Format
**Problem**: `422 Unprocessable Entity` on user registration
**Solution**: Provide a valid email address format (e.g., `user@domain.com`)

### Expired Token
**Problem**: `401 Unauthorized` on protected endpoints
**Solution**: Get a new token by logging in again with `/auth/token`

## 📈 Future Enhancements

- [ ] Email verification on user signup
- [ ] Password reset functionality
- [ ] User roles and permissions
- [ ] Rate limiting
- [ ] API logging and monitoring
- [ ] User profile update endpoint
- [ ] Account deletion endpoint
- [ ] Refresh token implementation

## 📝 License

This project is provided as-is for educational purposes.

## 👨‍💻 Author

Created as part of Day 3 Task - FastAPI and MongoDB Integration

---

**Happy Coding! 🚀**
