def allow_write(role: str) -> bool:
    return role == "writer"

def should_show_form(user_can_write: bool) -> bool:
    return bool(user_can_write)

def zero_dirt_on_reject() -> bool:
    return True
