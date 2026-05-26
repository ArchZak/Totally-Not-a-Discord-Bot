# region Category Errors


class CategoryNotFoundError(Exception):
    """Raised when a category with the specified ID is not found."""


# endregion

# region Channel Errors


class ChannelNotFoundError(Exception):
    """Raised when a channel with the specified ID is not found."""


# endregion

# region Enforcement Errors

# endregion

# region Message Errors


class MessageOwnershipError(Exception):
    """Raised when trying to mutate a message not owned by the bot."""


# endregion

# region Role Errors


class RoleNotFoundError(Exception):
    """Raised when a role with the specified ID is not found."""


# endregion


# region Guild Errors


class GuildNotFoundError(Exception):
    """Raised when a guild with the specified ID is not found."""


class MemberNotFoundError(Exception):
    """Raised when a user with the specified ID is not found."""

# endregion
