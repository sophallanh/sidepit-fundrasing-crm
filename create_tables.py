from app import db, create_app

def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()