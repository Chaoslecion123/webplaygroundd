from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    # el sef es equivalente a Thread.objects.all

    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)

        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update']

    objects = ThreadManager()

def messages_changed(sender, **kwargs):  # es una señal

    instance = kwargs.pop("instance", None) # al hilo al que estamos intantando añadir los mensajes7
    action = kwargs.pop("action", None)  # detecta el pre add o el post add , el pre add es el momento justo antes de añadir el mensaje y el post add es el momento justo despues de añadir los mensajes
    pk_set = kwargs.pop("pk_set", None)  # identificadores de los mensajes que estan en el many to many
    print(instance, action, pk_set)

    false_pk_set= set()
    if action in "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)

            if msg.user not in instance.users.all():
                print("Ups , ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)

    # Buscar los mensajes de false_pk_set que si estan en pk_set y lo borramos  de pk_set
    pk_set.difference_update(false_pk_set)


    # forzar la actualizacion haciendo save

    instance.save()


m2m_changed.connect(messages_changed, sender=Thread.messages.through)