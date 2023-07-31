# custom_middleware.py

from django.http import HttpResponseServerError


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Customize the error message as you wish
        error_message = "Oops! Something went wrong."
        return HttpResponseServerError(error_message)
