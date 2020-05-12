from celery.decorators import task
from celery.utils.log import get_task_logger
from .master import exec_command

logger = get_task_logger(__name__)


@task(name="async_update_database")
def async_update_database(post_data):
    """sends an email when feedback form is filled successfully"""
    logger.info("Executing command for update")
    ans = exec_command(post_data)
    logger.info(f"Executed with result {ans}")


