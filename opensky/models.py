from django.db import models

class Worker(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    birth_day = models.DateField("День рождения")
    email = models.EmailField("Почта")
    photo = models.ImageField("Фотография")
    phone = models.CharField("Телефон", max_length=100)
    def __str__(self):
        return self.name + " " + self.last_name


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
    image = models.ImageField("Изображение")
    header = models.CharField("Заголовок", max_length=100)
    text = models.CharField("Описание", max_length=10000)
    def __str__(self):
        return self.header


class Service(models.Model):
    image = models.ImageField("Изображение")
    header = models.CharField("Заголовок", max_length=100)
    text = models.CharField("Описание", max_length=100)
    def __str__(self):
        return self.header


class Partner(models.Model):
    name = models.CharField("Название", max_length=20, unique=True)
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


class Office(models.Model):
    address = models.CharField("Контактный адресс", max_length=50)
    email = models.EmailField("Контактная почта", max_length=50)
    phone_str = models.CharField("Контактный телефон (через ;)", max_length=100)
    latitude = models.CharField("Широта", max_length=10)
    longitude = models.CharField("Долгота", max_length=10)
    def phone(self):
        return self.phone_str.split(';')


class SocialWidget(models.Model):
    SOCIAL_CHOICES = (
        ('vk', 'Вконтакте'),
        ('ok', 'Одноклассники'),
        ('fb', 'Facebook'),
        ('tw', 'Twitter'),
        ('li', 'LinkedIn'),
        ('yt', 'YouTube'),
        ('in', 'Instagram'),
    )
    name = models.CharField("Название", max_length=2, choices=SOCIAL_CHOICES)
    url = models.URLField("Ссылка", blank=True)
    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField("Название", max_length=30)
    price = models.IntegerField("Цена", max_length=6)
    def __str__(self):
        return self.name