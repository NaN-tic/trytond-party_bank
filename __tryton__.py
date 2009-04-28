#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Party Bank',
    'name_de_DE': 'Partei Bankverbindungen',
    'name_es_ES': 'Banco de terceros',
    'version': '1.1.0',
    'author': 'virtual things',
    'email': 'info@virtual-things.biz',
    'website': 'http://www.virtual-things.biz/',
    'description': '''Party Bank
    Allows the management of bank accounts for parties
''',
    'description_de_DE': '''Ermöglicht die Verwaltung von Bankverbindungen für Parteien
''',
    'description_es_ES': '''Banco de terceros
    Permite la gestión de cuentas bancarias de terceros
''',
    'depends': [
        'party',
        'currency'
    ],
    'xml': [
        'bank.xml',
        'party.xml'
    ],
    'translation': [
        'de_DE.csv',
        'es_ES.csv',
    ],
}
