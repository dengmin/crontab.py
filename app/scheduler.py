
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

class Scheduler(object):

    def __init__(self):
        self._scheduler = BackgroundScheduler(executors=executors,job_defaults=job_defaults)
        self._scheduler.add_jobstore('redis', jobs_key='crontpy.jobs', run_times_key='crontpy.run_times')

    @property
    def running(self):
        return self._scheduler.running

    def start(self):
        self._scheduler.start()

    def shutdown(self, wait=True):
        self._scheduler.shutdown(wait)

    def pause(self):
        self._scheduler.pause()

    def resume(self):
        self._scheduler.resume()

    def get_jobs(self):
        return self._scheduler.get_jobs()

    def get_job(self, jid):
        return self._scheduler.get_job(job_id = jid)

    def run_job(self, jid):
        job = self.get_job(jid)
        if not job:
            raise  Exception('job id:{0} not found'.format(jid))
        job.func(*job.args, **job.kwargs)

    def resume_job(self, jid):
        self._scheduler.resume_job(job_id=jid)

    def pause_job(self, jid):
        self._scheduler.pause_job(job_id=jid)

    def modify_job(self, jid, **changes):
        return  self._scheduler.modify_job(job_id=jid, **changes)

    def delete_job(self, jid):
        self._scheduler.remove_job(job_id=jid)