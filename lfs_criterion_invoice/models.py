# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.criteria.models import Criterion
import lfs.customer.utils


class InvoiceCriterion(Criterion):
    value = models.CharField(max_length=100)

    def get_operators(self):
        return [
           ["0", _(u"Is checked")],
        ]

    def get_value_type(self):
        return self.SELECT

    def get_selectable_values(self, request):
        return [
            {
                "id": 0,
                "name": "Invoice allowed",
                "selected": True,
            },
        ]

    def is_valid(self):
        customer = lfs.customer.utils.get_customer(self.request)
        if customer and customer.allow_invoice:
            return True
        return False
