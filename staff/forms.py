from django import forms

class TimetableForm(forms.Form):
    off_day_choices = [('Thu', 'Thursday'),
            ('Fri', 'Friday'), ('Sat', 'Saturday'),
            ('Sun', 'Sunday')]

    off_day = forms.CharField(label='Select Off day',
            widget=forms.Select(choices=off_day_choices))

    class Meta:
        abstract = True

class Morning(TimetableForm):
    names = forms.CharField(label="Morning Shift names:")

class Afternoon(TimetableForm):
    names = forms.CharField(label="Afternoon Shift names:")
