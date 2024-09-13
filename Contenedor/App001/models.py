from django.db import models

# Create your models here.
class AutorDb(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento",null=False,blank=False)
    profesion =models.CharField(verbose_name="Profesion",max_length=50)
    nacionalidad = models.CharField(verbose_name="Nacionalidad",max_length=50)
    
    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self) -> str:
        return self.nombre
    
    
class FraseDb(models.Model):
    cita = models.TextField(verbose_name="Cita",max_length=500)
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
