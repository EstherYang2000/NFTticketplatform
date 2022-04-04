from rolepermissions.roles import AbstractUserRole


class Customer(AbstractUserRole):
    available_permissions = {

    }
class Company(AbstractUserRole):
    available_permissions = {
        'createevent': True,
        'updateevent': True,
    }