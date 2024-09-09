from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    # Modifying the instance within the signal handler
    instance.name = "Modified"
    instance.save()  # Save the modified instance within the same transaction

# Creating an instance of MyModel
obj = MyModel.objects.create(name="Original")

print("Name before save:", obj.name)

# Starting a new transaction explicitly
with transaction.atomic():
    obj.name = "Updated"
    obj.save()  # Save the modified object

print("Name after save:", obj.name)