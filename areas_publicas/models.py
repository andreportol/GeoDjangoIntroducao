from django.contrib.gis.db import models


class InserirAreaPublica(models.Model):
    inscant = models.CharField(verbose_name='Inscrição Imob.', max_length=11, blank=False, null=False)
    nome_invasor = models.CharField(verbose_name='Nome Invasor', max_length=100)
    rua= models.CharField(verbose_name='Rua do local', max_length=100)
    numero = models.IntegerField(verbose_name='Número')
    bairro = models.CharField(verbose_name='Bairro', max_length=100)
    nome_auditor = models.CharField(verbose_name='Nome Auditor', max_length=100)
    data = models.DateField(verbose_name='Data vistoria', auto_now_add=True)
    geom = models.PointField(srid=4674)
   
    def __str__(self):
        return self.nome_invasor

    @property
    def popup_content(self):
        popup =  f'<div><u><b>Nome Invasor:</b></u> {self.nome_invasor} </div>'
        popup += f'<div><u><b>Bairro:</b></u> {self.bairro} </div>'
        popup += f'<div><u><b>Inscrição Imob.:</b></u> {self.inscant} </div>'
        return popup
    
    class Meta:
        verbose_name = "Área Pública"
        verbose_name_plural = "Áreas Públicas"
        