from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput
from django.core.exceptions import ValidationError

from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"
        widgets = {
            "date": DateInput(attrs={"type": "date"}),
            "start": TimeInput(attrs={"type": "time"}),
            "duration": TextInput(attrs={"type": "number", "min": "1", "max": "6"})
        }

    def clean_date(self):
        cleaned_date = self.cleaned_data.get("date")
        if cleaned_date < date.today():
            raise ValidationError("Meetings cannot be set in the past")
        return cleaned_date
