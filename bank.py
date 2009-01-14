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
    bank_code = fields.Char('National Code', select=1)
    bic = fields.Char('BIC/SWIFT', select=1)

Bank()


class BankAccount(OSV):
    'Bank Account'
    _name = 'bank.account'
    _description = __doc__

    name = fields.Char('Name', required=True)
    code = fields.Char('Account Number', help='National Standard Code')
    iban = fields.Char('IBAN')
    bank = fields.Many2One('bank.bank', 'Bank', required=True)
    currency = fields.Many2One('currency.currency', 'Currency', required=True)
    party = fields.Many2One('party.party', 'Party',
                            ondelete='CASCADE', required=True)
    owner = fields.Char('Differing Owner')

BankAccount()


class Party(OSV):
    'Party'
    _name = 'party.party'
    _description = __doc__

    bank_accounts = fields.One2Many('bank.account', 'party', 'Bank Accounts')

Party()