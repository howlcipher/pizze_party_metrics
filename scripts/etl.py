import asyncio
import logging

from scripts.etl.main import ETLPipeline
from scripts import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

FALLBACK_VELOCITIES = config.FALLBACK_VELOCITIES
SETUP_REPOS = config.SETUP_REPOS

if __name__ == '__main__':
    asyncio.run(ETLPipeline().run())
