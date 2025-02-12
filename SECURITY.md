## DEPLOYMENT

Make sure to deploy your application safely by following the FLASK deployment documentation. If you run it on a production server, your application could be vulnerable.

Remember to have a securely generated secret key that should be changed periodically if you plan on hosting it publicly. You can generate a secure key by running this command in Python:

```python
python -c 'import secrets; print(secrets.token_hex())'
```

Alternatively, you can follow this step-by-step guide on deploying your server securely:
[Flask Deployment Guide](https://flask.palletsprojects.com/en/stable/tutorial/deploy/)
