from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth


class AutoLogout:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if not request.user.is_authenticated:

            return response

        else:
            try:
                if datetime.now() - datetime.strptime(request.session['last_touch'], '%Y-%m-%d %H:%M:%S.%f') > timedelta(
                        0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                    print('Bye')
                    auth.logout(request)
                    del request.session['last_touch']
                    return response
            except KeyError:
                pass

            request.session['last_touch'] = str(datetime.now())

        return response
