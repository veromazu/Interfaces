from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	
	ROLES = (
		('Estudiante', 'Estudiante'),
		('Profesor', 'Profesor'),
		('Representante','Representante'),
	)

	tipo_usuario = models.CharField('Tipo de usuario',max_length=50,null=True,choices=ROLES)
	user = models.OneToOneField(
		User,
		on_delete = models.CASCADE,
		default='userprofile'
	)

	def __str__(self):
		return self.user.email