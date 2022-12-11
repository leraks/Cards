from django import forms
from .models import Card


CHOICES = [('1', '1 year'), ('2', '6 months'), ('3', '1 months')]


class CreateForm(forms.Form):
    cvc = forms.IntegerField(label='cvc', max_value=999)
    number_of_digits_series = forms.CharField(label="Количества цифр в серии",)
    number_of_generated = forms.IntegerField(label="Количество генераций новых карт", min_value=1, max_value=100)
    choice_date_active_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def clean(self):
        super(CreateForm, self).clean()
        number_of_digits_series = self.cleaned_data['number_of_digits_series']
        cvc = self.cleaned_data['cvc']
        number_of_generated = self.cleaned_data['number_of_generated']

        if len(str(cvc)) != 3:
            self._errors['cvc'] = self.error_class(['Неверный cvc'])

        if number_of_generated > 100 or number_of_generated < 0:
            self._errors['number_of_generated'] = self.error_class(['Количество созданий карт от 1 до 100 !'])

        if not number_of_digits_series.isdigit():
            self._errors['number_of_digits_series'] = self.error_class(['Только цифры'])

        elif number_of_digits_series.isdigit():
            if int(number_of_digits_series) > 19 or int(number_of_digits_series) < 13:
                self._errors['number_of_digits_series'] = self.error_class(['Неверное количество цифр в номере,'
                                                                            ' цифр должо быть от 13 до 19'])