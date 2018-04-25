# -*- coding: utf-8 -*-
from odoo import http

# class ConnectionMdirector(http.Controller):
#     @http.route('/connection_mdirector/connection_mdirector/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/connection_mdirector/connection_mdirector/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('connection_mdirector.listing', {
#             'root': '/connection_mdirector/connection_mdirector',
#             'objects': http.request.env['connection_mdirector.connection_mdirector'].search([]),
#         })

#     @http.route('/connection_mdirector/connection_mdirector/objects/<model("connection_mdirector.connection_mdirector"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('connection_mdirector.object', {
#             'object': obj
#         })