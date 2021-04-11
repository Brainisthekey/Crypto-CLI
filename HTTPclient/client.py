from enum import Enum
import requests
from typing import List


class HTTPClient():
    BASE_PATH = None
    headers = None
    suported_codes = None

    def __init__(self, headers: dict = None, suported_codes: List[int] = None, BASE_PATH: str = None):
        self.headers = headers
        self.suported_codes = suported_codes
        self.BASE_PATH = BASE_PATH
        self.args = {'headers': self.headers}
    def request(self, type: Enum, path: str, params: dict, body: dict = None) -> requests.models.Response:
        self.args.update({'url': self.BASE_PATH + path})
        if type == HTTPClient.RequestType.GET:
            response = requests.get(**dict(self.args, params=params))
        elif type == HTTPClient.RequestType.POST:
            response = requests.post(**dict(self.args, params=params, body=body))
        elif type == HTTPClient.RequestType.PUT:
            response = requests.put(**dict(self.args, params=params, body=body))
        elif type == HTTPClient.RequestType.DELETE:
            response = requests.delete(**self.args['url']['headers']['params']['body'])
        elif type == HTTPClient.RequestType.PATCH:
            response = requests.put(**dict(self.args, params=params, body=body))
        else:
            raise BaseException

        return self.handle_response(response)

    def handle_response(self, response: requests.models.Response) -> requests.models.Response :
        if self.suported_codes:
            if response.status_code in self.suported_codes:
                return response
            else:
                raise BaseException
        
    class RequestType(Enum):
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        PATCH = 'DELETE'
        DELETE = 'PATCH'
