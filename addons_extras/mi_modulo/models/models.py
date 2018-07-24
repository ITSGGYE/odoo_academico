# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ParteVehiculo(models.Model):
    _name = 'test.vehiculo_partes'

    name = fields.Char(string='Nombre')
    fecha_fab = fields.Date(string='Fecha de Fabricación')


class DetalleVehiculo(models.Model):
    _name = 'test.vehiculo_detalle'


    id_vehiculo = fields.Many2one('test.vehiculo')

    parte = fields.Many2one('test.vehiculo_partes', string='Nombre de Parte')
    serie = fields.Char('Serie')
    estado = fields.Boolean('Estado')
    responsable = fields.Many2one('res.partner')


class Marca(models.Model):
    _name = 'test.vehiculo_marca'

    name = fields.Char(string='Nombre')
    origen = fields.Char(string='Oigen')


class Vehiculo(models.Model):
     _name = 'test.vehiculo'

     color = fields.Selection([('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Negro', 'Negro')], string="Color")
     marca = fields.Many2one('test.vehiculo_marca', string='Marca')
     marca_ids = fields.Many2many(
         'test.vehiculo_marca',  # hace referencia a la clase externa que tiene el Many2One
         column1='id',  # id que se encuentra en la misma clase
         column2='marca_ids',  # hace referencia al mismo campo el id del atributo
         string='Marcas'
     )

     detalle_line = fields.One2many('test.vehiculo_detalle', 'id_vehiculo', string='Detalle vehículo')