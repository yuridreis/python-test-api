from flask import Flask
from flask_restx import Resource, Api
import re

app = Flask(__name__)
api = Api(app)


@api.route('/<cpf>')
class Cpf(Resource):
    def get(self, cpf):

        if re.match('^\d{3}.?\d{3}.?\d{3}-?\d{2}$', cpf):
            with open('blacklist.txt', 'r') as f:
                file = f.read()
                if cpf in file:
                    blocked = True
                else:
                    blocked = False

            if blocked:
                return {'status': 'Block'}
            else:
                return {'status': 'Free'}
        else:
            return "Invalid CPF"


if __name__ == '__main__':
    app.run(debug=True)
