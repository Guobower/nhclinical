# Part of NHClinical. See LICENSE file for full copyright and licensing details
# -*- coding: utf-8 -*-
{
    'name': 'NH Clinical Core',
    'version': '0.1',
    'category': 'Clinical',
    'license': 'AGPL-3',
    'summary': '',
    'description': """     """,
    'author': 'Neova Health',
    'website': 'http://www.neovahealth.co.uk/',
    'depends': ['nh_activity', 'hr'],
    'data': ['data/data.xml',
             'data/nh_cancel_reasons.xml',
             'views/pos_view.xml',
             'views/location_view.xml',
             'views/patient_view.xml',
             'views/user_view.xml',
             'views/device_view.xml',
             'views/operations_view.xml',
             'views/user_management_view.xml',
             'views/doctor_view.xml',
             'wizard/placement_wizard_view.xml',
             'wizard/responsibility_allocation_wizard.xml',
             'wizard/user_allocation_view.xml',
             'views/menuitem.xml',
             'views/static_resources.xml',
             'security/ir.model.access.csv',
             'security/adt/ir.model.access.csv',
             'security/operations/ir.model.access.csv',
             'data/change_ward_manager_to_shift_coordinator.xml'],
    'demo': ['data/test/locations.xml', 'data/test/users.xml'],
    'css': [],
    'js': [],
    'qweb': [],
    'images': [],
    'application': True,
    'installable': True,
    'active': False,
}
