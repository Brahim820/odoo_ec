# -*- coding: utf-8 -*-

import logging
import time

from odoo import models, fields, api
from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.modules.module import get_module_resource
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from zklib import zklib
from zklib import zkconst


# inherit hr_employee module
class hr_employee(models.Model):
    _inherit = 'hr.employee'

    emp_code = fields.Char("Emp Code")
    category = fields.Char("Category")


# inherit hr_attendance module
class hr_attendance(models.Model):
    _inherit = 'hr.attendance'

    emp_code = fields.Char("Emp Code")

    # overriding the __check_validity fucntion to not check the "check_out" value for employee attendance
    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_validity(self):
        """ Verifies the validity of the attendance record compared to the others from the same employee.
            For the same employee we must have :
                * maximum 1 "open" attendance record (without check_out)
                * no overlapping time slices with previous employee records
        """
        for attendance in self:
            # we take the latest attendance before our check_in time and check it doesn't overlap with ours
            last_attendance_before_check_in = self.env['hr.attendance'].search([
                ('employee_id', '=', attendance.employee_id.id),
                ('check_in', '<=', attendance.check_in),
                ('id', '!=', attendance.id),
             ], order='check_in desc', limit=1)
            if last_attendance_before_check_in and last_attendance_before_check_in.check_out and last_attendance_before_check_in.check_out >= attendance.check_in:
                raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee was already checked in on %(datetime)s") % {
                    'empl_name': attendance.employee_id.name_related,
                    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(attendance.check_in))),
                 })

            # Commented out the attendance.checkout checking
            if not attendance.check_out:
                # if our attendance is "open" (no check_out), we verify there is no other "open" attendance
                no_check_out_attendances = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_out', '=', False),
                    ('id', '!=', attendance.id),
                 ])
                if no_check_out_attendances:
                    pass
                    # raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee hasn't checked out since %(datetime)s") % {
                    #    'empl_name': attendance.employee_id.name_related,
                    #    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(no_check_out_attendances.check_in))),
                    # })
            else:
                # we verify that the latest attendance with check_in time before our check_out time
                # is the same as the one before our check_in time computed before, otherwise it overlaps
                last_attendance_before_check_out = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_in', '<=', attendance.check_out),
                    ('id', '!=', attendance.id),
                 ], order='check_in desc', limit=1)
                if last_attendance_before_check_out and last_attendance_before_check_in != last_attendance_before_check_out:
                    raise ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee was already checked in on %(datetime)s") % {
                        'empl_name': attendance.employee_id.name_related,
                        'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(last_attendance_before_check_out.check_in))),
                     })


# biometric machine module
class biometric_machine(models.Model):
    _name = 'biometric.machine'

    name = fields.Char("Machine IP")
    ref_name = fields.Char("Location")
    port = fields.Integer("Port Number")
    address_id = fields.Many2one('res.partner', string='Partner')
    company_id = fields.Many2one("res.company", string='Company Name')

    # function to download attendance
    @api.multi
    def download_attendance(self):
        hr_attendance = self.env['hr.attendance'].browse()
        for info in self:
            machine_ip = info.name
            port = info.port

            # connect to the biometric device using the machine ip and port
            zk = zklib.ZKLib(str(machine_ip), int(port))
            res = zk.connect()
            print '1 res'+str(res)
            if res:
                zk.enableDevice()
                print zk.enableDevice()
                print zk.disableDevice()
                print zk.version()
                print zk.osversion()
                print zk.deviceName()
                print zk.getUser()

                user = zk.getUser()
                print '0 user ' + str(user)
                attendance = zk.getAttendance()
                print 'attendance ' + str(attendance)
                if (attendance):
                    # get the user data from the biometric device
                    user = zk.getUser()
                    print '0.1 user ' + str(user)
                    for lattendance in attendance:
                        time_att = str(lattendance[2].date()) + ' ' + str(lattendance[2].time())
                        print '2 time_att ' + str(time_att)
                        atten_time = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                        print '3 atten_time ' + str(atten_time)
                        atten_time = datetime.strftime(atten_time, '%Y-%m-%d %I:%M:%S')
                        print '4 atten_time ' + str(atten_time)
                        in_time = datetime.strptime(atten_time, '%Y-%m-%d %H:%M:%S').time()
                        print '5 in_time ' + str(in_time)
                        time_new = str(in_time)
                        time_new = time_new.replace(":", ".", 1)
                        time_new = time_new[0:5]
                        check_in = fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(atten_time))),
                        print '6 check_in ' + str(check_in)
                        if user:
                            for uid in user:
                                # compare the employee code in user data with employee code in attendance data of each employee in the attendance list
                                # only matched users are processed
                                print '7 user[uid][0] ' + user[uid][0]
                                print '8 lattendance[0] ' + str(lattendance)
                                print '8 lattendance[0] ' + str(str(lattendance[0]))
                                if user[uid][0] == str(lattendance[0]):
                                    get_user_id = self.env['hr.employee'].search([('emp_code', '=', str(lattendance[0]))])
                                    print '8 get_user_id ' + str(get_user_id)
                                    if get_user_id:

                                        # check for duplicate attendance values
                                        duplicate_atten_ids = self.env['hr.attendance'].search([('emp_code', '=', str(lattendance[0])), ('check_in', '=', check_in)])

                                        if duplicate_atten_ids:
                                            continue
                                        else:
                                            # create attendance values to hr.attendance table
                                            search_user_id = self.env['hr.employee'].search([('name', '=', user[uid][1]), ('emp_code', '=', str(lattendance[0]))])
                                            if search_user_id:
                                                data = hr_attendance.create({'employee_id': get_user_id.id, 'emp_code': lattendance[0], 'check_in': check_in})
                                    else:
                                        employee = self.env['hr.employee'].create({'emp_code': str(lattendance[0]), 'name': user[uid][1]})
                                        data = hr_attendance.create({'employee_id': employee.id, 'emp_code': lattendance[0], 'check_in': check_in})
                                else:
                                    pass

                    zk.enableDevice()
                    zk.disconnect()
                    return True
                else:
                    raise UserError(_('Unable to get the attendance log, please try again later.'))   
            else:
                raise UserError(_('Unable to connect, please check the parameters and network connections.'))
                
    # Dowload attendence data regularly
    @api.multi
    def schedule_download(self, ids=None):

        if not self.ids:
            ids = self.search(ids).ids
            res = None
            try:
                res = self.browse(ids).download_attendance()
            except:
                raise ValidationError(('Warning !'), ("Machine with is not connected"))
            return res
