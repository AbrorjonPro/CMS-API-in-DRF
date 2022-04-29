from django.contrib.auth.decorators import login_required
from django.conf import settings


# @login_required(login_url=settings.LOGIN_URL)
def editing_object(request):
    return True
    # return request.user.is_staff


