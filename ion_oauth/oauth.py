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

from typing import Any, Dict, List
from social_core.backends.oauth import BaseOAuth2

class IonOauth2(BaseOAuth2):  # pylint: disable=abstract-method
    name = "ion"
    AUTHORIZATION_URL = "https://ion.tjhsst.edu/oauth/authorize"
    ACCESS_TOKEN_URL = "https://ion.tjhsst.edu/oauth/token"
    ACCESS_TOKEN_METHOD = "POST"
    EXTRA_DATA = [("refresh_token", "refresh_token", True), ("expires_in", "expires")]

    def get_scope(self) -> List[str]:
        return ["read"]

    def get_user_details(self, response: Dict[str, Any]) -> Dict[str, Any]:
        profile = self.get_json(
            "https://ion.tjhsst.edu/api/profile", params={"access_token": response["access_token"]}
        )
        # fields used to populate/update User model
        data = {
            key: profile[key]
            for key in ("first_name", "last_name", "id", "is_student", "is_teacher")
        }
        data["username"] = profile["ion_username"]
        data["email"] = profile["tj_email"]
        return data

    def get_user_id(self, details: Dict[str, Any], response: Any) -> int:
        return details["id"]