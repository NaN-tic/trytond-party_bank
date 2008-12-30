#This file is part of Tryton. The COPYRIGHT file at the top level of 
#this repository contains the full copyright notices and license terms.
{
    'name': 'Party Bank',
    'name_de_DE': 'Bankverbindungen für Parteien',
    'version': '0.0.1',
    'author': 'virtual things',
    'email': 'info@virtual-things.biz',
    'website': 'http://www.virtual-things.biz/',
    'description': '''Party Bank
''',
    'description_de_DE': '''Erlaubt die Verwaltung von Bankverbindungen für
    Parteien
''',
    'depends': [
        'party',
        'currency'
    ],
    'xml': [
        'bank.xml',
    ],
#    'translation': [
#        'de_DE.csv',
#    ],
}
