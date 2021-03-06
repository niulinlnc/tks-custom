# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    comm_history_ids = fields.One2many(
        comodel_name='project.comm.history',
        inverse_name='task_id',
        string='Communication History'
    )
