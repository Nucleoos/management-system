# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields

class res_company(models.Model):
    _inherit = "res.company"

    risk_computation_id = fields.Many2one(
        'mgmtsystem.hazard.risk.computation',
        'Risk Computation',
        required=True,
        default=_get_formula
    )

    def _get_formula(self):
        ids = self.env['mgmtsystem.hazard.risk.computation'].search(
            [('name', '=', 'A * B * C')]
        )
        return ids and ids[0] or False
