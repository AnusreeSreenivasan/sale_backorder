from odoo import models,fields,api
from odoo.tools.float_utils import float_compare


class ResPartner(models.Model):
    _inherit = 'res.partner'

    create_backorder = fields.Selection(
    [('ask', 'Ask'), ('always', 'Always'), ('never', 'Never')],
        'Create Backorder', required=True, default='ask',)

