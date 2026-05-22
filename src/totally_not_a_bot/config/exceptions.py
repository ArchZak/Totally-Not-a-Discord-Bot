# region Message Errors

class MessageOwnershipError(Exception):
    """Raised when trying to mutate a message not owned by the bot."""
    pass

# endregion