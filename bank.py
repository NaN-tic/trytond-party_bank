#This file is part party_bank module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.backend import TableHandler
from trytond.pyson import Not, Eval, Bool
from trytond.transaction import Transaction
from trytond.pool import Pool

__all__ = ['Bank', 'BankAccount']

class Bank(ModelSQL, ModelView):
    'Bank'
    __name__ = 'bank.bank'
    _inherits = {'party.party': 'party'}
    _rec_name = 'bank_code'

    party = fields.Many2One('party.party', 'Party', required=True,
            ondelete='CASCADE')
    bank_code = fields.Char('National Code', select=1,
            states={
                'required': Not(Bool(Eval('bic')))
                }, depends=['bic'])
    bic = fields.Char('BIC/SWIFT', select=1,
            states={
                'required': Not(Bool(Eval('bank_code')))
                }, depends=['bank_code'])

    @classmethod
    def get_rec_name(cls, records, name):
        res = {}
        if not records:
            return res
        for bank in records:
            res[bank.id] = ", ".join(
                     x for x in [bank.name, bank.bank_code, bank.bic] if x)
        return res

    @classmethod
    def search_rec_name(cls, name, clause):
        ids = cls.search([
            ('name',) + tuple(clause[1:]),
            ], limit=1)
        if ids:
            return [('name',) + tuple(clause[1:])]
        else:
            ids = cls.search([
                ('bank_code',) + tuple(clause[1:]),
                ], limit=1)
            if ids:
                return [('bank_code',) + tuple(clause[1:])]
            else:
                ids = cls.search([
                    ('bic',) + tuple(clause[1:]),
                    ], limit=1)
                if ids:
                    return [('bic',) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]


class BankAccount(ModelSQL, ModelView):
    'Bank Account'
    __name__ = 'bank.account'
    _rec_name = 'code'

    default = fields.Boolean('Default', help="Default Bank Account")
    code = fields.Char('Account Number', help='National Standard Code',
            states={
                'required': Not(Bool(Eval('iban')))
                }, depends=['iban'])
    iban = fields.Char('IBAN',
            states={
                'required': Not(Bool(Eval('code')))
                }, depends=['code'])
    bank = fields.Many2One('bank.bank', 'Bank', required=True,
            on_change=['bank'], context={'is_bank': True})
    bank_code = fields.Function(fields.Char('National Code'),
            'get_bank_code')
    bic = fields.Function(fields.Char('BIC/SWIFT'), 'get_bic')
    currency = fields.Many2One('currency.currency', 'Currency')
    party = fields.Many2One('party.party', 'Party', ondelete='CASCADE',
            required=True)
    owner = fields.Char('Differing Owner')
    street = fields.Char('Street')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    country = fields.Many2One('country.country', 'Country',
        on_change=['country', 'subdivision'])
    subdivision = fields.Many2One("country.subdivision",
            'Subdivision', domain=[('country', '=', Eval('country'))],
            depends=['country'])

    @classmethod
    def __register__(cls, module_name):
        super(BankAccount, cls).__register__(module_name)
        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)
        # Migration for existing databases
        # Set column 'currency' not required
        table.not_null_action('currency', action='remove')
        # Remove column 'name'
        if table.column_exist('name'):
            table.drop_column('name', exception=True)

    @staticmethod
    def default_default():
        return True

    @classmethod
    def get_rec_name(cls, records, name):
        res = {}
        if not records:
            return res
        for account in records:
            res[account.id] = ", ".join(x for x in [account.bank.name,
                    account.code, account.bank_code, account.iban,
                    account.bic] if x)
        return res

    @classmethod
    def get_bank_code(cls, records, name):
        res = {}
        for account in records:
            res[account.id] = account.bank.bank_code
        return res

    @classmethod
    def get_bic(cls, records, name):
        res = {}
        for account in records:
            res[account.id] = account.bank.bic
        return res

    def on_change_bank(self):
        res = {
           'bank_code': False,
           'bic': False
           }
        print self.bank
        if self.bank:
            bank = self.bank
            if bank:
                res['bank_code'] = bank.bank_code
                res['bic'] = bank.bic
        print "==="
        print res
        return res

    def on_change_country(self):
        if (self.subdivision
                and self.subdivision.country != self.country):
            return {'subdivision': None}
        return {}
