from flask_sqlalchemy import SQLALchemy 

db = SQLALchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    age = db.Column(db.Integer)

    def __init__(self, username, password, first_name, last_name, age):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'age')


class UsersManager(Resource):
    @staticmethod
    def get():
        try: 
            id = request.args['id']
        except Exception: 
            id = None
        if not id:
            users = User.query.all()
            return jsonify(users_schema.dump(users))
        user = User.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        age = request.json['age']

        user = User(username, password, first_name, last_name, age)

        db.session.add(user)
        db.session.commit()

        return jsonify({'message': f'User {username} is inserted'})

    @staticmethod
    def put():
        try:
            id = request.args['id']
        except Exception:
            id = None
        if not id:
            return jsonify({'message': f'User not found'})
        user = User.query.get(id)
        
        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']

        user.username = username
        user.password = password
        user.first_name = first_name
        user.last_name = last_name
        user.age = age

        db.session.commit()

        return jsonify({'Message': f'User {username} altered'})

    @staticmethod 
    def delete():
        try:
            id = request.args['id']
        except Exception:
            id = None
        if not id:
            return jsonify({'message': f'User not found'})
        user = User.query.get(id)
        username = user.username
        db.session.delete(user)

        return jsonify({'Message': f'User {username} has been deleted'}) 