import logging
from datetime import datetime

class requestReponseMiddelWare:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request, *args, **kwds):
        current_datetime = datetime.now()
        method = request.method
        path = request.get_full_path()
        response = self.get_response(request)
        
        status = response.status_code

        logging_messgae = "{} {} {} {}".format(
            current_datetime, method, path, status
        )

        if status >= 400:
            print(logging_messgae)
        elif status >= 500:
            print(logging_messgae)
        else:
            print(logging_messgae)

        return response