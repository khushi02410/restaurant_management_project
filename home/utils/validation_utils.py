import logging
from email.utils import parseaddr
from django.core.validators import validate_email
from django.core.exception import ValidationError

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    try:
        if "@" not in parseaddr(email)[1]:
            return False

        validate_email(email)
        return True

    except ValidationError as e:
        logger.warning(f"Invalid email provided: {email} | Error: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while validating email: {e}")
        return False    