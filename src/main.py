from config.settings import (
    PROJECT_NAME,
    PROJECT_VERSION,
    PROJECT_ROOT,
)

from src.utils.logger import get_logger


logger = get_logger("quant_platform")


def main() -> None:
    logger.info("Starting %s", PROJECT_NAME)
    logger.info("Version: %s", PROJECT_VERSION)
    logger.info("Project root: %s", PROJECT_ROOT)
    logger.info("Quant research platform initialized successfully.")


if __name__ == "__main__":
    main()