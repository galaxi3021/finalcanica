from django.db import models
from django import forms

# Create your models here.
class Motivo_Ingreso(models.Model):
    """Model definition for Motivo_Ingreso."""

    # TODO: Define fields here
    nombre_motivo = models.CharField(max_length=60,verbose_name="Motivo de ingreso")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Motivo_Ingreso."""

        verbose_name = 'Motivo_Ingreso'
        verbose_name_plural = 'Motivo_Ingresos'

    def __str__(self):
        return self.nombre_motivo

class Idioma(models.Model):
    """Model definition for Idioma."""

    # TODO: Define fields here
    nombre_idioma = models.CharField(max_length=60,verbose_name="Nombre del idioma")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Idioma."""

        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.nombre_idioma

class Enfermedad(models.Model):
    """Model definition for Enfermedad."""

    # TODO: Define fields here
    nombre_enfermedad = models.CharField(max_length=60,verbose_name="Nombre de la enfermedad")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Enfermedad."""

        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedads'

    def __str__(self):
        return self.nombre_enfermedad

class Nivel_Nutricion(models.Model):
    """Model definition for Nivel_Nutricion."""

    # TODO: Define fields here
    nivel = models.CharField(max_length=60,verbose_name="Nivel de nutrición")
    descripcion=models.TextField(verbose_name="Descripción")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Nivel_Nutricion."""

        verbose_name = 'Nivel_Nutricion'
        verbose_name_plural = 'Nivel_Nutricions'

    def __str__(self):
        return self.nivel

class Etnia(models.Model):
    """Model definition for Etnia."""

    # TODO: Define fields here
    nombre_etnia = models.CharField(max_length=60,verbose_name="Nombre de la etnia")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Etnia."""

        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'

    def __str__(self):
        return self.nombre_etnia

class Fuente_Estre(models.Model):
    """Model definition for Fuente_Estre."""

    # TODO: Define fields here
    nombre_fuente = models.CharField(max_length=60,verbose_name="Fuente de estrés")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Fuente_Estre."""

        verbose_name = 'Fuente_Estre'
        verbose_name_plural = 'Fuente_Estres'

    def __str__(self):
        return self.nombre_fuente

class Relacion_Familia(models.Model):
    """Model definition for Relacion_Familia."""

    # TODO: Define fields here
    tipo_relacion = models.CharField(max_length=60,verbose_name="Tipo de relación familiar")

    class Meta:
        """Meta definition for Relacion_Familia."""

        verbose_name = 'Relacion_Familia'
        verbose_name_plural = 'Relacion_Familias'

    def __str__(self):
        return self.tipo_relacion

#################### Modelos para el registro biopsicosocial #############
class NNA(models.Model):
    """Model definition for NNA."""

    # TODO: Define fields here
    SEXO=[
        ("M","Masculino"),
        ("F","Femenino"),
    ]
    EDUCACION=[
        ("Pr","Pre-Primario"),
        ("P","Primario"),
        ("Ba","Básico"),
        ("D","Diversificado"),
        ("Na","Ninguno"),
    ]
    JUZGADO=[
         ("Ay","Ayutla"),
         ("Sm","San Marcos"),
         ("Ca","Catarina"),
         ("Cm","Comitancillo"),
         ("Ct","Concepción Tutuapa"),
         ("Eq","El Quetzal"),
         ("Et","El Tumbador"),
         ("Ep","Esquipulas Palo Gordo"),  
         ("Ix","Ixchiguan"),
         ("Lb","La Blanca"),
         ("Lr","La Reforma"), 
         ("M","Malacatán"), 
         ("Np","Nuevo Progreso"),
         ("O","Ocós"),  
         ("P","Pajapita"),
         ("R","Río Blanco"),  
         ("Sac","San Antornio Sac."), 
         ("Scc","San Cristóbal Cucho"), 
         ("Sr","San José el Rodeo"),
         ("So","San José Ojetenam"),  
         ("Sl","San Lorenzo"),
         ("Sx","San Miguel Ixtahuacán"),  
         ("Sjr","San José el Rodeo"), 
         ("Sp","San Pablo"),
         ("Spc","San Pedro Sac."),
         ("Srp","San Rafael pie de la Cuesta"),
         ("S","Sibinal"),
         ("Si","Sipacapa"), 
         ("T","Tacaná"),
         ("Tj","Tajumulco"),
         ("Tja","Tejutla"), 
    ]
    OFICIAL=[
        ("fr","1ro"),
        ("sd","2do"),
        ("tr","3ro"),
        ("fr","4to"),
        ("N","Ninguno"),

    ]
    fecha_evaluacion = models.DateField(verbose_name="Fecha de evaluación Biopsicosocial")
    nombre_nino = models.CharField(max_length=60,verbose_name="Nombres del niño")
    apellido_nino = models.CharField(max_length=60,verbose_name="Apellidos del niño")
    no_expediente=models.IntegerField(verbose_name="Número de expediente")
    juzgado_refiere=models.CharField(max_length=4,choices=JUZGADO,blank=True,null=True,verbose_name="Juzgado que refiere al niño")
    oficial=models.CharField(max_length=4,choices=OFICIAL,verbose_name="Oficial",blank=True,default=True)
    image = models.ImageField(upload_to="doc",verbose_name="Fotografía del niño")
    cui = models.CharField(max_length=60,blank=True,null=True,verbose_name="CUI")
    certificado_nacimiento=models.FileField(upload_to="doc",verbose_name="Certificado de nacimiento (Archivo .pdf)")
    sexo = models.CharField(max_length=3,choices=SEXO,verbose_name="Sexo")
    grado_educativo=models.CharField(max_length=30,choices=EDUCACION,null=True,blank=True,verbose_name="Nivel educativo")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    lugar_nacimiento = models.CharField(max_length=60,verbose_name="Lugar de nacimiento")
    lugar_residencia = models.CharField(max_length=60,verbose_name="Lugar de residencia")
    motivo_ingreso=models.ForeignKey(Motivo_Ingreso,on_delete=models.PROTECT)
    descripcion_motivo=models.TextField(verbose_name="Descripción del motivo de ingreso")
    ocupacion = models.CharField(max_length=60,null=True,blank=True,verbose_name="Ocupación")
    religion = models.CharField(max_length=30,null=True,blank=True,verbose_name="Religión")
    idioma=models.ForeignKey(Idioma,on_delete=models.PROTECT)
    etnia=models.ForeignKey(Etnia,on_delete=models.PROTECT)
    nombre_madre = models.CharField(max_length=100,verbose_name="Nombre completo de la madre")
    nombre_padre = models.CharField(max_length=100,verbose_name="Nombre completo del padre")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso a CANICA")
    orden_ingreso=models.FileField(upload_to="doc",verbose_name="Orden de ingreso (Archivo .pdf)",)
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for NNA."""

        verbose_name = 'NNA'
        verbose_name_plural = 'NNAs'

    def __str__(self):
        return self.nombre_nino+" "+self.apellido_nino
    
    def get_absolute_url(self):
        return u'/nino/%d' % self.id 



class Area_Dental(models.Model):
    """Model definition for Area_Dental."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.PROTECT)
    diagnostico = models.TextField(verbose_name="Dignóstico",blank=True,null=True)
    intervencion=models.TextField(verbose_name="Intervención médica",blank=True,null=True)
    proxima_cita=models.DateField(verbose_name="Próxima cita",)
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Area_Dental."""

        verbose_name = 'Area_Dental'
        verbose_name_plural = 'Area_Dentals'

    def __str__(self):
       return str(self.nino)

class Area_Social(models.Model):    
    """Model definition for Area_Social."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.PROTECT)
    rol_familiar=models.TextField(null=True,blank=True,verbose_name="Rol familiar")
    relacion_familiar=models.ForeignKey(Relacion_Familia,on_delete=models.PROTECT)
    fuente_estres=models.ForeignKey(Fuente_Estre,on_delete=models.PROTECT)
    descripcion=models.TextField(verbose_name="Descripción de la fuente de estrés",blank=True,null=True)
    visitas_autorizadas=models.BooleanField(verbose_name="Visitas Autorizadas")
    recurso_familiar=models.CharField(max_length=60,null=True,blank=True,verbose_name="Recurso familiar")


    class Meta:
        """Meta definition for Area_Social."""

        verbose_name = 'Area_Social'
        verbose_name_plural = 'Area_Socials'

    def __str__(self):
        return str(self.nino)

class Area_Psicologica(models.Model):
    """Model definition for Area_Psicologica."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.CASCADE)
    estado_emocional=models.TextField(null=True,verbose_name="Estado emocional",blank=True)
    aspecto_clinico=models.TextField(verbose_name="Aspecto clínico")
    percepcion_situacion_desproteccion=models.BooleanField(verbose_name="Percepción de la situación de desprotección")
    percepcion_calidad_vida=models.BooleanField(verbose_name="Percepción de la calidad de vida en su hogar")
    percepcion_temores_actuales=models.TextField(null=True,verbose_name="Percepción de temores actuales",blank=True)
    percepcion_temores_futuros=models.TextField(null=True,verbose_name="Percepción de temores futuros",blank=True)
    enfermedad=models.ForeignKey(Enfermedad,on_delete=models.CASCADE)
    descripcion=models.TextField(verbose_name="Descripcion de la enfermedad psicológica",blank=True,null=True)

    class Meta:
        """Meta definition for Area_Psicologica."""

        verbose_name = 'Area_Psicologica'
        verbose_name_plural = 'Area_Psicologicas'

    def __str__(self):
        return str(self.nino)
        
class Area_Medica(models.Model):
    """Model definition for Area_Medica."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.CASCADE)
    peso=models.IntegerField(verbose_name="Peso del niño (Libras)")
    altura=models.FloatField(verbose_name="Altura del niño (Metros)")
    presencia_piojos=models.BooleanField(verbose_name="Presencia de piojos")
    presencia_acaros=models.BooleanField(verbose_name="Presencia de acaros")
    programa_vacunacion=models.BooleanField(verbose_name="Programa de vacunación")
    examen_sangre=models.BooleanField(verbose_name="Examen de sangre")
    examne_orina=models.BooleanField(verbose_name="Examen de orina")
    estado_piel=models.TextField(verbose_name="Estado de la piel")
    nivel_nutricion=models.ForeignKey(Nivel_Nutricion,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Area_Medica."""

        verbose_name = 'Area_Medica'
        verbose_name_plural = 'Area_Medicas'

    def __str__(self):
        return str(self.nino)


       






        
        

       
        
        
        



        


