from requests import request as req
from django.http import JsonResponse
from common.enum import HttpMethods, HttpResponses

class Deliverer:
    def __init__(self, to, method=HttpMethods.GET, is_secure=False):
        self.to = to
        self.method = method
        self.is_secure = is_secure

    def is_available_method(self, request):
        return self.method.value == request.method

    def _send(self, request, method, params={}):
        if not self.is_available_method(request):
            return JsonResponse({'status' : HttpResponses.METHOD_NOT_ALLOWED.value})
        url = 'https' if self.is_secure else 'http' + '://' + self.to
        try:
            res = req(method.value, url, params=params).json()
        except Exception as e:
            print(e)
            res = {'status' : HttpResponses.INTERNER_SERVER_ERROR.value}
        return JsonResponse(res)

    @classmethod
    def send(cls, request, to, method=HttpMethods.GET, params={}, is_secure=False):
        deliverer = cls(to, method, is_secure)
        return deliverer._send(request, method, params)
