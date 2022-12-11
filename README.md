# Cards
Cloning the repository
--> Clone the repository using the command below :

git clone https://github.com/leraks/Cards.git


--> Create a virtual environment :

# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
--> Activate the virtual environment :

envname\scripts\activate
--> Install the requirements :

pip install -r requirements.txt


# Running the App
--> To run the App, we use :

python manage.py runserver <br>
⚠ Then, the development server will be started at http://127.0.0.1:8000/

# Task :
Web application for managing a database of bonus cards (loyalty cards, credit cards, etc. I have met many variations). List of fields: card series, card number, card issue date, end date of card activity, date of use, amount, card status (not activated/activated/expired).

The functionality of the application is a list of cards with fields: series, number, release date, end date of activity, status search for the same fields viewing the profile of the card with the purchase history of it activating/deactivating the card deleting the card

Implement a card generator, indicating the series and number of generated cards, as well as the "end date of activity" with the values "1 year", "6 months" and "1 month".

# Task Ru

Веб-приложение для управления базой данных бонусных карт (карт лояльности, кредитный карт и т.д. Я встречал много вариаций).
Список полей: серия карты, номер карты, дата выпуска карты, дата окончания активности карты, дата использования, сумма, статус карты (не активирована/активирована/просрочена).

Функционал приложения
список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус поиск по этим же полям
просмотр профиля карты с историей покупок по ней
активация/деактивация карты
удаление карты

Реализовать генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц". 
