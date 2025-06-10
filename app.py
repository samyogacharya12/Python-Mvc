from flask import Flask
from view.category_views import category_routes


app = Flask(__name__)

app.register_blueprint(category_routes)

if __name__ == "__main__":
    app.run(debug=True)
