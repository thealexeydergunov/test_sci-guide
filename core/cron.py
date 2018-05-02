from django_cron import CronJobBase, Schedule
from .models import (URLForProcessing, ResultFromParsing,
                     CronSettings, STATUS_CRON, STATUS_URL_PROCESSING)
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class ParseURLs(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.parse_urls'

    def do(self):
        setting, created = CronSettings.objects.get_or_create(code=self.code)
        if setting.status_cron == STATUS_CRON.WAIT:
            setting.status_cron = STATUS_CRON.PROCESS
            setting.save()
            try:
                url_objs = URLForProcessing.objects.filter(
                    status=STATUS_URL_PROCESSING.WAIT,
                    start_processing__lte=datetime.now()
                ).order_by('start_processing')
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; '
                                  'Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
                }
                for url_obj in url_objs:
                    url_obj.status = STATUS_URL_PROCESSING.PROCESS
                    url_obj.save()
                    r = requests.get(url_obj.url, headers=headers)
                    if r.status_code != 200:
                        url_obj.status = STATUS_URL_PROCESSING.ERROR
                        url_obj.save()
                        continue
                    charset = r.encoding
                    soup = BeautifulSoup(r.content, 'html.parser')
                    title = soup.title.string
                    h1 = '; '.join(map(lambda x: x.text, soup.find_all('h1')))
                    ResultFromParsing.objects.create(
                        url=url_obj,
                        title=title,
                        charset=charset,
                        h1=h1
                    )
                    url_obj.status = STATUS_URL_PROCESSING.SUCCESS
                    url_obj.save()
            finally:
                setting.status_cron = STATUS_CRON.WAIT
                setting.save()
