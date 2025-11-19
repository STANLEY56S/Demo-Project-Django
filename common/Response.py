from rest_framework.response import Response
from rest_framework import status
from common.common_utility import open_read_file


class ResponseCode:
    _cache = {}

    @classmethod
    def _load_codes(cls):
        if not cls._cache:

            # changed here for Based on the project id if We want to load different response codes

            # Loads response_config.json
            file = open_read_file('config', '', 'response')

            cls._cache = file
            for key, value in cls._cache.items():
                setattr(cls, key, cls(key, value['code'], value['message']))

    def __init__(self, name, code, message):
        self._name = name
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    @classmethod
    def create_response(cls, response_code_name, extra_data=None, extra_message=None):

        # Get code definition dynamically
        response_code = getattr(cls, response_code_name, None)

        if response_code is None:
            # Unknown response_code requested
            return Response({
                "code": 9999,
                "message": "Unknown error",
                "hasError": True,
                "result": None
            }, status=status.HTTP_400_BAD_REQUEST)

        # Allow overriding message
        message = extra_message if extra_message else response_code.message

        # Build base structure
        response = {
            "code": response_code.code,
            "message": message,
            "hasError": response_code.code >= 2000,   # error codes >= 2000
            "result": None
        }

        # Add user data if passed
        if extra_data:
            response["result"] = extra_data

        # Choose HTTP status based on code range
        http_status = status.HTTP_200_OK
        if response_code.code >= 2000:
            http_status = status.HTTP_400_BAD_REQUEST
        if response_code.code >= 5000:
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, status=http_status)


# Load all response codes on import
ResponseCode._load_codes()
