from django.db import models


class Worker(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    birth_day = models.DateField("День рождения")
    email = models.EmailField("Почта")
    photo = models.ImageField("Фотография")
    def __str__(self):
        return self.name + " " + self.lastname


class Blog(models.Model):
    mark = models.CharField("Название", max_length=20, unique=True)
    text = models.CharField("Текст", max_length=500)
    def __str__(self):
        return self.mark


class CarouselImage(models.Model):
    image = models.ImageField("Картинка", upload_to='carousel')
    text = models.CharField("Подпись", max_length=100)
    position = models.IntegerField("Позиция", max_length=1, unique=True, blank=False)
    def __str__(self):
        return self.text


class Feature(models.Model):
    icon = models.CharField("Название иконки", max_length=20, default='glyphicon-remove')
    header = models.CharField("Заголовок", max_length=100, default='Вставьте заголовок')
    text = models.CharField("Текст", max_length=100)
    def __str__(self):
        return self.header


class Service(models.Model):
    icon = models.CharField("Название иконки", max_length=20, default='glyphicon-remove')
    text = models.CharField("Текст", max_length=100)
    def __str__(self):
        return self.text


class Partner(models.Model):
    name = models.CharField("Название", max_length=20)
    logo = models.ImageField("Логотип", max_length=100)
    url = models.URLField("Ссылка на сайт")
    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField("Наименование", max_length=30, unique=True)
    description = models.CharField("Описание", max_length=200)
    manufacturer = models.CharField("Производитель", max_length=30)
    price = models.IntegerField("Цена", max_length=10)
    image = models.ImageField("Изображение")
    count = models.IntegerField("Количество", max_length=2)
    def __str__(self):
        return self.name