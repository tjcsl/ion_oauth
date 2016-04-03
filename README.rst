=========
ion_oauth
=========

Setup
-----

Run pip install ion_oauth.

Add AUTHENTICATION_BACKENDS = ['ion_oauth.oauth.IonOauth2'] to your settings.py for a django project.

Define SOCIAL_AUTH_ION_KEY and SOCIAL_AUTH_ION_SECRET in your settings.py by following the instructions at https://tjcsl.github.io/ion/developing/oauth.html
