# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    formacion_ids = fields.One2many('hr.employee.formacion', 'formacion_id', string="Formación")
    capacitacion_ids = fields.One2many('hr.employee.capacitacion', 'capacitacion_id', string="Capacitación")
    experiencia_ids = fields.One2many('hr.employee.experiencia', 'experiencia_id', string="Experiencia")
    logro_ids = fields.One2many('hr.employee.logro', 'logro_id', string="Logros")

    discapacidad = fields.Boolean(string="Tienes algún tipo de discapacidad",  required=True, )
    sustituto = fields.Boolean(string="Es sustituto", required=True, )
    porcentaje_discapacidad = fields.Integer(string="Porcentaje de discapacidad :",  )
    carnet_discapacidad = fields.Char(string="Carnet de discapacidad:", )
    parentesco = fields.Many2one('hr.employee.parentesco', string="Parentesco")
    cedula_familiar = fields.Char(string="Cédula persona con discapacidad:", )
    nombre_familiar = fields.Char(string="Nombre persona con discapacidad:", )



    etnia_ids = fields.Many2one('hr.employee.etnia', string="Etnia")
    ad_carnet_ids = fields.Many2many(comodel_name="ir.attachment", relation="carnet_id", string='Adjuntar Carnet', )
    ad_cedula_ids = fields.Many2many(comodel_name="ir.attachment", relation="cedula_id", string='Adjuntar Cédula', required=True, )
    ad_papeleta_ids = fields.Many2many(comodel_name="ir.attachment", relation="papeleta_id", string='Adjuntar Papeleta',required=True,  )
    ad_cuenta_ids = fields.Many2many(comodel_name="ir.attachment", relation="cuenta_id", string='Adjuntar Cuenta',required=True,  )

    escalafon = fields.Many2one('hr.employee.escalafon', string="Escalafón RMU",)
    fecha_ingreso = fields.Date(string="Fecha de Ingreso:", )
    relacion = fields.Boolean(string="Relación de dependencia", required=True, )
    actividad_con_ids = fields.One2many('hr.employee.actividad_contrato', 'actividad_con_id', string="Actividad")


class Etnia(models.Model):
    _name = 'hr.employee.etnia'
    name = fields.Char(string="Etnia")
    grupo_etnia_ids = fields.Many2one('hr.employee.grupo_etnico', string="Grupo Étnico",)

class Grupo_Etnico(models.Model):
    _name = 'hr.employee.grupo_etnico'
    name = fields.Char(string="Grupo Étnico",)

class ActividadContrato(models.Model):
    _name = 'hr.employee.actividad_contrato'
    actividad_con_id = fields.Many2one('hr.employee', string="Actividad",)
    name = fields.Char(string="Actividad")


class Parentesco(models.Model):
    _name = 'hr.employee.parentesco'
    name = fields.Char(string="Parentesco")

class TipoFuncionario(models.Model):
    _name = 'hr.employee.tipo_funcionario'
    name = fields.Char(string="Tipo Funcionario")


class Escalafon(models.Model):
    _name = 'hr.employee.escalafon'
    name = fields.Char(string="Escalafón")
    tipo_funcionario = fields.Many2one(comodel_name="hr.employee.tipo_funcionario", string="Tipo Funcionario", required=True, )

class Formacion(models.Model):
    _name = 'hr.employee.formacion'
    formacion_id = fields.Many2one('hr.employee', string="Formación")
    nivel = fields.Many2one(comodel_name="hr.employee.nivel", string="Nivel de Instrucción", required=True, )
    institucion = fields.Many2one(comodel_name="hr.employee.institucion", string="Institución educativa", required=True, )
    titulo = fields.Many2one(comodel_name="hr.employee.titulo", string="Título obtenido", required=True, )
    registrado =  fields.Boolean(string="Registrado", required=True, )
    registro = fields.Char(string="No. del registro")
    file_name = fields.Char(string="Nombre archivo")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment",relation="formacion_id",string='Adjunto',required=True,)

class Nivel(models.Model):
    _name = 'hr.employee.nivel'
    name = fields.Char(string="Nivel de Instrucción")

class Institucion(models.Model):
    _name = 'hr.employee.institucion'
    name = fields.Char(string="Institución educativa")

class Titulo(models.Model):
    _name = 'hr.employee.titulo'
    name = fields.Char(string="Título obtenido")

class Capacitacion(models.Model):
    _name = 'hr.employee.capacitacion'
    capacitacion_id = fields.Many2one('hr.employee', string="Capacitación")

    name = fields.Char(string="Nombre del Evento")
    institucioncap = fields.Char(string="Institución educativa", required=True, )
    evento = fields.Many2one(comodel_name="hr.employee.evento", string="Tipo de evento", required=True, )
    area = fields.Many2one(comodel_name="hr.employee.area", string="Área de estudios", required=True, )
    tipo = fields.Many2one(comodel_name="hr.employee.tipo", string=" Tipo de certificado", required=True, )
    fecha_desde = fields.Date(string="Fecha desde", required=True, )
    fecha_hasta = fields.Date(string="Fecha hasta", required=True, )
    dias = fields.Integer(string="Número de días", required=True, )
    horas = fields.Integer(string="Número de horas totales", required=True, )
    ad_capacitacion_ids = fields.Many2many(comodel_name="ir.attachment", relation="capacitacion_id", string='Adjuntar Capacitación',required=True, )

class Evento(models.Model):
    _name = 'hr.employee.evento'
    name = fields.Char(string="Nombre del Evento")

class Area(models.Model):
    _name = 'hr.employee.area'
    name = fields.Char(string="Área de estudios")

class Tipo(models.Model):
    _name = 'hr.employee.tipo'
    name = fields.Char(string=" Tipo de certificado")

class Experiencia(models.Model):
    _name = 'hr.employee.experiencia'

    experiencia_id = fields.Many2one('hr.employee', string="Experiencia")
    institucion = fields.Char(string="Institución", required=True, )
    puesto = fields.Char(string="Puesto", required=True, )
    areatrabajo = fields.Many2one(comodel_name="hr.employee.areatrabajo", string="Área de trabajo", required=True, )
    fecha_desde = fields.Date(string="Fecha desde", required=True, )
    fecha_hasta = fields.Date(string="Fecha hasta",  )
    actividad_ids = fields.Many2many('hr.employee.actividad', string="Actividades")
    ad_experiencia_ids = fields.Many2many(comodel_name="ir.attachment", relation="experiencia_id", string='Adjuntar Experiencia', required=True,)

class AreaTrabajo(models.Model):
    _name = 'hr.employee.areatrabajo'
    name = fields.Char(string="Área de trabajo")

class Actividad(models.Model):
    _name = 'hr.employee.actividad'
    name = fields.Char(string="Actividades")

class Logro(models.Model):
    _name = 'hr.employee.logro'
    name = fields.Char(string="Logro")
    logro_id = fields.Many2one('hr.employee', string="Logros")
    tipologro = fields.Many2one(comodel_name="hr.employee.tipologro", string="Tipo de Logro", required=True, )
    ad_logro_ids = fields.Many2many(comodel_name="ir.attachment", relation="logro_id", string='Adjuntar Logro', )

class TipoLogro(models.Model):
    _name = 'hr.employee.tipologro'
    name = fields.Char(string="Tipo Logro")
