Doc : https://apscheduler.readthedocs.io/en/3.x/userguide.html

## Installation 
```
$ pip install apscheduler
```

## APScheduler  4 components

- Triggers contain the scheduling logic. Each job has its own trigger which determines when the job should be run next. Beyond their initial configuration, triggers are completely stateless.

- Job stores house the scheduled jobs. The default job store simply keeps the jobs in memory, but others store them in various kinds of databases. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it. Job stores (other than the default one) don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs in the backend. Job stores must never be shared between schedulers.

- Executors are what handle the running of the jobs. They do this typically by submitting the designated callable in a job to a thread or process pool. When the job is done, the executor notifies the scheduler which then emits an appropriate event.

- Schedulers are what bind the rest together. You typically have only one scheduler running in your application. The application developer doesn’t normally deal with the job stores, executors or triggers directly. Instead, the scheduler provides the proper interface to handle all those. Configuring the job stores and executors is done through the scheduler, as is adding, modifying and removing jobs.


## Choosing a scheduler
- BlockingScheduler: use when the scheduler is the only thing running in your process
- BackgroundScheduler: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
- AsyncIOScheduler: use if your application uses the asyncio module
- GeventScheduler: use if your application uses gevent
- TornadoScheduler: use if you’re building a Tornado application
- TwistedScheduler: use if you’re building a Twisted application
- QtScheduler: use if you’re building a Qt application

```
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def my_monthly_task():
    print(f"Monthly task is running at {datetime.now()}")

# Create a scheduler
scheduler = BackgroundScheduler(timezone=utc)

# Schedule the task to run on the 1st day of every month at 9:00 AM
scheduler.add_job(my_monthly_task, 'cron', day=1, hour=9, minute=0)

# Start the scheduler
scheduler.start()

try:
    # Keep the script running
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
```    
    
    
