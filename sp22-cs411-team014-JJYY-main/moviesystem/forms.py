from django import forms

from moviesystem.models import Review, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userName', 'preferredGenres', 'phoneNumber')

    def clean_user_name(self):
        return self.cleaned_data['userName'].strip()

    def clean_user_preferredGenres(self):
        return self.cleaned_data['preferredGenres'].strip()

    def clean_user_phoneNumber(self):
        return self.cleaned_data['phoneNumber'].strip()



class addReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating','source','content')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating','content')






