#
# App-runner script
#

import os

from booze import app

if __name__ == '__main__':
    # Import heroku config, or set defaults
    port = os.environ.get('PORT')
    if not port:
        port = 5000
    # Run the app
    app.run(
        host='0.0.0.0',
        port=int(port),
        debug=True
        )
