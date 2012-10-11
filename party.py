#This file is part party_bank module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta

class Party:
    __name__ = 'party.party'

    bank_accounts = fields.One2Many('bank.account', 'party', 'Bank Accounts')

