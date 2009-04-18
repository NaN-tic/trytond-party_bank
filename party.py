#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

class Party(ModelSQL, ModelView):
    'Party'
    _name = 'party.party'
    _description = __doc__

    bank_accounts = fields.One2Many('bank.account', 'party', 'Bank Accounts')

Party()