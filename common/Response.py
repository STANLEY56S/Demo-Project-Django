from rest_framework.response import Response

class Responses:

    def load_response(self, has_error, message, result, status_code):
        self.has_error = has_error
        self.status_code = status_code
        self.message = message
        self.result = result

    def load_response(self):

        return ''