from django.db import models


class UserScripts(models.Model):
    positions = (
        ('head_bottom', 'head bottom'),
        ('body_top', 'body top'),
        ('body_bottom', 'body bottom')
    )
    name = models.CharField(max_length=50, db_index=True, verbose_name='Name')
    position = models.CharField(max_length=15, choices=positions, default='head', verbose_name='Position')
    script = models.TextField(verbose_name='Script')
    active = models.BooleanField(default=False, db_index=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'
        ordering = ('name',)

    def __str__(self):
        return self.name
