from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from moviesystem import recommendation as RC
from moviesystem.forms import ReviewForm, UserForm, addReviewForm
from moviesystem.models import Director, Movie, User, Act, Actor, Review



class Home(View):

    def get(self, request, reset=False):
        actor_list = goodactor()
        movie_list = hotmovie()
        try:
            context = {"user_id": request.COOKIES["user_id"], "login_status": request.COOKIES["login_status"],
                       'goodActor': actor_list, 'hotMovie': movie_list}
            response = render(
                request,
                'moviesystem/home.html',
                context,
            )
            if (reset):
                response.set_cookie("login_status", "false")
                response.set_cookie("user_id", "")
            return response
        except:
            print("no user logged in")
            return render(
                request,
                'moviesystem/home.html',
                {'goodActor': actor_list,
                 'hotMovie': movie_list}
            )


class DirectorList(View):

    def get(self, request):
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        context["director_list"] = Director.objects.all()
        return render(
            request,
            'moviesystem/director_list.html',
            context
        )

    page_kwarg = 'page'
    paginate_by = 10;  # 25 instructors per page
    template_name = 'moviesystem/director_list.html'

    def get(self, request):
        directors = Director.objects.all()
        paginator = Paginator(
            directors,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'director_list': page,
        }
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(
            request, self.template_name, context)


class MovieList(View):

    page_kwarg = 'page'
    paginate_by = 10;  # 25 instructors per page
    template_name = 'moviesystem/movie_list.html'

    def get(self, request):
        movies = Movie.objects.all()
        paginator = Paginator(
            movies,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'movie_list': page,
        }
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(
            request, self.template_name, context)


class MovieDetail(View):

    def get(self, request, pk):
        movie = get_object_or_404(
            Movie,
            pk=pk
        )
        act_list = movie.acts.all()
        director = movie.directorID
        review_list = movie.reviews.all()
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        context['movie'] = movie
        context["director"] = director
        context["act_list"] = act_list
        context["review_list"] = review_list
        return render(
            request,
            'moviesystem/movie_detail.html',
            context
        )


class DirectorDetail(View):

    def get(self, request, pk):
        director = get_object_or_404(
            Director,
            pk=pk
        )
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        movie_list = director.movies.all()
        context["director"] = director
        context["movie_list"] = movie_list
        return render(
            request,
            'moviesystem/director_detail.html',
            context
        )


class ActorDetail(View):

    def get(self, request, pk):
        actor = get_object_or_404(
            Actor,
            pk=pk
        )
        act_list = actor.acts.all()
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        context["actor"] = actor
        context["act_list"] = act_list
        return render(
            request,
            'moviesystem/actor_detail.html',
            context
        )


class Myprofile(View):

    def get(self, request, pk):
        user = get_object_or_404(
            User,
            pk=pk
        )

        watch_list = user.watchs.all()
        review_list = user.reviews.all()
        id_int = -1
        login_status = "false"
        try:
            login_status = request.COOKIES["login_status"]
        except:
            pass
        try:
            id_int = int(request.COOKIES["user_id"])
        except:
            pass
        print(id_int)
        return render(
            request,
            'moviesystem/myprofile.html',
            {'user': user,
             'watch_list': watch_list,
             'review_list': review_list,
             'login_status': login_status,
             "user_id": id_int}
        )


class ActorList(View):

    page_kwarg = 'page'
    paginate_by = 10;
    template_name = 'moviesystem/actor_list.html'

    def get(self, request):
        actors = Actor.objects.all()
        paginator = Paginator(
            actors,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'actor_list': page,
        }
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(
            request, self.template_name, context)


class ReviewList(View):

    def get(self, request):

        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        context["review_list"] = Review.objects.all()
        return render(
            request,
            'moviesystem/review_list.html',
            context
        )


class ReviewUpdate(View):
    form_class = ReviewForm
    model = Review
    template_name = 'moviesystem/review_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        review = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=review),
            'review': review,
        }
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        review = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=review)
        if bound_form.is_valid():
            new_review = bound_form.save()
            userID = new_review.userID.pk
            return redirect('moviesystem_myprofile_urlpattern', pk=userID)
        else:
            context = {
                'form': bound_form,
                'review ': review,
            }
            try:
                context["user_id"] = request.COOKIES["user_id"]
                context["login_status"] = request.COOKIES["login_status"]
            except:
                pass
            return render(
                request,
                self.template_name,
                context)


class MyprofileUpdate(View):
    form_class = UserForm
    model = User
    template_name = 'moviesystem/user_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=user),
            'review': user,
        }

        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass

        return render(
            request, self.template_name, context)


    def post(self, request, pk):
        user = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=user)
        if bound_form.is_valid():
            new_user = bound_form.save()
            userID = new_user.pk
            return redirect('moviesystem_myprofile_urlpattern', pk=userID)
        else:
            context = {
                'form': bound_form,
                'user ': user,
            }
            return render(
                request,
                self.template_name,
                context)


def add_review_to_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = get_object_or_404(User, pk=request.COOKIES["user_id"])
    context = {}
    try:
        context["user_id"] = request.COOKIES["user_id"]
        context["login_status"] = request.COOKIES["login_status"]
    except:
        pass
    if request.method == "POST":
        form = addReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movieID = movie
            review.userID = user
            review.save()
            return redirect('moviesystem_movie_detail_urlpattern', pk=movie.pk)
    else:
        form = addReviewForm()
    context["form"] = form
    return render(request, 'moviesystem/add_review_to_movie.html', context)


class ReviewDelete(View):

    def get(self, request, pk):
        review = self.get_object(pk)
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        context['review'] = review
        return render(
                request,
                'moviesystem/review_confirm_delete.html',
                context
            )

    def get_object(self, pk):
        return get_object_or_404(
            Review,
            pk=pk)

    def post(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return redirect('moviesystem_myprofile_urlpattern', pk=review.userID.pk)


class Login(View):
    def get(self, request):
        context = {}
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(request, 'moviesystem/login.html', context)


def goodactor():
    cursor = connection.cursor()

    cursor.execute("""select actorID, name, avgrating1
                    from (select a1.actorID, AVG(ratingFromTomato) as avgrating1,count(movieID) as nummovie
                    from Act a1 natural join Movie
                    group by a1.actorID) as avgrate1 
                    Natural Join Actor
                    where avgrating1 >70 and nummovie>3
                    ORDER BY name""")
    rows = cursor.fetchall()
    actor_list = []
    for row in rows:
        actor = get_object_or_404(
            Actor,
            pk=row[0]
        )
        actor_list.append(actor)
    return actor_list


def hotmovie():
    cursor = connection.cursor()

    cursor.execute("""SELECT tmp.movieID,m.name,tmp.avgrating
                       FROM Movie m NATURAL JOIN (SELECT r.movieID, COUNT(r.reviewID) as numreview, AVG(r.rating) AS avgrating 
                               FROM Review r
                               WHERE (r.rating != -1)
                               GROUP BY r.movieID) tmp
                       where numreview>15
                       ORDER BY avgrating DESC LIMIT 10;""")
    rows = cursor.fetchall()
    movie_list = []
    for row in rows:
        movie = get_object_or_404(
            Movie,
            pk=row[0]
        )
        movie_list.append(movie)
    return movie_list

class yearsmovie(View):

    def get(self, request):

        cursor = connection.cursor()
        cursor.callproc('Result15')
        movielist_1990 = []
        movielist_2000 = []
        movielist_2010 = []

        actorlist_1990 = []
        actorlist_2000 = []
        actorlist_2010 = []

        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            if row[4] == 1990:
                movie = get_object_or_404(
                    Movie,
                    pk=row[0]
                )
                if row[3] is not None:
                    actor = get_object_or_404(
                        Actor,
                        pk=row[3]
                    )
                    actorlist_1990.append(actor)
                movielist_1990.append(movie)
            elif row[4] == 2000:
                movie = get_object_or_404(
                    Movie,
                    pk=row[0]
                )
                if row[3] is not None:
                    actor = get_object_or_404(
                        Actor,
                        pk=row[3]
                    )
                    actorlist_2000.append(actor)
                movielist_2000.append(movie)
            elif row[4] ==2010:
                movie = get_object_or_404(
                    Movie,
                    pk=row[0]
                )
                if row[3] is not None:
                    actor = get_object_or_404(
                        Actor,
                        pk=row[3]
                    )
                    actorlist_2010.append(actor)
                movielist_2010.append(movie)

        context = {
            'Bestmovie1990': movielist_1990,
            'Bestmovie2000': movielist_2000,
            'Bestmovie2010': movielist_2010,
            'BestActor1990': actorlist_1990,
            'BestActor2000': actorlist_2000,
            'BestActor2010': actorlist_2010,
        }
        try:
            context["user_id"] = request.COOKIES["user_id"]
            context["login_status"] = request.COOKIES["login_status"]
        except:
            pass
        return render(request, 'moviesystem/yearsmovie.html', context)


def recommend(user_id):
    movieIDList = RC.retrieveResForUser(user_id)
    ls = []
    for row in movieIDList:
        movie = get_object_or_404(
            Movie,
            pk=row
        )
        ls.append(movie)
    return ls

class Recommendation(View):
    def get(self, request, reset=False):
        try:
            context = {"user_id": request.COOKIES["user_id"], "login_status": request.COOKIES["login_status"]}

            if (context["login_status"] == "true"):
                recommendation = recommend(int(request.COOKIES["user_id"]))
                context["recommendations"] = recommendation
            response = render(
                request,
                'moviesystem/recommendation.html',
                context,
            )
            if (reset):
                response.set_cookie("login_status", "false")
                response.set_cookie("user_id", "")
            return response
        except:
            return render(
                request,
                'moviesystem/home.html',{}
            )
