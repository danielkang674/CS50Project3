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

class PizzaStyle(models.Model):
  style = models.CharField(max_length=10)

  def __str__(self):
    return f"{self.style}"

class PizzaType(models.Model):
  type = models.CharField(max_length=10)

  def __str__(self):
    return f"{self.type}"

class Pizza(models.Model):
  style = models.ForeignKey(PizzaStyle, on_delete=models.CASCADE, related_name="pizzaStyle")
  type = models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name="pizzaType")
  size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizzaSize")
  toppings = models.ManyToManyField(PizzaTopping, blank=True, related_name="toppings")

  def __str__(self):
    # pylint: disable=E1101
    ptoppings = ""
    for topp in self.toppings.all().values():
      ptoppings += " " + topp["topping"]
    return f"{self.id} - {self.size} {self.style} {self.type} with {ptoppings}"

class SubTopping(models.Model):
  topping = models.CharField(max_length=25)

  def __str__(self):
    return f"{self.topping}"

class SubType(models.Model):
  type = models.CharField(max_length=40)

  def __str__(self):
    return f"{self.type}"

class Sub(models.Model):
  type = models.ForeignKey(SubType, on_delete=models.CASCADE, related_name="subType")
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

class PlatterType(models.Model):
  type = models.CharField(max_length=35)

  def __str__(self):
    return f"{self.type}"

class Platter(models.Model):
  type = models.ForeignKey(PlatterType, on_delete=models.CASCADE, related_name="platterType")
  size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="platterSize")

  def __str__(self):
    # pylint: disable=E1101
    return f"{self.id} - {self.size} {self.type}"