from django.db import models
from embed_video.fields import EmbedVideoField
from unidecode import unidecode
from django.urls import reverse
from model_utils.managers import InheritanceManager
from embed_video.admin import AdminVideoMixin
from embed_video.fields import EmbedVideoField


class CoursePage(models.Model):
    name = models.CharField('Название курса', max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")

    general_info = models.TextField('Общая информация')

    def create_slug(self):  # self-written function for better generating slugs
        self.slug = unidecode(self.name).replace(' ', '_')
        copies = CoursePage.objects.all().filter(slug__startswith=self.slug)
        if copies:
            self.slug += str(len(copies) + 1)

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})


class MaterialMaster(InheritanceManager):
    pass


class Material(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    objects = MaterialMaster()

    # master = models.ForeignKey(MaterialMaster)

    @property
    def view(self):
        pass

    def concretize(self):
        "return inherited version of self"
        return Material.objects.get_subclass(id=self.id)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Url(Material):
    address = models.URLField(max_length=200)

    @property
    def view(self):
        return

            # self.address


class File(Material):
    file_material = models.FileField(upload_to='files/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    @property
    def view(self):
        return "Dummy place for a file"


class Video(Material):
    video_material = EmbedVideoField()

    # class Meta:
    #     verbose_name_plural = "Video"

    def __str__(self):
        return str(self.name) if self.name else " "

    @property
    def view(self):
        return self.video_material


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    course = models.ForeignKey(CoursePage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ((str(self.course) + ': ') if self.course else '') + self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Group(models.Model):
    name = models.CharField(max_length=30)
    subgroups = models.ManyToManyField('self')
    parent_grop = models.ForeignKey('self', on_delete=models.CASCADE)
    courses = models.ManyToManyField(CoursePage)
