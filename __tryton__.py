#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Party Bank',
    'name_de_DE': 'Partei Bankverbindungen',
    'version': '0.0.2',
    'author': 'virtual things',
    'email': 'info@virtual-things.biz',
    'website': 'http://www.virtual-things.biz/',
    'description': '''Party Bank
    Allows the management of bank accounts for parties
''',
    'description_de_DE': '''Ermöglicht die Verwaltung von Bankverbindungen für Parteien
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
    ],
}
