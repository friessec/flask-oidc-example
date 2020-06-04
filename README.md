# flask-oidc-example
example based on pyoidc

# Init
pip install -r requirements.txt

# Config

* Provide your OP settings in provider.json
* If your not using Okta change @auth.oidc_auth('okta') to your provider name (must match provider.json) in app/main/routes.py
* Several OpenID provider are supported. Additional login routes must be added!
