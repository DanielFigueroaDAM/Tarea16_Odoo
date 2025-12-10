# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class PartnerChineseStats(models.Model):
    _inherit = 'res.partner'

    f_nac = fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string="Edad", readonly=True, compute='_calcular_edad', store=True)
    signo_chino = fields.Char(string="Signo Chino", readonly=True, compute='_calcular_chinada', store=True)

    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                today = date.today()
                record.edad = today.year - record.f_nac.year - (
                    (today.month, today.day) < (record.f_nac.month, record.f_nac.day)
                )
            else:
                record.edad = 0

    @api.depends('f_nac')
    def _calcular_chinada(self):
        signos = [
            "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
            "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
        ]
        for record in self:
            if record.f_nac:
                year = record.f_nac.year
                # El ciclo chino es de 12 años, empezando en 1900 con la Rata
                index = (year - 1900) % 12
                record.signo_chino = signos[index]
            else:
                record.signo_chino = "Sin signo"

