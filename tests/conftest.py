from logging import DEBUG, INFO, Logger, basicConfig, getLogger

from pytest import fixture


@fixture
def logger() -> Logger:
    basicConfig()
    logger = getLogger()
    logger.setLevel(DEBUG)
    getLogger("lstr").setLevel(INFO)
    return logger
