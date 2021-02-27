# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Taco(models.Model):
    id = models.TextField(db_column="id", primary_key=True, blank=True)  # This field type is a guess.
    nomedoalimento = models.TextField(db_column='NomedoAlimento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    umidade_field = models.TextField(db_column='Umidade(%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    energia_kcal_field = models.TextField(db_column='Energia(kcal)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    energia_kj_field = models.TextField(db_column='Energia(kJ)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    proteina_g_field = models.TextField(db_column='Proteina(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    lipideos_g_field = models.TextField(db_column='Lipideos(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    colesterol_mg_field = models.TextField(db_column='Colesterol(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    carboidrato_g_field = models.TextField(db_column='Carboidrato(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    fibraalimentar_g_field = models.TextField(db_column='FibraAlimentar(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    cinzas_g_field = models.TextField(db_column='Cinzas(g)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    calcio_mg_field = models.TextField(db_column='Calcio(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    magnesio_mg_field = models.TextField(db_column='Magnesio(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    manganes_mg_field = models.TextField(db_column='Manganes(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    fosforo_mg_field = models.TextField(db_column='Fosforo(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    ferro_mg_field = models.TextField(db_column='Ferro(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    sodio_mg_field = models.TextField(db_column='Sodio(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    potassio_mg_field = models.TextField(db_column='Potassio(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    cobre_mg_field = models.TextField(db_column='Cobre(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    zinco_mg_field = models.TextField(db_column='Zinco(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    retinol_mg_field = models.TextField(db_column='Retinol(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    re_mcg_field = models.TextField(db_column='RE(mcg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    rae_mcg_field = models.TextField(db_column='RAE(mcg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    tiamina_mg_field = models.TextField(db_column='Tiamina(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    riboflavina_mg_field = models.TextField(db_column='Riboflavina(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    piridoxina_mg_field = models.TextField(db_column='Piridoxina(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    niacina_mg_field = models.TextField(db_column='Niacina(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    vitaminac_mg_field = models.TextField(db_column='VitaminaC(mg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Taco_4a_edicao_2011'
