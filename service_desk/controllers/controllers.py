# -*- coding: utf-8 -*-
import werkzeug
from random import randint
from odoo import http
from odoo.http import request


class Example(http.Controller):
    @http.route('/create_issue', type='http', auth='user', website=True)
    def render_example_page(self):
        return http.request.render('service_desk.website_project_issue', {})

    @http.route('/create_issue/ticket', type='http', auth='user', website=True)
    def navigate_to_detail_page(self):
        # This will get all company details (in case of multicompany this are multiple records)
        issue = http.request.env['project.issue'].sudo().search([ ('partner_id','=',http.request.env.user.partner_id.id) ])
        return http.request.render('service_desk.website_project_detail_ticket', {
            # pass company details to the webpage in a variable
            'issue': issue})

    @http.route('/create_issue/ticket/submit', type="http", auth="public", website=True)
    def support_submit_ticket(self, **kw):
        """Let's public and registered user submit a support ticket"""
        person_name = ""
        if http.request.env.user.name != "Public user":
            person_name = http.request.env.user.name

        setting_max_ticket_attachments = request.env['ir.values'].get_default('website.support.settings',
                                                                              'max_ticket_attachments')

        if setting_max_ticket_attachments == 0:
            # Back compatablity
            setting_max_ticket_attachments = 2

        setting_max_ticket_attachment_filesize = request.env['ir.values'].get_default('website.support.settings',
                                                                                      'max_ticket_attachment_filesize')

        if setting_max_ticket_attachment_filesize == 0:
            # Back compatablity
            setting_max_ticket_attachment_filesize = 500

        return http.request.render('service_desk.website_project_create_ticket', {
            'categories': http.request.env['project.issue.category'].sudo().search([]),
            'person_name': person_name, 'email': http.request.env.user.email,
            'setting_max_ticket_attachments': setting_max_ticket_attachments,
            'setting_max_ticket_attachment_filesize': setting_max_ticket_attachment_filesize})

    @http.route('/create_issue/ticket/process', type="http", auth="public", website=True, csrf=True)
    def support_process_ticket(self, **kwargs):
        """Adds the support ticket to the database and sends out emails to everyone following the support ticket category"""
        values = {}
        for field_name, field_value in kwargs.items():
            values[field_name] = field_value

        if values['my_gold'] != "256":
            return "Bot Detected"

        my_attachment = ""
        file_name = ""



        if http.request.env.user.name != "Public user":
            portal_access_key = randint(1000000000, 2000000000)
            new_ticket_id = request.env['project.issue'].sudo().create(
                {'categoria': values['category'],
                 'email_from': values['email'], 'description': values['description'], 'name': values['subject'],
                 'partner_id': http.request.env.user.partner_id.id,
                 })

       # if http.request.env.user.name != "Public user":
       #     portal_access_key = randint(1000000000, 2000000000)
       #     new_ticket_id = request.env['project.issue'].sudo().create(
       #          {'person_name': values['person_name'], 'categoria': values['category'],
       #           'email_from': values['email'], 'description': values['description'], 'name': values['subject'],
       #           'partner_id': http.request.env.user.partner_id.id, 'attachment': my_attachment,
       #           'attachment_filename': file_name, 'portal_access_key': portal_access_key})

            partner = http.request.env.user.partner_id

            # Add to the communication history
            partner.message_post(body="Customer " + partner.name + " has sent in a new support ticket",
                                 subject="New Support Ticket")


        # Remove the Administrator follower
        for ticket_follower in request.env['mail.followers'].sudo().search(
                [('res_model', '=', 'project.issue'), ('res_id', '=', new_ticket_id.id)]):
            ticket_follower.unlink()

        if 'file' in values:

            for c_file in request.httprequest.files.getlist('file'):
                data = c_file.read()

                if c_file.filename:
                    request.env['ir.attachment'].sudo().create({
                        'name': c_file.filename,
                        'datas': data.encode('base64'),
                        'datas_fname': c_file.filename,
                        'res_model': 'project.issue',
                        'res_id': new_ticket_id.id
                    })

        return werkzeug.utils.redirect("/support/ticket/thanks")



