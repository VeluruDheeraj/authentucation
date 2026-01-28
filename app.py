from flask import Flask
from database import init_db, close_db
from auth import register_auth_routes
from admin import register_admin_routes
from member import register_member_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"

register_auth_routes(app)
register_admin_routes(app)
register_member_routes(app)

@app.teardown_appcontext
def teardown(e=None):
    close_db(e)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
