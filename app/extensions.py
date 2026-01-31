import logging
import os

def setup_logging(app):
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=app.config["LOG_LEVEL"],
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    app.logger.info("Logging system initialized")
