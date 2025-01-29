from flask import Flask
from flask_restful import Api, Resource 
from flask_cors import CORS

from datetime import datetime, timezone


app = Flask(__name__)

# initialize the api 
api = Api(app) 

# add cors support 
cors = CORS(app)

# The resource class for the data 
class Me(Resource):

    # Make a GET request on resource /me 
    def get(self):
        current_datetime = datetime.now(timezone.utc)
        
        return {
            "email": "ebonko2017ip@gmail.com",
            "current_datetime": current_datetime.replace(microsecond=0).isoformat(),
            "github_url": "<https://github.com/ubterko/stage-zero>"
        }, 200

# Add resource to the api 
api.add_resource(Me, '/me')

if __name__ == "__main__":
    app.run(debug=True)