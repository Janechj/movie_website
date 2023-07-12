from django.db import models
from django.urls import reverse


class Director(models.Model):
    directorID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthYear = models.IntegerField(default=1900)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('moviesystem_director_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['name']
        db_table = "Director"


class Movie(models.Model):
    movieID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    releaseDate = models.CharField(max_length=15)
    duration = models.IntegerField(default=120)
    genres = models.CharField(max_length=45)
    ratingFromTomato = models.FloatField(max_length=45)
    ratingFromIMDB = models.FloatField(max_length=45)
    contentRating = models.CharField(max_length=45)
    directorID = models.ForeignKey(Director,db_column='directorID', related_name='movies', on_delete=models.PROTECT)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.ratingFromTomato}'

    def get_absolute_url(self):
        return reverse('moviesystem_movie_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_add_comment_url(self):
        return reverse('add_review_to_movie',
                       kwargs={'pk': self.pk}
                       )

    def primary_key(self):
        return f'{self.movieID}'

    class Meta:
        ordering = ['-ratingFromTomato']
        db_table = "Movie"



class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    preferredGenres = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phoneNumber = models.IntegerField(default=000000)
    adultStatus = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.userName}'

    def get_absolute_url(self):
        return reverse('moviesystem_myprofile_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('moviesystem_myprofile_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def primary_key(self):
        return f'{self.userID}'

    class Meta:
        db_table = "User"


class Actor(models.Model):
    actorID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthYear = models.IntegerField(default=1900)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} '

    def get_absolute_url(self):
        return reverse('moviesystem_actor_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def primary_key(self):
        return f'{self.actorID}'

    class Meta:
        ordering = ['name']
        db_table = "Actor"


class Act(models.Model):
    actID = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=255,default='')
    actorID = models.ForeignKey(Actor,db_column='actorID', related_name='acts', on_delete=models.PROTECT)
    movieID = models.ForeignKey(Movie,db_column='movieID', related_name='acts', on_delete=models.PROTECT)

    def Formovie(self):
        return f'{self.actorID.name}'

    def Foractor(self):
        return f'{self.movieID.name} - {self.movieID.ratingFromTomato}'

    def get_movie_absolute_url(self):
        return reverse('moviesystem_movie_detail_urlpattern',
                       kwargs={'pk': self.movieID.primary_key()}
                       )


    def get_actor_absolute_url(self):
        return reverse('moviesystem_actor_detail_urlpattern',
                       kwargs={'pk': self.actorID.primary_key()}
                       )

    class Meta:
        db_table = "Act"


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    source = models.CharField(choices=[('IMDB', 'IMDB'), ('Rotten Tomatoes', 'Rotten Tomatoes')], max_length=255, default='IMDB')
    rating = models.IntegerField(default=5)
    movieID = models.ForeignKey(Movie,db_column='movieID', related_name='reviews', default='', on_delete=models.PROTECT)
    content = models.TextField(default="")
    userID = models.ForeignKey(User,db_column='userID', related_name='reviews', default='', on_delete=models.PROTECT)

    def __str__(self):
        if self.rating == -1:
            return f'noRating/ {self.content} '
        else:
            return f'{self.rating}/ {self.content} '


    def Formovie(self):
            return f'{self.userID.userName}'


    def Foruser(self):
            return f'{self.movieID.name}'

    def get_movie_absolute_url(self):
        return reverse('moviesystem_movie_detail_urlpattern',
                       kwargs={'pk': self.movieID.primary_key()}
                       )

    def get_user_absolute_url(self):
        return reverse('moviesystem_myprofile_urlpattern',
                       kwargs={'pk': self.userID.primary_key()}
                       )


    def get_update_url(self):
        return reverse('moviesystem_review_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('moviesystem_review_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        db_table = "Review"


class Watch(models.Model):
    watchID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, db_column='userID', related_name='watchs', on_delete=models.PROTECT)
    movieID = models.ForeignKey(Movie, db_column='movieID', related_name='watchs', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.movieID.name} - {self.movieID.ratingFromTomato}'

    def Foruser(self):
        return f'{self.movieID.name} - {self.movieID.ratingFromTomato}'


    def get_movie_absolute_url(self):
        return reverse('moviesystem_movie_detail_urlpattern',
                       kwargs={'pk': self.movieID.primary_key()}
                       )


    class Meta:
        db_table = "Watch"
