from django.db import models





class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre de la Categoría')
  slug = models.SlugField(unique=True, max_length=100)


  def __str__(self):
    return self.name


class Product(models.Model):
  category = models.ForeignKey(
      Category,
      on_delete=models.CASCADE,
      verbose_name='Categoría',
      related_name='products',
  )
  title = models.CharField(max_length=200, verbose_name='Título del Producto')
  slug = models.SlugField(unique=True, max_length=200)
  description = models.TextField(verbose_name='Descripción')
  price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name='Precio'
  )
  image = models.ImageField(
      upload_to='products/images/', verbose_name='Imagen de Portada'
  )
  digital_file = models.FileField(
      upload_to='products/downloads/',
      blank=True,
      null=True,
      verbose_name='Archivo Descargable (PDF)',
  )
  is_active = models.BooleanField(default=True, verbose_name='Disponible')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title