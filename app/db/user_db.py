from app import db
from app.models.user_models import User


def create_user(user):
    """
    :param user: User()
    :return: Boolean
    """
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def check_phone_number_is_in_use(phone_number):
    return db.session.query(User).filter(User.phone_number == phone_number).first()

    # This method is same as upside
    # User.query.filter_by(phone_number=phone_number).first()
