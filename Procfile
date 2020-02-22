release: python deekoo_auth/cli.py db upgrade
web: gunicorn -w 1 -p 8000 deekoo_auth.wsgi:app