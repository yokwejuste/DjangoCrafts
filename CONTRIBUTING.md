# Contributing to Django Crafts

Thank you for your interest in contributing to Django Crafts! This document provides guidelines and instructions for contributing to this repository.

## How to Contribute

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Clone the Repository**: Clone your forked repository to your local machine.

## Cloning a Specific Folder

If you only want to work on a specific project (e.g., django2fa), you can use git's sparse checkout feature:

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

4. Specify the folder you want to clone:
   ```bash
   echo "django2fa/" >> .git/info/sparse-checkout
   ```

5. Pull the content:
   ```bash
   git pull origin main
   ```

Now you have only the django2fa folder in your local repository, which makes it easier to focus on a specific project.

3. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**: Implement your changes, following our coding standards.

5. **Test Your Changes**: Ensure your changes work as expected and don't break existing functionality.

6. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message.
   ```bash
   git commit -m "Add a descriptive message about your changes"
   ```

7. **Push to Your Fork**: Push your changes to your forked repository.
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request**: Create a pull request from your branch to our main repository.

## Coding Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Comment your code where necessary
- Write unit tests for new features

## Project Structure

Each project folder should have:
- A clear README.md explaining the project
- Requirements file listing dependencies
- Proper documentation for APIs and functions

## Pull Request Process

1. Ensure your code passes all tests
2. Update documentation if necessary
3. Your pull request will be reviewed by a maintainer
4. Once approved, a maintainer will merge your changes

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.