from django.http import HttpResponse

def showcookie(request):
    """
    read cookie from current browser
    """
    login_status = request.COOKIES['login_status']
    profile_link = request.COOKIES['profile_link']
    user_id = request.COOKIES['user_id']
    cookie = {"login_status":login_status, "profile_link":profile_link, "user_id":user_id}
    return cookie
