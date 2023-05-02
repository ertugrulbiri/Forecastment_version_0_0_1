from app.db import user_db
from app.models.user_models import User


def check_registrarion_data(data):
    if 'first_name' not in data or 'last_name' not in data or 'phone_number' not in data\
            or "email" not in data or 'password' not in data:
        return False
    return True


def register_user_service(first_name, last_name, phone_number, password, email):
    """
    Registers users to system
    :param first_name: Str
    :param last_name:  Str
    :param phone_number: Str
    :param password: str
    :param email: email(str)
    :return: Boolean
    """
    user = User()
    user.from_dict(first_name, last_name, phone_number, password, email)

    return user_db.create_user(user)


def check_phone_number_is_already_in_use_service(phone_number):
    if user_db.check_phone_number_is_in_use(phone_number):
        return True
    return False
