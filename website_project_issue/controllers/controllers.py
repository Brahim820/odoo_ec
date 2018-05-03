# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteProjectIssue(http.Controller):
#     @http.route('/website_project_issue/website_project_issue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_project_issue/website_project_issue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_project_issue.listing', {
#             'root': '/website_project_issue/website_project_issue',
#             'objects': http.request.env['website_project_issue.website_project_issue'].search([]),
#         })

#     @http.route('/website_project_issue/website_project_issue/objects/<model("website_project_issue.website_project_issue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_project_issue.object', {
#             'object': obj
#         })