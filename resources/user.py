from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This is Username and it is mandatory'
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help='This is password and it is mandatory'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':'A User with same name already exist'}, 400

        user  = UserModel(**data) #**data=data['username'],data['password']
        user.save_to_db()

        return {"message":"User registered Successfully"}, 201
