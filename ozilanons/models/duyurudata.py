from django.db import models
import os
from django.conf import settings


# Create your models here.
def mp3_path():
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT1 = os.path.abspath(os.path.dirname(settings_dir))
    PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_ROOT1))
    MP3FILES_FOLDER = os.path.join(PROJECT_ROOT, 'mp3file')
    return MP3FILES_FOLDER

class DuyuruData(models.Model):
    metin = models.CharField(verbose_name='Duyuru Metni',max_length=200, null=True)
    mp3yolu = models.FilePathField(path=mp3_path, recursive=False, verbose_name='Melodi Yolu', null=True)
    guncellendi = models.BooleanField(verbose_name='Zil Güncel', default=False)
    zilaktif = models.BooleanField(verbose_name='Zil Aktif', default=True)

    def __str__(self):
        return self.metin

    class Meta:

        db_table = 'cal_duyur'
