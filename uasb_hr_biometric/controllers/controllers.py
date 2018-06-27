# -*- coding: utf-8 -*-
from odoo import http

# class UasbHrBiometric(http.Controller):
#     @http.route('/uasb_hr_biometric/uasb_hr_biometric/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uasb_hr_biometric/uasb_hr_biometric/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uasb_hr_biometric.listing', {
#             'root': '/uasb_hr_biometric/uasb_hr_biometric',
#             'objects': http.request.env['uasb_hr_biometric.uasb_hr_biometric'].search([]),
#         })

#     @http.route('/uasb_hr_biometric/uasb_hr_biometric/objects/<model("uasb_hr_biometric.uasb_hr_biometric"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uasb_hr_biometric.object', {
#             'object': obj
#         })