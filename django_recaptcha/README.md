![header image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y2fsjbyvyigst25jnmdm.png)

A comprehensive demonstration of different CAPTCHA implementations in Django, including Google reCAPTCHA (v2 and v3) and Django Simple CAPTCHA.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo Screenshots](#demo-screenshots)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates how to implement various CAPTCHA systems in a Django application to protect your forms from spam and bot submissions. Multiple CAPTCHA types are included to showcase different approaches to bot protection.

## Features

- **Google reCAPTCHA v2 Checkbox** - Traditional checkbox-based "I'm not a robot" verification
- **Google reCAPTCHA v2 Invisible** - Invisible protection that doesn't require user interaction
- **Google reCAPTCHA v3** - Background scoring system without user interaction
- **Django Simple CAPTCHA** - Self-hosted math challenge CAPTCHA with audio support
- **Responsive Design** - Mobile-friendly interface built with Tailwind CSS
- **Dark Mode Support** - Toggle between light, dark, and system preference themes
- **Comprehensive Error Handling** - User-friendly error messages for CAPTCHA verification failures

## Demo Screenshots

![Demo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hlkze1huy33xuzwzlb06.gif)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/djangocrafts.git
   cd djangocraft/django_recaptcha
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file with your Google reCAPTCHA site keys and secret keys.

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit http://localhost:8000 in your browser**

## Configuration

### Google reCAPTCHA Setup

1. Visit the [Google reCAPTCHA admin console](https://www.google.com/recaptcha/admin)
2. Create separate keys for:
   - reCAPTCHA v2 Checkbox
   - reCAPTCHA v2 Invisible
   - reCAPTCHA v3
3. Add your domain to the allowed domains list
4. Copy the Site keys and Secret keys to your `.env` file:
   ```
   RECAPTCHA_PUBLIC_KEY_V2='your_site_key_v2'
   RECAPTCHA_PRIVATE_KEY_V2='your_secret_key_v2'
   RECAPTCHA_PUBLIC_KEY='your_site_key_v3'  
   RECAPTCHA_PRIVATE_KEY='your_secret_key_v3'
   ```

### Django Simple CAPTCHA Setup

The Django Simple CAPTCHA configuration is already set up in `settings.py`. You may customize the settings:

```python
# Django Simple Captcha settings
CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"
CAPTCHA_LENGTH = 6
CAPTCHA_TIMEOUT = 5
# Enable audio captcha
CAPTCHA_AUDIO_URLS = True
CAPTCHA_NOISE_FUNCTIONS = ("captcha.helpers.noise_dots",)
CAPTCHA_LETTER_ROTATION = (-15, 15)
```

## Usage

The project includes four demonstration pages:

1. **reCAPTCHA v2 Checkbox** - `/contact/`
   - Traditional "I'm not a robot" checkbox
   
2. **reCAPTCHA v2 Invisible** - `/invisible/`
   - Invisible protection with automatic verification

3. **reCAPTCHA v3** - `/v3/`
   - Background scoring system that runs automatically

4. **Django Simple CAPTCHA** - `/django-captcha/`
   - Self-hosted math challenge with audio support

## Project Structure

```
```
django_recaptcha/
├── accounts/
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── contact.html
│   ├── django_captcha.html
│   ├── home.html
│   ├── invisible.html
│   └── v3.html
├── verify/
│   ├── settings.py
│   └── urls.py
├── .env
├── .env.example
├── manage.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- **Django** - Web framework
- **django-recaptcha** - Google reCAPTCHA integration
- **django-simple-captcha** - Self-hosted CAPTCHA solution
- **Tailwind CSS** - Utility-first CSS framework
- **python-dotenv** - Environment variable management

## 👥 Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Make your changes and commit them**:
   ```bash
   git commit -am 'Add some feature'
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature/my-new-feature
   ```
5. **Submit a pull request**

Please make sure your code follows the existing style and includes appropriate tests.

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use 4 spaces for indentation (not tabs)
- Include docstrings for functions and classes

## 📄 License

This project is licensed under the Creative Common License - see the [LICENSE](../LICENSE) file for details.

---

Built with ❤️ by [Steve Yonkeu (@yokwejuste)](https://me.yokwejuste.me)