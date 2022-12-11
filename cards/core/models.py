from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


def validate_cvc(value):
    if len(str(value)) != 3:
        raise ValidationError( ('Длина привышает максимум, максимум 3 цифры'), params={'value': value},)


def validate_number(value):
    if len(value) < 13 or len(value) > 19:
        raise ValidationError( ('Длина должна быть в диапозоне от 13 до 19'), params={'value': value},)

    if not value.isdigit():
        raise ValidationError(('Номер включает в себя только цифры'), params={'value': value}, )


def validate_price(value):
    if value < 0:
        raise ValidationError(('Сумма должна быть больше >= 0'), params={'value': value}, )


class Card(models.Model):
    WORKING = 'WORK'
    STOPPED = 'STOP'
    NOT_ACTIVATED = "NOT ACTIVATED"
    STATUC_CHOICES = [
        (WORKING, 'WORKING'),
        (STOPPED, 'STOPPED'),
        (NOT_ACTIVATED, 'NOT_ACTIVATED'),
    ]

    cvc = models.IntegerField(validators=[validate_cvc], db_index=True)  # 3 ЛЮБЫЕ ЦИФРЫ
    number_cart = models.CharField(max_length=19, unique=True, validators=[validate_number], db_index=True)  # Длина от 13 до 19 (проверить на буквы)
    date_start = models.DateTimeField(auto_now_add=True)
    date_stop = models.DateTimeField(default=timezone.now() + timedelta(days=365))
    date_use = models.DateTimeField(auto_now=True)
    amount_cash = models.IntegerField(validators=[validate_price])

    status = models.CharField(max_length=14, choices=STATUC_CHOICES, default=WORKING)

    def __str__(self):
        return self.number_cart


class Purchase(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField(validators=[validate_price])
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    statuc = models.CharField(max_length= 14, default="SUCCESS")

    def __str__(self):
        return f"Покупка: {self.title} - {self.statuc}"

    def save(self, *args, **kwargs):
        card = Card.objects.get(id=self.card.id)
        card.amount_cash -= self.price
        if card.amount_cash < 0:
            card.amount_cash += self.price
            self.statuc = "FAIL"

        card.save()

        super(Purchase, self).save(*args, **kwargs)
