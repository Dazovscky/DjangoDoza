from django.db import models


def case_upload_location(instance, filename):
    file_name = filename.lower().replace(" ", "-")
    return "photos/{}".format(file_name)


class Case(models.Model):
    name = models.CharField('Автор', max_length=250)
    number_folder = models.CharField('Инициалы', max_length=250)

    def __str__(self):
        return "{}  {}".format( self.name, self.number_folder)


class CaseFile(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE) # When a Case is deleted, upload models are also deleted
    file = models.ImageField(upload_to=case_upload_location, null = True, blank = True)

    def __str__(self):
        return "{}  {}".format( self.case, self.file)







