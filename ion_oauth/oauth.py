# -*- coding: utf-8 -*-
# Copyright (C) 2016 Peter Foley
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from social.backends.oauth import BaseOAuth2


class IonOauth2(BaseOAuth2):
    name = 'Ion'
    AUTHORIZATION_URL = 'https://ion.tjhsst.edu/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://ion.tjhsst.edu/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        profile = self.get_json('https://ion.tjhsst.edu/api/profile',
                                params={'access_token': response['access_token']})
        return {'username': profile['ion_username'],
                'id': profile['id'],
                'email': profile['tj_email'],
                'fullname': profile['full_name'],
                'first_name': profile['first_name'],
                'last_name': profile['last_name']}

    def get_user_id(self, details, response):
        return details['id']
