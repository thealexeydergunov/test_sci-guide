from django.shortcuts import render
from .models import URLForProcessing, ResultFromParsing, STATUS_URL_PROCESSING


def get_main_info(request):
    urls = URLForProcessing.objects.all().order_by(
        '-start_processing')[:20].values('start_processing', 'status')
    status_list = list(map(
            lambda x: (
                x['start_processing'].strftime('%d:%m:%Y %H:%M:%S:'),
                STATUS_URL_PROCESSING.DICT[x['status']]
            ),
            urls
        ))
    results = ResultFromParsing.objects.all().order_by(
        '-created_at').select_related('url')[:20]
    results_list = list(map(
        lambda x:(
            x.url.url,
            x.title,
            x.charset,
            x.h1
        ),
        results
    ))
    context = {
        'status_list': status_list,
        'results_list': results_list
    }
    return render(request, 'base.html', context)