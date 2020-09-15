from apscheduler.schedulers.background import BackgroundScheduler
from service import operation_service, OperationService
import logging


class Schedule(object):
    def __init__(self):
        self.schedule = None

    def start_schedule(self) -> None:
        logging.info("------------ starting the schedule -----------")
        self.schedule = BackgroundScheduler(daemon=True)
        self.schedule.add_job(id='send_next_job', func=self._send_next_job_to_iot, trigger='interval', kwargs={'service': operation_service}, seconds=10)
        self.schedule.start()

    def stop_schedule(self) -> None:
        if self.schedule:
            self.schedule.shutdown()
            logging.info("-------------- stopping the schedule ------------")

    @staticmethod
    def _send_next_job_to_iot(service: OperationService) -> None:
        logging.info("--------------- scheduler sending next job -------------")
        service.get_next_operation()
