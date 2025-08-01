from django.db import models

class Autor(models.Model):
    nome = models.CharField( max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Autores"

class Postagem(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=80)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data = models.CharField(max_length=50)
    texto = models.CharField(max_length=180)

    class Meta:
        verbose_name_plural = "Postagens"

    def __str__(self):
        return f"{self.titulo} - {self.data}"

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    copyright = models.CharField(max_length=50)
