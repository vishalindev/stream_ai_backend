import logging


def configure_logging() -> None:
    """Configure process-wide logging for the monolithic API."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
