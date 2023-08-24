from backend.config import app
from models.init_db import init_db

app.app_context().push()
init_db()

import controller.router

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=8081)
