from flask import request

from app.api import bp
from app.controllers import user_controller


@bp.route('/RequestRegistration', methods=['POST'])
def request_registration_otp():
    """
    Send otp for registration of Client to given phone number
    :return: message in Response
    """
    return user_controller.request_registration_otp_controller(request)

