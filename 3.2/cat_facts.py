import httpx
from prefect import flow, task

# will try up to 4 times with a short time delay inbetween, any print statements will be in the logs
@task(retries=4, retry_delay_seconds=0.1, log_prints=True)
def fetch_cat_fact():
    cat_fact = httpx.get("https://f3-vyx5c2hfpq-ue.a.run.app/")
    #An endpoint that is designed to fail sporadically
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)

# simple flow that just calls a task
@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()