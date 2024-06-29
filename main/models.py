from django.db import models
from ckeditor.fields import RichTextField
class Cover(models.Model):
    mini_txt=models.CharField('Small title',max_length=200)
    name=models.TextField('Title')
    txt=models.TextField('Text')
    img=models.ImageField('Foto:530x300',upload_to='archive')
    def __str__(self):
        return self.mini_txt
    class Meta:
        verbose_name='Cover'
        verbose_name_plural='Cover'