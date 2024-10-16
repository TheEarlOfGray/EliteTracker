from application import db, app

# db.drop_all()
with app.app_context():
    db.create_all()
