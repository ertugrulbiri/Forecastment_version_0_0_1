from flask import jsonify

from app.services import user_services
from errors import bad_request


def user_registration_controller(request):
    data = request.get_json() or {}
    # check registration data fields are correct or not
    if not user_services.check_registrarion_data(data):
        return bad_request(message="Üyelik bilgileri eksik gönderildi")

    # Now field controls
    if not isinstance(data['phone_number'], str):
        return bad_request(message="Telefon Formatı yanlış verildi")

    if len(data['password']) < 8:
        return bad_request(message="Password must be at least 8 characters")

    if user_services.check_phone_number_is_already_in_use_service(data['phone_number']):
        return bad_request(message="phone number already in use")

    if user_services.register_user_service(data['first_name'], data['last_name'], data['phone_number'],
                                        data['password'], data['email']):

        return jsonify(message="Registration Success, must return token")

    return bad_request(message="Üyelik başarılı değil")
