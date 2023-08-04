from django.core.mail import send_mail


HOST = '127.0.0.1:8000'

from django.core.mail import message
def send_confirmation_email(user, code):
    link = f'http://{HOST}/account/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке ниже: '
        f'\n{link}'
        f'\nСсылка работает один раз!',
        'kadyrovalazat1985@gmail.com',
        [user],
        fail_silently=False,
    )