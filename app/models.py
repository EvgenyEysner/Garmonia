from django.db import models
from django.core.validators import RegexValidator


class Swiper(models.Model):
    """
    Swiper
    """
    title = models.CharField('überschrift', max_length=128, help_text='maximal 128 Zeichen')
    image = models.ImageField('bild', upload_to='images/swiper', help_text='maximale Bildauflösung 1920x717')
    text = models.TextField('text eingeben', max_length=256, help_text='maximale Länge 512 Zeichen')

    class Meta:
        verbose_name = 'swiper'

    def __str__(self):
        return self.title


class Carousel(models.Model):
    """
    Beauty experts
    """
    name = models.CharField('überschrift', max_length=128, help_text='maximal 128 Zeichen', null=True, blank=True)
    image = models.ImageField('bild', upload_to='images/swiper', help_text='maximale Bildauflösung 370x370')


class Contact(models.Model):
    """
    Create contact request
    """
    first_name = models.CharField('name', max_length=120)
    last_name = models.CharField('name', max_length=120)
    email = models.EmailField('email', max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)  # Validator soll eine Liste sein
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField('nachricht', help_text='max. 500 Zeichen')

    class Meta:
        verbose_name = 'kontaktanfrage'
        verbose_name_plural = 'kontaktanfragen'
        ordering = ['-created']

    def __str__(self):
        return f'{self.last_name}: {self.message} {self.created}'