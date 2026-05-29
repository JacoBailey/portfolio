from loguru import logger

logger.add(
    "logs/portfolio.log",
    rotation="10 MB",
    retention="10 MB",
    level="INFO"
)