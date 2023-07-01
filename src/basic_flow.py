from prefect import flow, get_run_logger


@flow(name="Demo")
def basic_flow():
    logger = get_run_logger()
    logger.warning("Hello from basic_flow.py")


if __name__ == "__main__":
    basic_flow()
