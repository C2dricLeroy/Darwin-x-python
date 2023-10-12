from flask import Flask
from controller.user_controller import UserController

app = Flask(__name__)

user_controller = UserController()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/performance/<int:investor_id>')
def get_performances(investor_id):
    return user_controller.get_user_informations(investor_id)


if __name__ == '__main__':
    app.run()
