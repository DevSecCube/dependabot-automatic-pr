# Dependabot Automatic PR

A Flask web application with automatic dependency updates using GitHub Dependabot. This project demonstrates how to set up automated dependency management for Python applications.

## 🚀 Features

- **Flask Web Application**: RESTful API with user management
- **Automatic Dependency Updates**: Daily dependency scanning and PR creation via Dependabot
- **Database Integration**: SQLAlchemy with Flask-Migrate for database management
- **Testing**: Comprehensive test suite with pytest
- **Code Quality**: Black formatting, flake8 linting, and safety checks

## 📋 Prerequisites

- Python 3.11+
- pip
- Git

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DevSecCube/dependabot-automatic-pr.git
   cd dependabot-automatic-pr
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies**

   ```bash
   pip install -r requirements-dev.txt
   ```

## 🚀 Usage

### Running the Application

1. **Set environment variables (optional)**

   ```bash
   # Default uses SQLite database
   export DATABASE_URL="sqlite:///app.db"
   ```

2. **Initialize the database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

3. **Run the application**

   ```bash
   flask run
   ```

The application will be available at `http://localhost:5000`

### API Endpoints

- `GET /health` - Health check endpoint
- `GET /users` - Retrieve all users
- `POST /users` - Create a new user (requires email in JSON body)

### Example API Usage

```bash
# Health check
curl http://localhost:5000/health

# Create a user
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com"}'

# Get all users
curl http://localhost:5000/users
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run with verbose output
pytest -v
```

## 🔧 Development

### Code Quality Tools

- **Black**: Code formatting

  ```bash
  black app/ tests/
  ```

- **Flake8**: Linting

  ```bash
  flake8 app/ tests/
  ```

- **Safety**: Security vulnerability scanning

  ```bash
  safety check
  ```

### Database Migrations

```bash
# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback migrations
flask db downgrade
```

## 🤖 Dependabot Configuration

This project includes automatic dependency updates via GitHub Dependabot. The configuration (`.github/dependabot.yml`) is set to:

- **Package Ecosystem**: pip (Python)
- **Schedule**: Daily updates
- **Scope**: Direct and indirect dependencies
- **PR Limit**: Maximum 10 open pull requests

Dependabot will automatically:

1. Check for outdated dependencies daily
2. Create pull requests with updates
3. Include changelog information
4. Run tests to ensure compatibility

## 📁 Project Structure

```bash
dependabot-automatic-pr/
├── app/                    # Application package
│   ├── __init__.py        # Flask app factory
│   └── routes.py          # API endpoints
├── .github/               # GitHub configuration
│   └── workflows/         # GitHub Actions
│   └── dependabot.yml     # Dependabot configuration
├── tests/                 # Test suite
│   └── test_app.py        # Application tests
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── README.md              # This file
```

## 🔒 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///app.db` | Database connection string |
| `FLASK_ENV` | `development` | Flask environment |

## 📝 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Dependencies

### Production Dependencies

- Flask 2.3.3 - Web framework
- Flask-SQLAlchemy 3.0.5 - Database ORM
- Flask-Migrate 4.0.5 - Database migrations
- SQLAlchemy 2.0.23 - Database toolkit
- Werkzeug 2.3.7 - WSGI utilities

### Development Dependencies

- pytest 7.4.3 - Testing framework
- pytest-cov 4.1.0 - Coverage reporting
- black 23.11.0 - Code formatter
- flake8 6.1.0 - Linter
- safety 3.6.0 - Security scanner

## 🚨 Troubleshooting

### Common Issues

1. **Database connection errors**
   - Ensure the database URL is correct
   - Check if the database file exists and is writable

2. **Import errors**
   - Verify virtual environment is activated
   - Check if all dependencies are installed

3. **Migration errors**
   - Delete the `migrations/` folder and reinitialize
   - Ensure database schema is clean

### Getting Help

If you encounter issues:

1. Check the existing issues in the repository
2. Create a new issue with detailed error information
3. Include your environment details and steps to reproduce

## 🔮 Future Enhancements

- [ ] Add authentication and authorization
- [ ] Implement rate limiting
- [ ] Add more comprehensive API endpoints
- [ ] Include Docker support
- [ ] Add CI/CD pipeline
- [ ] Implement monitoring and logging
