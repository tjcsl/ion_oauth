# ion-oauth
Ion Oauth2 backend for [python-social-auth](https://github.com/python-social-auth/social-app-django).


Setup
-----

Install with pip:

```
pip install ion_oauth
```

Add
```
AUTHENTICATION_BACKENDS = [
    ...
    'ion_oauth.oauth.IonOauth2',
]
```
to `settings.py` in your django project.

Define `SOCIAL_AUTH_ION_KEY` and `SOCIAL_AUTH_ION_SECRET` in `settings.py` by following the instructions at https://guides.tjhsst.edu/ion/using-ion-oauth.
The redirect_uris for Django projects should be "http://<site-url>/complete/ion/" and "http://<site-url>/complete/ion".
