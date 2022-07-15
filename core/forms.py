from django import forms

from core.models import Card


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
        widgets = {
            "release_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "activity_end_date": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(str(number)) != 16:
            raise forms.ValidationError("Not correct number, number has less or greater 16 digit", code="invalid")

        if Card.objects.filter(number=number).exists():
            raise forms.ValidationError("This card exist in database", code="invalid")

        return number

