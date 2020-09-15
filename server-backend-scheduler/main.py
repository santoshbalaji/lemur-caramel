import logging
from dao import disconnect_database
from schedule import Schedule
from service import mqtt_connection

schedule = None


def main() -> None:
    global schedule
    schedule = Schedule()
    schedule.start_schedule()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
    text = ''
    while text != 'y':
        text = input("Enter y to stop the process")
    schedule.stop_schedule()
    mqtt_connection.close()
    disconnect_database()

