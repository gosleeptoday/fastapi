from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class CardsModel(models.Model):
    num = fields.CharField(max_length=16)
    month = fields.CharField(max_length=2)
    year = fields.CharField(max_length=4)
    cvv = fields.CharField(max_length=3)
    holder_name = fields.CharField(max_length=100)

    class Meta:
        table = "Cards"

CardsPydantic = pydantic_model_creator(CardsModel, exclude=('id',))