import os
from api import app

if __name__ == '__main__':
    host = None

    if 'HOST' in os.environ:
        host = os.environ['HOST']

    app.run(host, debug=True)