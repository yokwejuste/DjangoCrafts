![SSO Image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e2cjsymq0l30i4uu1jx0.png)

A Django-based Single Sign-On (SSO) implementation that allows users to authenticate using Google OAuth2. This project demonstrates a basic SSO system for educational purposes.

## What is SSO?

Single Sign-On (SSO) is an authentication scheme that allows users to access multiple applications with a single set of credentials. When a user logs in to one application, they are automatically logged in to all other connected applications without needing to re-enter their credentials. This project shows how to:

1. Authenticate users with Google OAuth2
2. Generate SSO tokens that can be used by other applications
3. Manage user sessions and authentication states

## Project Structure

```
django_sso/
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── django_sso/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── _base.html
│   ├── home.html
│   ├── login.html
│   └── sso_token.html
├── manage.py
├── requirements.txt
└── .env
└── .env.example                       
```

## Key Features

- **Google OAuth2 Authentication**: Users can log in using their Google accounts
- **SSO Token Generation**: Generate unique tokens for cross-application authentication
- **Token Management**: Tokens are stored with expiration times
- **Responsive UI**: Built with Tailwind CSS for a clean, modern interface

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- A Google Developer account for OAuth2 credentials

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django_sso.git
   cd django_sso
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

5. Get Google OAuth2 credentials:
   - Go to the [Google Developer Console](https://console.developers.google.com/)
   - Create a new project
   - Enable the Google+ API
   - Create OAuth2 credentials
   - Add authorized redirect URIs (e.g., `http://localhost:8000/auth/complete/google-oauth2/`)
   - Add your credentials to the `.env` file:
     ```
     GOOGLE_CLIENT_ID='your-client-id'
     GOOGLE_CLIENT_SECRET='your-client-secret'
     ```

6. Apply migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://localhost:8000` in your browser

## Usage

1. Visit the homepage and click "Login with Google"
2. After successful authentication, you'll be redirected to the homepage
3. Click "Generate SSO Token" to create a new token
4. Use the generated token in other applications that support this SSO implementation

## Contributing

We welcome contributions to improve this SSO implementation!

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**:
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed
4. **Test your changes**:
   - Ensure the application works as expected
   - Check for any errors or warnings
5. **Commit your changes**:
   ```bash
   git commit -m "Add a descriptive commit message"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a pull request**:
   - Provide a clear title and description
   - Reference any related issues

### Development Areas

Areas where the project could be improved:

- Add unit and integration tests
- Implement token revocation functionality
- Add support for more OAuth providers
- Enhance token security with encryption
- Create a dashboard for managing tokens

## License

This project is licensed under the Creative Commons Legal Code - see the [LICENSE](../LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python Social Auth](https://python-social-auth.readthedocs.io/) - Authentication backend
- [Tailwind CSS](https://tailwindcss.com/) - For styling the UI
