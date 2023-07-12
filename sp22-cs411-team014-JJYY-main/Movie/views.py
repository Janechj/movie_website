from django.core.paginator import Paginator
from django import forms
from django.shortcuts import redirect, render

from moviesystem.models import Movie, User
from moviesystem.views import Myprofile


def redirect_root_view(request):
    return redirect('moviesystem_home_urlpattern')


def search(request):
    search_title = request.GET.get('wd', '')
    search_movies = Movie.objects.filter(name__icontains=search_title)
    search_movie_count = search_movies.count()

    # paginator = Paginator(search_movies, settings.EACH_PAGE_BLOGS_NUMBER)

    context = {'search_title': search_title,
               'search_movie_count':search_movie_count,
               'search_movie': search_movies}
    try:
        context["user_id"] = request.COOKIES["user_id"]
        context["login_status"] = request.COOKIES["login_status"]
    except:
        pass
    return render(request, 'moviesystem/search.html', context)


def userSearch(request):
    usr_name = request.GET.get('usr', '')
    pwd = request.GET.get('pwd', '')
    user = User.objects.filter(userName=usr_name)
    user_count = user.count()
    print(f"user:{user_count}")
    context = {}
    if (user_count == 0):
        context = {'error_msg': "User Not Found"}
        return render(request, 'moviesystem/login.html', context)
    elif (user_count > 1):
        context = {'error_msg': "More than 1 user with the same name"}
        return  render(request, 'moviesystem/login.html', context)
    else:
        if (pwd == user[0].password):
            user_id = user[0].userID
            watch_list = user[0].watchs.all()
            review_list = user[0].reviews.all()
            response = render(request, 'moviesystem/myprofile.html',
                              {'user': user[0],
                               'watch_list': watch_list,
                               'review_list': review_list,
                               'login_status': "true",
                               "user_id": int(user[0].userID)})
            response.set_cookie("login_status", "true")
            response.set_cookie("user_id", user_id)

            return response
        else:
            context = {'error_msg': "password incorrect"}
            print(f"pwd for {usr_name}: {user[0].password}")
            return render(request, 'moviesystem/login.html', context)


def showAccount(request):
    user_id = request.COOKIES['user_id']
    status = request.COOKIES["login_status"]
    if (status=="true"):
        myProfile = Myprofile
        print(user_id)
        return myProfile.get(Myprofile, request, int(user_id))


def logOut(request):
    response = render(
                request,
                'moviesystem/logout.html',
                {"login_status": "false", "user_id": "9999999"}
            )
    response.set_cookie("login_status", "false")
    response.set_cookie("user_id", "9999999")
    return response


# def searchgoodactor(self):
#     book_obj = models.Book.objects.filter.




