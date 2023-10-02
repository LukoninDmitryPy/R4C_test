import os

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot

OWNER_MAIL = os.getenv('OWNER_MAIL')

@receiver(post_save, sender=Robot)
def notify_customers(sender, instance, **kwargs):
    """Отправка сообщения"""
    pending_orders = Order.objects.filter(robot_serial=instance.serial)
    for order in pending_orders:
        customer_email = order.customer.email
        subject = 'Робот доступен в наличии'
        message = f'Добрый день!\n\n'
        message += f'Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\n'
        message += f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'
        send_mail(subject, message, OWNER_MAIL, [customer_email])