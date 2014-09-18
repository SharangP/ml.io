import os
import json
import uuid

from flask import Flask, render_template, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user
from flask.ext.security.signals import user_registered

from ml.utils import parse_data
from ml.MLTask import MLTask

###############################################################################
# Config
###############################################################################
app = Flask(__name__)
app.config.from_object(__name__)
app.config['DEBUG'] = 'PRODUCTION' not in os.environ
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'development_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQL_DATABASE_URI', 'sqlite:///dev.db')
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('PASSWORD_SALT', '$2a$12$skCRnkqE5L01bHEke678Ju')

app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_REGISTER_URL'] = '/register'
app.config['SECURITY_REGISTER_USER_TEMPLATE'] = 'register.html'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'login.html'
app.config['SECURITY_LOGIN_URL'] = '/login'
app.config['SECURITY_CHANGEABLE'] = True

app.config['UPLOAD_FOLDER'] = 'uploads'


# Fake emails for now
class FakeMail(object):
    def send(self, message):
        pass

app.extensions = getattr(app, 'extensions', {})
app.extensions['mail'] = FakeMail()

###############################################################################
# Database
###############################################################################
db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), index = True, unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
          backref=db.backref('user', lazy='dynamic'))

    def is_admin(self):
        return self.has_role("admin")

#TODO store results betterer
class Run(db.Model):
    uuid = db.Column(db.String(36), primary_key = True)
    pending = db.Column(db.Boolean(), nullable=False)
    results = db.Column(db.Text(), nullable=False)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@user_registered.connect_via(app)
def user_registered_sighandler(app, user, confirm_token):
    default_role = user_datastore.find_role("user")
    user_datastore.add_role_to_user(user, default_role)
    db.session.commit()


###############################################################################
# Routes
###############################################################################
@app.route('/')
def index():
    if not current_user.is_authenticated():
        context = {}
        return render_template('index.html', ctx=context)
    else:
        return redirect('/dashboard')

@app.route('/submit', methods=['POST'])
def submit():
    import ipdb; ipdb.set_trace()
    datafile = request.files['datafile']
    if datafile:
        filename = str(uuid.uuid4())
        datafile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        run = Run(uuid=filename, pending=True, results='')
        db.session.add(run)
        db.session.commit()
        return redirect('/results/%s' % filename)
    return redirect('/')

@app.route('/results/<uuid>')
def results(uuid):
    run = Run.query.filter_by(uuid=uuid).first()

    if not run:
        return redirect('/')

    if run.pending:
        #TODO background this
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], uuid)
        contents = file(filepath).read()
        data = parse_data(json.loads(contents))
        task = MLTask({}, {}, data, test=data)
        task.run()
        results = task.results()

        run.pending = False
        run.results = json.dumps(results)

        db.session.add(run)
        db.session.commit()
    else:
        results = json.loads(run.results)

    context = { 'uuid': uuid, 'pending': False, 'results': results }
    return render_template('results.html', ctx=context)

@app.route('/files/<uuid>')
def files(uuid):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], uuid)
    if os.path.exists(filepath):
        return file(filepath).read()
    else:
        return 'File not found'

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
