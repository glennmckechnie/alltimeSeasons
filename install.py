# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)
#
# installer for the AllTimeSeasons historygenerator skin
# Copyright 2024 Glenn McKechnie : glenn.mckechnie@gmail.com

import configobj
from weecfg.extension import ExtensionInstaller

def loader():
    return AllTimeInstaller()


class AllTimeInstaller(ExtensionInstaller):
    def __init__(self):
        super(AllTimeInstaller, self).__init__(
            version="0.06",
            name='AllTimeSeasons',
            description='Alltime history tables for the Seasons skin, '
                        'or with some adjustment, other skins.',
            author="Glenn McKechnie",
            author_email="glenn.mckechnie@gmail.com",
            config={
                'StdReport': {
                    'AllTimeSeasons': {
                        'enable':'true',
                        'skin':'AllTimeSeasons',
                        'report_timing':'*/10 * * * *'
                   }}},
            files=[
                   ('bin/user',
                    ['bin/user/historygenerator.py']),
                   ('skins/AllTimeSeasons',
                    ['skins/AllTimeSeasons/histgenerator.inc.tmpl',
                     'skins/AllTimeSeasons/histgen_menu.inc',
                     'skins/AllTimeSeasons/skin.conf',
                     ])
                   ]
        )
