from app import create_app, db
from config.config import Config


class APISetup:

    def setUp(self):
        self.app = create_app(Config())
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.db = db
        db.session.commit()

    def teardown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pick", help="pick: setUp, tearDown", default="s")
    args = parser.parse_args()
    db_app = APISetup()
    db_app.setUp()

    if args.pick == "s":
        try:
            print("nothing to create")
        except Exception as e:
            print(e)
            print("Didnt get created.")
            db_app.db.session.rollback()
        db_app.db.session.commit()
    else:
        db_app.teardown()