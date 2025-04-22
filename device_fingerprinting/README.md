![Device Fingerprinting](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l9dp8ji6vp4ovhhlzlfo.png)

A Django application that demonstrates device fingerprinting implementation for enhanced security and user tracking. This project shows how to identify and track unique devices accessing your web application without relying on cookies.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

Device fingerprinting is a technique used to identify and track devices based on their unique characteristics, such as browser settings, installed plugins, screen resolution, and system fonts. This project demonstrates how to implement device fingerprinting in a Django application for security and analytics purposes.

## Features

- Browser-based device fingerprinting
- Secure storage of device signatures
- User session tracking
- Device change detection
- Analytics dashboard for device statistics
- Privacy-focused implementation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Django-Crafts.git
cd Django-Crafts/device_fingerprinting
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

4. Apply migrations:
```bash
python manage.py migrate
```

## Configuration

1. Update `settings.py` with your specific settings
2. Configure the fingerprinting parameters in `middleware.py`
3. Customize the tracking behavior in `views.py`

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application at `http://localhost:8000`
3. Monitor device fingerprints in the admin interface

## Project Structure

```plaintext
device_fingerprinting/
├── acc_users/              # User management app
│   ├── models.py          # Device fingerprint models
│   ├── views.py           # Fingerprint processing views
│   └── urls.py           # URL configurations
├── fingerprint/           # Main project folder
│   ├── middleware.py     # Fingerprinting middleware
│   ├── settings.py       # Project settings
│   └── urls.py          # Main URL configuration
├── templates/            # HTML templates
│   ├── _base.html       # Base template
│   └── index.html       # Main page template
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Technologies Used

- **Django** - Web framework
- **JavaScript** - Client-side fingerprinting
- **SQLite** - Database
- **Python** - Backend logic

## Contributing

Please read our [Contributing Guidelines](../CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the Creative Commons License - see the [LICENSE](../LICENSE) file for details.

---

Built with ❤️ by [Steve Yonkeu (@yokwejuste)](https://me.yokwejuste.me)
