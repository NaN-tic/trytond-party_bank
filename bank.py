#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.backend import TableHandler

class Bank(ModelSQL, ModelView):
    'Bank'
    _name = 'bank.bank'
    _description = __doc__
    _inherits = {'party.party': 'party'}
    _rec_name = bank_code

    party = fields.Many2One('party.party', 'Party', required=True,
            ondelete='CASCADE')
    bank_code = fields.Char('National Code', select=1)
    bic = fields.Char('BIC/SWIFT', select=1)

    def get_rec_name(self, cursor, user, ids, name, arg, context=None):
        if not ids:
            return {}
        res = {}
        for bank in self.browse(cursor, user, ids, context=context):
            res[bank.id] = ", ".join(x for x in [bank.name, bank.bank_code,
                                                 bank.bic] if x)
        return res

    def search_rec_name(self, cursor, user, name, args, context=None):
        args2 = []
        i = 0
        while i < len(args):
            ids = self.search(cursor, user, [
                ('bank_code', args[i][1], args[i][2]),
                ], limit=1, context=context)
            if ids:
                args2.append(('bank_code', args[i][1], args[i][2]))
            else:
                ids = self.search(cursor, user, [
                             ('bic', args[i][1], args[i][2]),
                             ], limit=1, context=context)
                if ids:
                    args2.append(('bic', args[i][1], args[i][2]))
                else:
                    args2.append((self._rec_name, args[i][1], args[i][2]))
            i += 1
        return args2

Bank()


class BankAccount(ModelSQL, ModelView):
    'Bank Account'
    _name = 'bank.account'
    _description = __doc__
    _rec_name = 'code'

    code = fields.Char('Account Number', help='National Standard Code')
    iban = fields.Char('IBAN')
    bank = fields.Many2One('bank.bank', 'Bank', required=True,
                           on_change=['bank'])
    bank_code = fields.Function('get_bank_code', type='char',
            string='National Code')
    bic = fields.Function('get_bic', type='char',
            string='BIC/SWIFT')
    currency = fields.Many2One('currency.currency', 'Currency')
    party = fields.Many2One('party.party', 'Party',
                            ondelete='CASCADE', required=True)
    owner = fields.Char('Differing Owner')

    def init(self, cursor, module_name):
        super(BankAccount, self).init(cursor, module_name)
        table = TableHandler(cursor, self, module_name)
        # Migration for existing databases
        # Set currency not required
        table.not_null_action('currency', action='remove')

    def get_rec_name(self, cursor, user, ids, name, arg, context=None):
        if not ids:
            return {}
        res = {}
        for account in self.browse(cursor, user, ids, context=context):
            res[account.id] = ", ".join(x for x in [account.bank.name,
                        account.code, account.bank_code, account.iban,
                        account.bic] if x)
        return res

    def get_bank_code(self, cursor, user, ids, name, arg, context=None):
        res = {}
        for account in self.browse(cursor, user, ids, context=context):
            res[account.id] = account.bank.bank_code
        return res

    def get_bic(self, cursor, user, ids, name, arg, context=None):
        res = {}
        for account in self.browse(cursor, user, ids, context=context):
            res[account.id] = account.bank.bic
        return res

    def on_change_bank(self, cursor, user, ids, vals, context=None):
        bank_obj = self.pool.get('bank.bank')
        res = {'bank_code': None,
               'bic': None}

        if vals.get('bank'):
            bank = bank_obj.browse(cursor, user, vals.get('bank'),
                                context=context)
            if bank:
                res['bank_code'] = bank.bank_code
                res['bic'] = bank.bic
        return res

BankAccount()
