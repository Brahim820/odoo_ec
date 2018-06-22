from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
from zklib import zklib

class hr_employee(models.Model):
    _name = "hr.employee"
    _inherit = 'hr.employee'

    emp_code = fields.Char(string="Emp Code",)
    category = fields.Char(string="category",)

class biometric_machine(models.Model):
    _name= 'biometric.machine'
    name = fields.Char(string="Machine IP",)
    ref_name = fields.Char(string="Location",)
    port = fields.Integer(string="Port Number",)
    address_id = fields.Many2one('res.partner', string="Working Address")
    company_id = fields.Many2one('res.company', string="Company Name")
    atten_ids = fields.One2many('biometric.data', 'mechine_id', string="Attendance")

    def download_attendance(self, context=None):
        machine_ip = self.name
        port = self.port
        zk = zklib.ZKLib(machine_ip, int(port))
        res = zk.connect()
        print zk.enableDevice()
        print zk.disableDevice()
        print zk.version()
        print zk.osversion()
        print zk.deviceName()
        print zk.getAttendance()
        if res == True:
            zk.enableDevice()
            zk.disableDevice()
            attendance = zk.getAttendance()
            hr_attendance =  self.pool.get("hr.attendance")
            hr_employee = self.pool.get("hr.employee")
            biometric_data = self.pool.get("biometric.data")
            print 'CD------------------------------------------attendance' + str(attendance)
            if (attendance):
                for lattendance in attendance:
                    time_att = str(lattendance[2].date()) + ' ' + str(lattendance[2].time())
                    print 'CD------------------------------------------time_att' + str(time_att)
                    atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                    print 'CD------------------------------------------atten_time1' + str(atten_time1)
                    atten_time = atten_time1 - timedelta(hours=5,minutes=30)
                    print 'CD------------------------------------------atten_time' + str(atten_time)
                    atten_time = datetime.strftime(atten_time, '%Y-%m-%d %H:%M:%S')
                    print 'CD------------------------------------------time_att' + str(atten_time)
                    atten_time1 = datetime.strftime(atten_time1, '%Y-%m-%d %H:%M:%S')
                    print 'CD------------------------------------------atten_time1' + str(atten_time1)
                    in_time = datetime.strptime(atten_time1, '%Y-%m-%d %H:%M:%S').time()
                    print 'CD------------------------------------------in_time' + str(in_time)

                    time_new = str(in_time)
                    time_new = time_new.replace(":", ".", 1)
                    time_new = time_new[0:5]
                    print time_att, lattendance[0]
                    try:
                        del_atten_ids = biometric_data.search([('emp_code', '=', str(lattendance[0])), ('name', '=', atten_time)])
                        if del_atten_ids:
                            # hr_attendance.unlink(cr, uid, del_atten_ids)
                            continue
                        else:
                            print "Date %s, Name %s: %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0] )
                            a = biometric_data.create({'name':atten_time, 'emp_code': lattendance[0]})
                            print a
                    except Exception, e:
                        pass
                        print "exception..Attendance creation======", e.args
            zk.enableDevice()
            zk.disconnect()
            return True
        else:
            print(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))
    #Dowload attendence data regularly
    def schedule_download(self, cr, uid, context=None):

            scheduler_line_obj = self.pool.get('biometric.machine')
            scheduler_line_ids = self.pool.get('biometric.machine').search(cr, uid, [])
            for scheduler_line_id in scheduler_line_ids:
                scheduler_line =scheduler_line_obj.browse(cr, uid, scheduler_line_id, context=None)
                try:
                    scheduler_line.download_attendance()
                except:
                    print(('Warning !'), ("Machine with %s is not connected" %(scheduler_line.name)))

    def clear_attendance(self,  context=None):
        machine_ip = self.name
        port = self.port
        print 'CD------------------------------------------' + str(machine_ip) + '' + str(port)
        zk = zklib.ZKLib(machine_ip, int(port))
        res = zk.connect()
        print 'CD------------------------------------------' + str(res)
        if res == True:
            zk.enableDevice()
            zk.disableDevice()
            zk.clearAttendance()
            zk.enableDevice()
            zk.disconnect()
            return True
        else:
            print(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))

class biometric_data(models.Model):
    _name = "biometric.data"
    name = fields.Datetime(string="Date"),
    emp_code = fields.Char(string="Employee Code"),
    mechine_id = fields.Many2one('biometric.machine', string="Mechine No")

