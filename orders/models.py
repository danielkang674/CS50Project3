from django.db import models

# Create your models here.

class Size(models.Model):
  size = models.CharField(max_length=6)

  def __str__(self):
    return f"{self.size}"

class PizzaTopping(models.Model):
  topping = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.topping}"

class Pizza(models.Model):
  style = models.CharField(max_length=10)
  type = models.CharField(max_length=12)
  size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizzaSize")
  toppings = models.ManyToManyField(PizzaTopping, blank=True, related_name="toppings")

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.size} {self.style} {self.type} with {self.toppings}"

class SubTopping(models.Model):
  topping = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.topping}"

class Sub(models.Model):
  type = models.CharField(max_length=40)
  size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="subSize")
  toppings = models.ManyToManyField(SubTopping, blank=True, related_name="toppings")

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.size} {self.type} with {self.toppings}"

class Pasta(models.Model):
  type = models.CharField(max_length=35)

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.type}"

class Salad(models.Model):
  type = models.CharField(max_length=35)

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.type}"

class Platter(models.Model):
  type = models.CharField(max_length=35)
  size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="platterSize")

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.size} {self.type}"