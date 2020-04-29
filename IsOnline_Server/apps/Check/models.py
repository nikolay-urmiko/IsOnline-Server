import datetime
from django.db import models
from django.utils import timezone

class Ur_face(models.Model):
    ur_face_name = models.CharField('Наименование Юридического лица', max_length = 100)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'
        ordering = ('ur_face_name',)

    def __str__(self):
        return self.ur_face_name

class Checks(models.Model):
    ur_facce = models.ForeignKey(Ur_face, on_delete = 'CASKADE')
    namedot = models.CharField('название точки', max_length = 100)
    last_online = models.DateTimeField('дата последнего соединения')
    GOST_key = models.DateTimeField('дата окончания ключа ГОСТ')
    
    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        ordering = ('ur_facce', 'namedot',)
        
    def __str__(self):
        s = self.ur_facce.ur_face_name + '/' + self.namedot

        return s#"%s (%s)" % (s, ", ".join('ur_facce'))

    def was_online(self):
        return self.last_online <= (timezone.now() - datetime.timedelta(hours = 1))

    def GOST_check(self):
        return self.GOST_key <= timezone.now()