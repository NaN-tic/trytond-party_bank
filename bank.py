#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.osv import fields, OSV

class Bank(OSV):
    'Bank'
    _name = 'bank.bank'
    _description = __doc__
    _inherits = {'party.party': 'party'}
    
    party = fields.Many2One('party.party', 'Party', required=True,
            ondelete='CASCADE')
    bank_code = fields.Char('National Code', select=1, 
                       states={'required': "type=='national'"})
    bic = fields.Char('BIC/SWIFT', select=1, states={'required': "type=='bic'"})
    type = fields.Selection([('national', 'National Standard'),
                             ('bic', 'BIC/SWIFT')], 'Bank Type', required=True,
                             select=1)
    
    def default_type(self, cursor, user, context=None):
        return 'national'
        
Bank()


class BankAccount(OSV):
    'Bank Account'
    _name = 'bank.account'
    _description = __doc__
    
    name = fields.Char('Name', required=True)
    code = fields.Char('Account Number', help='National Standard Code',
                       states={'required': "type=='national'" })
    iban = fields.Char('IBAN', states={'required': "type=='iban'"})
    bank = fields.Many2One('bank.bank', 'Bank', required=True)
    currency = fields.Many2One('currency.currency', 'Currency', required=True)
    party = fields.Many2One('party.party', 'Party', required=True)
    type = fields.Selection([('national', 'National Standard'),
                             ('iban', 'IBAN')], 'Bank Account Type')
    owner = fields.Many2One('party.party', 'Differing Owner')
    
    def default_type(self, cursor, user, context=None):
        return 'national'
    
BankAccount()    
    
    
class Party(OSV):
    'Party'
    _name = 'party.party'
    _description = __doc__
    
    bank_accounts = fields.One2Many('bank.account', 'party', 'Bank Accounts')
        
Party()