# Security Policy

## Disclaimer

**IMPORTANT**: The Django Crafts repository contains sample projects and tutorials for educational purposes. We are not responsible for any security leakages that might occur in your production environment if you implement these examples without proper security considerations. Please refer to the original packages' documentation and security guidelines for any corrections or updates.

## Reporting a Vulnerability

If you discover a security vulnerability within any of the projects in this repository:

1. **Do Not** disclose the vulnerability publicly
2. Send an email to [yokwejuste@gmail.com](mailto:yokwejuste@gmail.com) describing the issue
3. Allow time for the vulnerability to be addressed before disclosing it publicly

## Security Best Practices

When implementing any of the projects from this repository in your own applications, please consider the following security best practices:

1. **Keep Dependencies Updated**: Always use the latest stable versions of Django and other dependencies
2. **Secure Environment Variables**: Never commit sensitive information like API keys or passwords
3. **Implement Proper Authentication**: Follow security standards for user authentication
4. **Regular Security Audits**: Perform regular security audits of your code
5. **Follow Django's Security Guidelines**: Refer to [Django's security documentation](https://docs.djangoproject.com/en/stable/topics/security/)

## Original Package References

For specific security concerns related to the packages used in these projects, please refer to the security documentation of the original packages:

- Django: [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)
- Django Two-Factor Authentication: Refer to the documentation of the specific package used in the django2fa project
- Django Passkeys: For WebAuthn and Passkey implementation, refer to [WebAuthn Documentation](https://webauthn.guide/) and [FIDO Alliance Guidelines](https://fidoalliance.org/specifications/)
- Django reCAPTCHA: For integration of Google reCAPTCHA, refer to [Google reCAPTCHA Documentation](https://developers.google.com/recaptcha/docs/security)
- Django SSO: For Single Sign-On implementation, refer to [OAuth 2.0 Security Best Practices](https://oauth.net/2/security-best-practices/) and [OpenID Connect Security](https://openid.net/specs/openid-connect-core-1_0.html#Security)

## Version Support

We only support the latest version of each project in this repository. If you find security issues in older versions, please upgrade to the latest version before reporting.