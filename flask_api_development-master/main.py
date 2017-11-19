from flask import Flask
from api.countries import country_api

app = Flask(__name__)
app.register_blueprint(country_api)

if __name__ == '__main__':
    app.run(port=5000,debug=True)