
from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    
    validated_id = fields.Many2one(
        string='Validated By',
        comodel_name='res.users',
        required=False
    )
    
