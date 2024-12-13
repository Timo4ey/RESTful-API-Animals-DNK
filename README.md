# RESTful API for Animal Genetic Tests

## Project Overview
This project is a RESTful API for managing animal genetic test data and calculating aggregated statistics. It is built using Django and Django REST Framework and is containerized with Docker for easy deployment.

## Features

### Core Functionalities
1. **Add Genetic Test Data**: Create records for genetic tests with fields such as animal name, species, test date, milk yield, and health status.
2. **View Records**:
   - Retrieve all genetic test records.
   - Filter records by species.
3. **Calculate Statistics**:
   - Count the number of tests for each species.
   - Calculate the average and maximum milk yield.
   - Determine the percentage of animals with good health status.

### Technical Highlights
- **Technologies**: Django, Django REST Framework, PostgreSQL, Docker.
- **Validation**: Ensures proper data input for each field.
- **Swagger Documentation**: Automatically generated API documentation using `drf-yasg`.
- **Error Handling**: Provides informative messages for invalid requests.

---

## Getting Started

### Prerequisites
1. **Docker**: Ensure Docker and Docker Compose are installed.
2. **Python**: Python 3.11 (for local development).
3. **PostgreSQL**: Required for database operations.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd RESTful_API_Animals_DNK
   ```

2. **Build and Run with Docker**
   ```bash
   docker-compose up --build
   ```
   - The API will be available at `http://localhost:8080`.
   - Swagger UI documentation: `http://localhost:8080/swagger/`.

3. **Run Locally (Without Docker)**
   - Set up a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Run the development server:
     ```bash
     python manage.py runserver
     ```

---

## API Endpoints

### Genetic Tests
1. **GET /tests**: Retrieve all genetic test records (with optional filtering).
2. **POST /tests**: Add a new genetic test.

### Statistics
1. **GET /statistics**: Retrieve aggregated statistics for all species.

---

## Example Requests

### Add a Genetic Test
**Request**
```http
POST /tests
Content-Type: application/json
{
    "animal_name": "Bella",
    "species": "cow",
    "test_date": "2024-12-10",
    "milk_yield": 12.5,
    "health_status": "good"
}
```
**Response**
```json
{
    "message": "Data added successfully",
    "id": 1
}
```

### Retrieve Statistics
**Request**
```http
GET /statistics
```
**Response**
```json
[
    {
        "species": "cow",
        "total_tests": 10,
        "avg_milk_yield": 15.3,
        "max_milk_yield": 20.0,
        "good_health_percentage": 80.0
    }
]
```

---

## Project Structure
```
RESTful_API_Animals_DNK/
├── app_dnk/
│   ├── models.py          # Database models
│   ├── views.py           # API endpoints
│   ├── serializers.py     # Data serialization and validation
│   ├── filters.py         # Queryset filters
├── manage.py              # Django management script
├── Dockerfile             # Docker build file
├── docker-compose.yml     # Docker Compose configuration
├── Makefile               # Development and deployment commands
├── entrypoint.sh          # Entrypoint for the Docker container
└── pyproject.toml         # Project dependencies and build configuration
```

---

## Deployment

### Production Mode
1. **Run in Production**
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. **Environment Variables**
   Configure the following environment variables for production:
   - `DJANGO_SECRET_KEY`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`

---

## Development

### Testing
1. **Run Tests**
   ```bash
   python manage.py test
   ```

2. **Linting**
   ```bash
   flake8 app_dnk
   ```

---

## Known Issues and Improvements
1. **Docker Healthcheck**: Add a health check for PostgreSQL in `docker-compose.yml`.
2. **Tests**: Expand test coverage for edge cases and error scenarios.
3. **Error Messages**: Refine error messages for user clarity.
4. **Security**: Add `DJANGO_SETTINGS_MODULE` and configure allowed hosts dynamically.

---

## Author
- **Timofey Yakovishin**  
  Email: [yakovishintimofey@gmail.com](mailto:yakovishintimofey@gmail.com)

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

