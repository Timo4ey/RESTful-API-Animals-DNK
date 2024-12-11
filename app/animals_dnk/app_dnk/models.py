from django.db import models

# Create your models here.


class GeneticTests(models.Model):
    animal_name = models.CharField(
        max_length=150,
        null=False,
    )  # String Имя животного
    # String Вид (ĸорова, свинья и т.д.)
    species = models.CharField(
        max_length=60,
        null=False,
    )
    test_date = models.DateField(null=True)  # Date Дата проведения теста
    milk_yield = models.FloatField(null=True)  # Float Продуĸтивность
    # String Состояние здоровья ("good" или "poor")
    health_status = models.CharField(
        null=False, max_length=10, choices=(("good", "good"), ("poor", "poor"))
    )
    # Timestamp Дата создания записи
    created_at = models.DateTimeField(auto_now_add=True)
