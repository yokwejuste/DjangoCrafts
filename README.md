![DjangoCrafts - 2FA With google authenticator](https://github.com/user-attachments/assets/a2d49ed9-279a-41b3-8112-544564efa4fa)

This repository contains various Django projects and tutorials to help you learn and implement different Django features and functionalities.

## Table of Contents

- [Projects](#projects)
  - [Django 2FA](#django-2fa)
  - [Django SSO](#django-sso)
  - [Django 2FA with Google Authenticator](#django-2fa-with-google-authenticator)
  - [Django Passkeys](#django-passkeys)
  - [Django ReCaptcha](#django-recaptcha)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Security](#security)
- [Support](#support)
- [License](#license)

## Projects

### Django 2FA

A Django project that demonstrates how to implement Two-Factor Authentication in your Django applications. This enhances security by requiring users to provide two forms of identification before gaining access.

### Django SSO

A [Django-based Single Sign-On (SSO) implementation](./django_sso/) that allows users to authenticate using Google OAuth2. This project demonstrates how to:

1. Authenticate users with Google OAuth2
2. Generate SSO tokens that can be used by other applications
3. Manage user sessions and authentication states

The implementation provides a practical example of SSO for educational purposes, making it easier to understand the concepts behind single sign-on authentication systems.

### Django 2FA with Google Authenticator

A [comprehensive Django application](./django2fa/) demonstrating two-factor authentication (2FA) implementation using `django-two-factor-auth`. This project showcases a secure Django implementation with multiple two-factor authentication methods including:

- TOTP (Time-based One-Time Password) for Google Authenticator
- Email verification codes
- Phone verification (SMS)

The application provides a complete authentication flow with a custom user model for enhanced security and Bootstrap UI for responsive design.

### Django Passkeys

A [Django-based web application](https://github.com/yokwejuste/django-passkeys) that implements both traditional authentication (username/password) and passkey authentication using the WebAuthn API. Passkey authentication allows users to securely log in without passwords, using biometric or hardware-based authentication methods.

Key features include:
- Traditional username/password registration and login
- Passkey-based authentication (passwordless)
- Implementation of the WebAuthn API for secure authentication
- Django's CSRF protection and HTTPS support for secure contexts

### Django ReCaptcha

A [comprehensive demonstration](./django_recaptcha/) of different CAPTCHA implementations in Django, including Google reCAPTCHA (v2 and v3) and Django Simple CAPTCHA. This project helps protect your forms from spam and bot submissions by showcasing multiple CAPTCHA types:

- Google reCAPTCHA v2 Checkbox - Traditional "I'm not a robot" verification
- Google reCAPTCHA v2 Invisible - Protection without user interaction
- Google reCAPTCHA v3 - Background scoring system
- Django Simple CAPTCHA - Self-hosted math challenge with audio support

The implementation uses Django, django-recaptcha, django-simple-captcha, and Tailwind CSS for styling.

## Getting Started

### Cloning a Specific Folder

If you want to clone only a specific project folder instead of the entire repository, you can use sparse checkout with git. Follow these steps:

1. Create a new directory and initialize a git repository:
   ```bash
   mkdir my-project
   cd my-project
   git init
   ```

2. Add the remote repository:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/Django-Crafts.git
   ```

3. Enable sparse checkout:
   ```bash
   git config core.sparseCheckout true
   ```

4. Specify the folder you want to clone (e.g., django2fa):
   ```bash
   echo "django2fa/" >> .git/info/sparse-checkout
   ```

5. Pull the content:
   ```bash
   git pull origin main
   ```

Now you have only the django2fa folder in your local repository.

## Contributing

Please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this repository.

## Security

For security concerns, please see our [SECURITY.md](SECURITY.md) file.

## Support

Need help? Check out our [SUPPORT.md](SUPPORT.md) document for assistance options.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
