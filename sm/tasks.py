from celery.decorators import task
from celery.utils.log import get_task_logger
from .master import exec_command
from .facedetection import eval_faces

logger = get_task_logger(__name__)


@task(name="async_update_database")
def async_update_database(post_data):
    logger.info("Executing command for update")
    ans = exec_command(post_data)
    logger.info(f"Executed with result {ans}")



@task(name="async_eval_faces")
def async_eval_faces():
    logger.info("Executing command for face-evaluation")
    try:
        eval_faces()
        logger.info(f"Executed with result ok")
    except (Exception, ValueError) as e:
        logger.info(f"Executed with result {str(e)}")







