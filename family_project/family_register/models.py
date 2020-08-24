from django.db import models
# from address.models import AddressField

# Create your models here.

# class Address(models.Model):
#     #parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=100)
# #     def __str__(self):
# #         return '%s %s %s %s' % (self.street, self.city, self.state, self.zip_code)


# class Parent(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     # address = AddressField(on_delete=models.CASCADE)
#     # def __str__(self):
#     #     return '%s %s %s' % (self.first_name, self.last_name, self.address)

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '%s %s %s %s' % (self.street, self.city, self.state, self.zip)

class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Address', null=True, blank=True)
    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.address)

    
class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        verbose_name = 'Child'
        verbose_name_plural = 'Children'

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.parent)


    
