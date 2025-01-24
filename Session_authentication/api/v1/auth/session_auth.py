#!/usr/bin/env python3
"""
SessionAuth module
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Class for managing Session API authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = user_id
        return session_id
