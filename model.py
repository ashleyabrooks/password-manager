from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///password-manager'
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User of password manager app."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        """Add helpful representation of model object when printed."""

        return "< User user_id = %s, email = %s >" % (self.user_id, self.email)


class Password(db.Model):
    """Password 'packet' to be encrypted before adding to DB."""

    __tablename__ = 'passwords'

    password_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    website = db.column(db.String(500), nullable=False)
    username = db.column(db.String(100), nullable=False)
    password = db.column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)



if __name__ == '__main__':
    # Helpful for running this module interactively

    from server import app
    connect_to_db(app)
    print "Connected to db."