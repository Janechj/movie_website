from django.contrib import admin
from .models import User, Movie, Director, Actor, Act, Review, Watch

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Act)
admin.site.register(Review)
admin.site.register(Watch)
