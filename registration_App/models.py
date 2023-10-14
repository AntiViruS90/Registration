from django.db import models as m


class User(m.Model):
    username = m.CharField(max_length=40)
    first_name = m.CharField(max_length=40)
    last_name = m.CharField(max_length=40)
    email = m.CharField(max_length=40)

    def __str__(self):
        return self.username