# -*- coding: utf-8 -*-
from odoo import http

# class ServiceDesk(http.Controller):
#     @http.route('/service_desk/service_desk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_desk/service_desk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_desk.listing', {
#             'root': '/service_desk/service_desk',
#             'objects': http.request.env['service_desk.service_desk'].search([]),
#         })

#     @http.route('/service_desk/service_desk/objects/<model("service_desk.service_desk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_desk.object', {
#             'object': obj
#         })