import re
from typing import TypeVar, Generic, Union, Dict, Any

# Define generic type for Result
T = TypeVar('T')
E = TypeVar('E')

class Ok(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.is_ok = True
        self.is_err = False
    
    def unwrap(self) -> T:
        return self.value

class Err(Generic[E]):
    def __init__(self, error: E):
        self.error = error
        self.is_ok = False
        self.is_err = True
    
    def unwrap_err(self) -> E:
        return self.error

# Union type for Result
Result = Union[Ok[T], Err[E]]

def ok(value: T) -> Ok[T]:
    return Ok(value)

def err(error: E) -> Err[E]:
    return Err(error)

def parse_email(email: str) -> Result[str, Dict[str, Any]]:
    """
    Validates an email address using regex.
    
    Args:
        email: The email address to validate
        
    Returns:
        Result containing either the valid email or an error object
    """
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if re.match(email_regex, email):
        return ok(email)
    else:
        return err({"message": "Not a valid email", "code": 401})