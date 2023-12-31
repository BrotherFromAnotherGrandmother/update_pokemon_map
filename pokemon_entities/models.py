from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название на русском')
    title_en = models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на английском')
    title_jp = models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на японском')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='next_evolutions', verbose_name='Предыдущая эволюция')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="entities", verbose_name='Вид покемона')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появится/появится')
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет/исчез')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return self.pokemon.title, f'Координаты {self.lat}:{self.lon}'
