from django.contrib.gis.db import models


class AvaliacaoImob(models.Model):
    objectid = models.BigIntegerField(blank=True, null=True)
    informante = models.CharField(max_length=50,blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    parcelamen = models.CharField(max_length=50,blank=True, null=True)
    testada = models.FloatField(blank=True, null=True)
    areaterren = models.FloatField(blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)
    quadra = models.CharField(max_length=50,blank=True, null=True)
    lote = models.CharField(max_length=50,blank=True, null=True)
    endereco = models.CharField(max_length=50,blank=True, null=True)
    inscant = models.CharField(max_length=11,blank=True, null=True)
    bairro = models.CharField(max_length=30,blank=True, null=True)
    regiao = models.CharField(max_length=20,blank=True, null=True)
    observacao = models.CharField(max_length=50,blank=True, null=True)
    pavimentac = models.CharField(max_length=1,blank=True, null=True)
    n_testadas = models.BigIntegerField(blank=True, null=True)
    preco_un = models.FloatField(blank=True, null=True)
    contato_in = models.CharField(max_length=50,blank=True, null=True)
    formatoter = models.CharField(max_length=10,blank=True, null=True)
    topografia = models.BigIntegerField(blank=True, null=True)
    fat_fonte = models.CharField(max_length=1,blank=True, null=True)
    indice = models.FloatField(blank=True, null=True)
    created_us = models.CharField(max_length=254,blank=True, null=True)
    created_da = models.DateField(blank=True, null=True)
    last_edite = models.CharField(max_length=254,blank=True, null=True)
    last_edi_1 = models.DateField(blank=True, null=True)
    geom = models.PointField(srid=31981,blank=True, null=True)

    class Meta:
        verbose_name= "Avaliação Imobiliária"
        verbose_name_plural = "Avaliações Imobiliárias"
        #ordering=[-1] # transforma para ordem decrescente
        ordering = ["-objectid"] # (-) ordena de forma decrescent
        
    
        def __str__(self):
            return self.inscant