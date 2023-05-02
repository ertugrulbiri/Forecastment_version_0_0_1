from flask import request

from app.api import bp
from app.controllers import user_controller


@bp.route('/RequestRegistration', methods=['POST'])
def request_registration_otp():
    """
    Registration system endpoint
    :return: client information
    """
    return user_controller.user_registration_controller(request)

