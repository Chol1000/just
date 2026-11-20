"""User roles and the permissions each role holds.

The role chosen at startup is stored with every record it creates
(the ``created_by`` column), and the service layer checks the role's
permissions before any create, update, or delete operation runs.
"""

from enum import Enum


class Role(Enum):
    ORGANIZER = "Community Cultural Organizer"
    GROUP_LEADER = "Cultural Group Leader"
    VOLUNTEER = "Local Heritage Volunteer"


class Permission(Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


_ALL_PERMISSIONS = frozenset(Permission)

ROLE_PERMISSIONS = {
    Role.ORGANIZER: _ALL_PERMISSIONS,
    Role.GROUP_LEADER: _ALL_PERMISSIONS,
    # Volunteers can record and view heritage information but cannot
    # change or remove records that others have created.
    Role.VOLUNTEER: frozenset({Permission.CREATE, Permission.READ}),
}


def has_permission(role: Role, permission: Permission) -> bool:
    """Return True if ``role`` is allowed to perform ``permission``."""
    return permission in ROLE_PERMISSIONS[role]
