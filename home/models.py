# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    cin = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    percent_gros = models.CharField(max_length=255, null=True, blank=True)
    percent_details = models.CharField(max_length=255, null=True, blank=True)
    percent_vente_occas = models.CharField(max_length=255, null=True, blank=True)
    percent_achat_occas = models.CharField(max_length=255, null=True, blank=True)
    percent_service = models.CharField(max_length=255, null=True, blank=True)
    salaire_base = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class App_Agence(models.Model):

    #__App_Agence_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

    #__App_Agence_FIELDS__END

    class Meta:
        verbose_name        = _("App_Agence")
        verbose_name_plural = _("App_Agence")


class App_Fournisseur(models.Model):

    #__App_Fournisseur_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__App_Fournisseur_FIELDS__END

    class Meta:
        verbose_name        = _("App_Fournisseur")
        verbose_name_plural = _("App_Fournisseur")


class App_Vendeur_Occas(models.Model):

    #__App_Vendeur_Occas_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    cin = models.CharField(max_length=255, null=True, blank=True)

    #__App_Vendeur_Occas_FIELDS__END

    class Meta:
        verbose_name        = _("App_Vendeur_Occas")
        verbose_name_plural = _("App_Vendeur_Occas")


class App_Client(models.Model):

    #__App_Client_FIELDS__
    cin = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    max_credit = models.CharField(max_length=255, null=True, blank=True)
    date_entree = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Client_FIELDS__END

    class Meta:
        verbose_name        = _("App_Client")
        verbose_name_plural = _("App_Client")


class App_Product(models.Model):

    #__App_Product_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    min_stock = models.IntegerField(null=True, blank=True)
    max_to_buy = models.IntegerField(null=True, blank=True)
    points_gros = models.IntegerField(null=True, blank=True)
    points_details = models.IntegerField(null=True, blank=True)
    discount_gros = models.CharField(max_length=255, null=True, blank=True)
    discount_details = models.CharField(max_length=255, null=True, blank=True)

    #__App_Product_FIELDS__END

    class Meta:
        verbose_name        = _("App_Product")
        verbose_name_plural = _("App_Product")


class App_Product_Stock(models.Model):

    #__App_Product_Stock_FIELDS__
    product = models.ForeignKey(app_product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    avg_prix_achat = models.CharField(max_length=255, null=True, blank=True)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)

    #__App_Product_Stock_FIELDS__END

    class Meta:
        verbose_name        = _("App_Product_Stock")
        verbose_name_plural = _("App_Product_Stock")


class App_Used_Product(models.Model):

    #__App_Used_Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

    #__App_Used_Product_FIELDS__END

    class Meta:
        verbose_name        = _("App_Used_Product")
        verbose_name_plural = _("App_Used_Product")


class App_Achat(models.Model):

    #__App_Achat_FIELDS__
    fournisseur = models.ForeignKey(app_fournisseur, on_delete=models.CASCADE)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    total = models.CharField(max_length=255, null=True, blank=True)
    espece = models.CharField(max_length=255, null=True, blank=True)
    cheque = models.CharField(max_length=255, null=True, blank=True)
    reste = models.CharField(max_length=255, null=True, blank=True)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)
    is_validated = models.BooleanField()

    #__App_Achat_FIELDS__END

    class Meta:
        verbose_name        = _("App_Achat")
        verbose_name_plural = _("App_Achat")


class App_Details_Achat(models.Model):

    #__App_Details_Achat_FIELDS__
    achat = models.ForeignKey(app_achat, on_delete=models.CASCADE)
    product = models.ForeignKey(app_product, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    percent_discount = models.CharField(max_length=255, null=True, blank=True)

    #__App_Details_Achat_FIELDS__END

    class Meta:
        verbose_name        = _("App_Details_Achat")
        verbose_name_plural = _("App_Details_Achat")


class App_Vente(models.Model):

    #__App_Vente_FIELDS__
    client = models.ForeignKey(app_client, on_delete=models.CASCADE)
    total = models.CharField(max_length=255, null=True, blank=True)
    espece = models.CharField(max_length=255, null=True, blank=True)
    cheque = models.CharField(max_length=255, null=True, blank=True)
    reste = models.CharField(max_length=255, null=True, blank=True)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)
    is_validated = models.BooleanField()

    #__App_Vente_FIELDS__END

    class Meta:
        verbose_name        = _("App_Vente")
        verbose_name_plural = _("App_Vente")


class App_Details_Vente(models.Model):

    #__App_Details_Vente_FIELDS__
    vente = models.ForeignKey(app_vente, on_delete=models.CASCADE)
    product = models.ForeignKey(app_product, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=True, blank=True)
    avg_prix_achat = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    percent_discount = models.CharField(max_length=255, null=True, blank=True)

    #__App_Details_Vente_FIELDS__END

    class Meta:
        verbose_name        = _("App_Details_Vente")
        verbose_name_plural = _("App_Details_Vente")


class App_Achat_Occas(models.Model):

    #__App_Achat_Occas_FIELDS__
    product = models.ForeignKey(app_used_product, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(app_vendeur_occas, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=True, blank=True)
    espece = models.CharField(max_length=255, null=True, blank=True)
    cheque = models.CharField(max_length=255, null=True, blank=True)
    reste = models.CharField(max_length=255, null=True, blank=True)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_returned = models.BooleanField()
    is_validated = models.BooleanField()

    #__App_Achat_Occas_FIELDS__END

    class Meta:
        verbose_name        = _("App_Achat_Occas")
        verbose_name_plural = _("App_Achat_Occas")


class App_Vente_Occas(models.Model):

    #__App_Vente_Occas_FIELDS__
    product = models.ForeignKey(app_used_product, on_delete=models.CASCADE)
    client = models.ForeignKey(app_client, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=True, blank=True)
    espece = models.CharField(max_length=255, null=True, blank=True)
    cheque = models.CharField(max_length=255, null=True, blank=True)
    reste = models.CharField(max_length=255, null=True, blank=True)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)
    is_validated = models.BooleanField()
    is_returned = models.BooleanField()

    #__App_Vente_Occas_FIELDS__END

    class Meta:
        verbose_name        = _("App_Vente_Occas")
        verbose_name_plural = _("App_Vente_Occas")


class App_Retour_Vente(models.Model):

    #__App_Retour_Vente_FIELDS__
    vente = models.ForeignKey(app_vente, on_delete=models.CASCADE)
    total = models.CharField(max_length=255, null=True, blank=True)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Retour_Vente_FIELDS__END

    class Meta:
        verbose_name        = _("App_Retour_Vente")
        verbose_name_plural = _("App_Retour_Vente")


class App_Details_Retour_Vente(models.Model):

    #__App_Details_Retour_Vente_FIELDS__
    retour = models.ForeignKey(app_retour_vente, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    details_vente = models.ForeignKey(app_details_vente, on_delete=models.CASCADE)

    #__App_Details_Retour_Vente_FIELDS__END

    class Meta:
        verbose_name        = _("App_Details_Retour_Vente")
        verbose_name_plural = _("App_Details_Retour_Vente")


class App_Retour_Achat(models.Model):

    #__App_Retour_Achat_FIELDS__
    achat = models.ForeignKey(app_achat, on_delete=models.CASCADE)
    total = models.CharField(max_length=255, null=True, blank=True)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Retour_Achat_FIELDS__END

    class Meta:
        verbose_name        = _("App_Retour_Achat")
        verbose_name_plural = _("App_Retour_Achat")


class App_Details_Retour_Achat(models.Model):

    #__App_Details_Retour_Achat_FIELDS__
    retour = models.ForeignKey(app_retour_achat, on_delete=models.CASCADE)
    details_achat = models.ForeignKey(app_details_achat, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    #__App_Details_Retour_Achat_FIELDS__END

    class Meta:
        verbose_name        = _("App_Details_Retour_Achat")
        verbose_name_plural = _("App_Details_Retour_Achat")


class App_Retour_Achat_Occas(models.Model):

    #__App_Retour_Achat_Occas_FIELDS__
    achat = models.ForeignKey(app_achat_occas, on_delete=models.CASCADE)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Retour_Achat_Occas_FIELDS__END

    class Meta:
        verbose_name        = _("App_Retour_Achat_Occas")
        verbose_name_plural = _("App_Retour_Achat_Occas")


class App_Retour_Vente_Occas(models.Model):

    #__App_Retour_Vente_Occas_FIELDS__
    vente = models.ForeignKey(app_vente_occas, on_delete=models.CASCADE)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Retour_Vente_Occas_FIELDS__END

    class Meta:
        verbose_name        = _("App_Retour_Vente_Occas")
        verbose_name_plural = _("App_Retour_Vente_Occas")


class App_Service(models.Model):

    #__App_Service_FIELDS__
    client = models.ForeignKey(app_client, on_delete=models.CASCADE)
    espece = models.CharField(max_length=255, null=True, blank=True)
    cheque = models.CharField(max_length=255, null=True, blank=True)
    reste = models.CharField(max_length=255, null=True, blank=True)
    agence = models.ForeignKey(app_agence, on_delete=models.CASCADE)
    details = models.CharField(max_length=255, null=True, blank=True)
    date_operation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__App_Service_FIELDS__END

    class Meta:
        verbose_name        = _("App_Service")
        verbose_name_plural = _("App_Service")



#__MODELS__END
