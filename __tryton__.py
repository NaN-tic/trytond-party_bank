#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'BETA: Party Bank',
    'name_de_DE': 'BETA: Partei Bankverbindungen',
    'name_es_ES': 'BETA: Banco de terceros',
    'version': '1.5.0',
    'author': 'virtual things',
    'email': 'info@virtual-things.biz',
    'website': 'http://www.virtual-things.biz/',
    'description': '''        WARNING: BETA STATUS
        This module is in public testing phase and not yet released.
        Never use this module in productive environment. You can not
        uninstall this module once it is installed. Watch
        www.tryton.org/news.html for release announcements.

        Use this module only for testing purposes and submit your issues to
        http://bugs.tryton.org. Please note your testing results on
        http://code.google.com/p/tryton/wiki/Testing1_2_0#External_Modules.
        Allows the management of bank accounts for parties''',
    'description_de_DE': '''        ACHTUNG: MODUL IM BETA STATUS
        Dieses Modul befindet sich in der öffentlichen Testphase und
        ist noch nicht released. Benutzen Sie dieses Modul nicht in
        produktiven Umgebungen. Das Modul kann nicht mehr deinstalliert werden,
        nachdem es in eine Datenbank installiert wurde.
        Release Ankündigung werden auf www.tryton.org/news.html veröffentlicht.

        Benutzen Sie dieses Modul nur für Testzwecke und unterbreiten Sie
        Fehler oder Vorschläge auf http://bugs.tryton.org. Bitte vermerken Sie
        Ihre Testergebnisse auf
        http://code.google.com/p/tryton/wiki/Testing1_2_0#External_Modules.

    Ermöglicht die Verwaltung von Bankverbindungen für Parteien
''',
    #'description_es_ES': '''Banco de terceros
    #Permite la gestión de cuentas bancarias de terceros
#''',
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
