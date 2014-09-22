# -*- coding: utf-8 -*-

from openerp.osv import orm, fields
from openerp.addons.t4activity.activity import except_if
import logging        
_logger = logging.getLogger(__name__)


class t4_clinical_spell(orm.Model):
    _name = 't4.clinical.spell'
    _inherit = ['t4.activity.data']
    _description = "Spell / Visit"
    
    _rec_name = 'code'
    _columns = {
        'patient_id': fields.many2one('t4.clinical.patient', 'Patient', required=True),
        'location_id': fields.many2one('t4.clinical.location', 'Placement Location'),
        'pos_id': fields.many2one('t4.clinical.pos', 'Placement Location', required=True),
        'code': fields.text("Code"),
        'start_date': fields.datetime("ADT Start Date"),
        'ref_doctor_ids': fields.many2many('res.partner', 'ref_doctor_spell_rel', 'spell_id', 'doctor_id', "Referring Doctors"),
        'con_doctor_ids': fields.many2many('res.partner', 'con_doctor_spell_rel', 'spell_id', 'doctor_id', "Consulting Doctors"),        
    }
    _defaults = {
         'code': lambda s, cr, uid, c: s.pool['ir.sequence'].next_by_code(cr, uid, 't4.clinical.spell', context=c),
     }

    def create(self, cr, uid, vals, context=None):
        current_spell_id = self.search(cr, uid, [('patient_id','=',vals['patient_id']),('state','in',['started'])], context)
#         if current_spell_id:
#             import pdb; pdb.set_trace()
        if current_spell_id:
            res = current_spell_id[0]
            _logger.warn("Started spell already exists! Current spell ID=%s returned." % current_spell_id[0])
        else:        
            res = super(t4_clinical_spell, self).create(cr, uid, vals, context)
        return res

    def get_activity_user_ids(self, cr, uid, activity_id, context=None):
        api = self.pool['t4.clinical.api']
        user_ids = api.user_map(cr, uid, 
                        group_xmlids=['group_t4clinical_hca', 'group_t4clinical_nurse', 
                                      'group_t4clinical_ward_manager', 'group_t4clinical_doctor',
                                      'group_t4clinical_dev', 'group_t4clinical_admin']).keys()
        print "SPELL get_activity_user_ids user_ids: %s " % user_ids
        return user_ids