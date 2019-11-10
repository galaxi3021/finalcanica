from django.db import models
from nino.models import NNA
# Create your models here.

class Evaluacion_Medica(models.Model):
    """Model definition for Evaluacion_Medica."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.CASCADE)
    DESNUTRICION=[
        ("S","Si"),
        ("N","No")
    ]
    edad=models.IntegerField(verbose_name="Edad del niño")
    peso=models.IntegerField(verbose_name="Peso del niño (Libras)")
    desnutricion=models.CharField(max_length=3,choices=DESNUTRICION,verbose_name="Desnutrición")
    altura=models.FloatField(verbose_name="Altura del niño (Metros)")
    circunferencia_brazo_derecho=models.FloatField(verbose_name="Circunferencia del brazo derecho (Centímetros)")
    circunferencia_brazo_izquierdo=models.FloatField(verbose_name="Circunferencia del brazo izquierdo (Centímetros)")
    circunferencia_abdominal=models.FloatField(verbose_name="Circunferencia abdominal (Centímetros)")
    imc=models.FloatField(verbose_name="I.M.C (Indice de masa corporal)",blank=True,null=True)
    antecendentes_medicos=models.TextField("Antecedentes médicos de importancia",blank=True,null=True)
    padece_alergias=models.CharField(max_length=30,verbose_name="Padece de alergias, cual",null=True,blank=True)
    sintomas=models.TextField(verbose_name="Síntomas",null=True,blank=True)
    impresion_clinica=models.TextField(verbose_name="Impresión clínica")
    recomendacion=models.TextField(verbose_name="Recomendaciones",null=True,blank=True)
    tratamiento=models.TextField(verbose_name="Tratamiento",null=True,blank=True)
    proxima_cita=models.DateField(verbose_name="Próxima cita")
    observaciones=models.TextField(verbose_name="Observaciones",null=True,blank=True)
    medico=models.CharField(max_length=40,verbose_name="Doctor encargado de la evaluación")
   
    class Meta:
        """Meta definition for Evaluacion_Medica."""

        verbose_name = 'Evaluacion_Medica'
        verbose_name_plural = 'Evaluacion_Medicas'

    def __str__(self):
        return str(self.nino)