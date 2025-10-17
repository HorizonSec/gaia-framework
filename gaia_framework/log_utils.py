"""
Shared logging utilities for GAIA Framework.
"""

import logging


def setup_logger(name, level=logging.INFO):
    """Set up a logger with the specified name and level.
    
    Args:
        name: Name of the logger.
        level: Logging level (default: INFO).
    
    Returns:
        Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger
