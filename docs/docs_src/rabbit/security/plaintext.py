import ssl

from faststream.rabbit import RabbitBroker
from faststream.security import SASLPlaintext

ssl_context = ssl.create_default_context()
security = SASLPlaintext(
    ssl_context=ssl_context,
    username="admin",
    password="password",  # pragma: allowlist secret
)

broker = RabbitBroker(security=security)
