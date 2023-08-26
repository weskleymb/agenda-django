from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length = 100, null = False, blank = False)
    fone = models.CharField(max_length = 20, null = False, blank = False)

    def __str__(self):
        return f"Contato[{self.nome}, {self.fone}]"
