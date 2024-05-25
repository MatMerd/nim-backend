import logging

import uvicorn
import uvloop


if __name__ == "__main__":
    uvloop.install()
    logger = logging.getLogger("app")
    logger.info("Starting mgw-black-mirror")
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=3000,
        log_level="debug",
        reload=True,
    )
