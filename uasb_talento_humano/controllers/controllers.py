# -*- coding: utf-8 -*-
from odoo import http

# class UasbTalentoHumano(http.Controller):
#     @http.route('/uasb_talento_humano/uasb_talento_humano/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uasb_talento_humano/uasb_talento_humano/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uasb_talento_humano.listing', {
#             'root': '/uasb_talento_humano/uasb_talento_humano',
#             'objects': http.request.env['uasb_talento_humano.uasb_talento_humano'].search([]),
#         })

#     @http.route('/uasb_talento_humano/uasb_talento_humano/objects/<model("uasb_talento_humano.uasb_talento_humano"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uasb_talento_humano.object', {
#             'object': obj
#         })