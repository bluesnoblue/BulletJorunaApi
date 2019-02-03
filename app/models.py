from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.String(11), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, **kwargs):
        self.username = username
        self.role = kwargs['role_id']
        if self.role is None:
            self.role = Role.query.filter_by(default=True).first()

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Bullet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bullet_type = db.Column(db.Integer)  # 任务 1事件 2记录
    status = db.Column(db.Integer, default=0)  # 0未完成 1已完成 2延后
    body = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True)
    mark = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, bullet_type, body, user_id):
        self.status = 0
        self.bullet_type = bullet_type
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return '<Bullet %s form user_%s>' % (self.body, self.user_id)

    def update_mark(self):
        self.mark = (self.mark + 1) % 3

    def update_body(self):
        self.body = (self.mark + 1) % 3

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Permission:
    ONLY_QUERY = 0x01  # 仅查询
    FORBID = 0x03  # 封号
    ASSIGN = 0x07  # 分配行号
    ADMINISTRATOR = 0x0f  # 这个权限要异或

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    default = db.Column(db.Boolean,default=False,index= True)
    users = db.relationship('User',beackref='role',lazy='dynamic')

    @staticmethod
    def insert_role():
        roles = {
            'STAFF': (Permission.ONLY_QUERY, True),
            'HIGH_STAFF': (Permission.ONLY_QUERY |
                           Permission.FORBID, False),
            'LEADER': (Permission.ONLY_QUERY |
                       Permission.FORBID |
                       Permission.ASSIGN, False),
            'ROOT': (0x0f, False)}
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %s>'%self.name