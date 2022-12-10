from flask import Flask, request

# Flask() takes one required parameter "import name". This matters, sometimes.
# For more details read the 'About the First Parameter' section
# [here](https://flask.palletsprojects.com/en/2.2.x/api/).
application = Flask(__name__)


# This is called a controller. Controllers are where you define

# (1) a function that performs some action (e.g. log in a user, return
# data from a database)
# (2) how to call that function (i.e. the location you must make a request to, the "types" of requests you can make...)
@application.route("/")
def fulfill_default_request():

    return "You've made a GET request to the main endpoint! \
                An example GET request would return a message, image, or an entire web page!"


# This is a cats controller. Observe how our first argument is '/cat'. This means
# any cat-related requests should made to the /cat endpoint.
@application.route("/cat", methods=["GET", "POST"])
def fulfill_cat_request():

    # included this to illustrate how you can define both a GET and POST request from a single controller
    if request.method == "GET":
        pass

    # define what happens if you make a POST request to the /cat endpoint
    if request.method == "POST":

        # request.get_json() means you're expecting the request content-type to be 'application/json'
        # if the request is any other type, the server will respond with an error.
        name = request.get_json().get("name", None)

        # define what you want to send back
        on_success = f"You've successfully made a POST request to the /cat endpoint! \
                    An example POST request would be to add your cat {name} to a cats database."
        on_fail = "The \"name\" field was not found in your request body :("

        # return success message if "name" was provided, otherwise return the fail message
        return on_success if name else on_fail


# This starts a web server that "executes" the logic you defined, above.
if __name__ == "__main__":
    application.run()
