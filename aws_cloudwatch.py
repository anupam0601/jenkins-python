import logging
import watchtower
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler(log_group="automation_logs",
                                                  stream_name=__file__))
# logger.info("testing logs from python to cloudwatch...")
# logger.info(dict(test_status="PASS", details={"test has passed"}))

def test_cloudwatch_func():
    logger.info("testing logs from python to cloudwatch...")
    logger.info(dict(test_status="FAIL", details={"test has passed"}))


test_cloudwatch_func()
