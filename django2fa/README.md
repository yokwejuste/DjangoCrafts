# Django 2FA Implementation

A comprehensive Django application demonstrating two-factor authentication (2FA) implementation using `django-two-factor-auth`.

## Overview

This project showcases a secure Django implementation with two-factor authentication methods including:
- TOTP (Time-based One-Time Password)
- Email verification codes
- Phone verification (SMS)

The application provides a complete authentication flow with a custom user model for enhanced security.

## Features

- Custom user model (`STUser`) with verification status
- Multiple 2FA methods:
  - TOTP authentication
  - Email verification
  - Phone verification
- Admin interface integration with 2FA
- Bootstrap UI for responsive design
- User session management
- Logout functionality

## Prerequisites

- Python 3.9+
- pip
- Django 5.1+
- A virtual environment tool (virtualenv, pipenv, or conda)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django2fa.git
   cd django2fa
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit http://localhost:8000 in your browser to see the application.

## Configuration

### Environment Variables

Configure the following variables in your `.env` file:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'True' for development, 'False' for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Additional Settings

For production, you may want to configure:
- Email settings for 2FA via email
- SMS gateway for phone verification
- HTTPS for secure communication

## Usage

1. Register a new user account
2. Set up 2FA during the authentication process
3. Login with your credentials plus 2FA verification

Or use the admin interface at `/admin` with your superuser credentials.

## Project Structure

```
django2fa/
├── accounts/               # Custom user app
│   ├── models.py           # STUser model
│   ├── views.py            # Authentication views
│   └── urls.py             # Account-related URLs
├── django2fa/              # Main project folder
│   ├── settings.py         # Project settings
│   └── urls.py             # Main URL configuration
├── templates/              # HTML templates
│   └── two_factor/         # 2FA templates
├── .env                    # Environment variables
├── manage.py               # Django command line utility
└── requirements.txt        # Project dependencies
```

## How 2FA Works in This Project

1. **Authentication**: User logs in with username and password
2. **Verification**: User provides a second factor:
   - TOTP code from an authenticator app
   - Code sent via email
   - Code sent via SMS
3. **Authorization**: Upon successful verification, user gains access to protected resources

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows PEP 8 guidelines. To check your code style:

```bash
pip install flake8
flake8
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Open a Pull Request

Please ensure your code follows the project's coding style and includes appropriate tests.

## Troubleshooting

- **Migration issues**: Delete the `db.sqlite3` file and run migrations again
- **TOTP not working**: Check your server time is synchronized correctly
- **Email verification issues**: Check your email settings in Django

## Security Considerations

- Keep your `SECRET_KEY` confidential
- In production, always use HTTPS
- Regularly update dependencies to address security vulnerabilities

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [django-two-factor-auth](https://github.com/jazzband/django-two-factor-auth) library
- Django documentation on authentication

## Contact

For questions or support, please open an issue in the GitHub repository.