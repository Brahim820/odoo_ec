# -*- coding: utf-8 -*-
from odoo import http

# class IpEcSolicitudMaterial(http.Controller):
#     @http.route('/ip_ec_solicitud_material/ip_ec_solicitud_material/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ip_ec_solicitud_material/ip_ec_solicitud_material/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ip_ec_solicitud_material.listing', {
#             'root': '/ip_ec_solicitud_material/ip_ec_solicitud_material',
#             'objects': http.request.env['ip_ec_solicitud_material.ip_ec_solicitud_material'].search([]),
#         })

#     @http.route('/ip_ec_solicitud_material/ip_ec_solicitud_material/objects/<model("ip_ec_solicitud_material.ip_ec_solicitud_material"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ip_ec_solicitud_material.object', {
#             'object': obj
#         })