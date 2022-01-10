from django.db import models


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