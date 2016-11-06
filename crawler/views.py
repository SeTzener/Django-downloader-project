from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import RootUrl, ItemUrl


def index(request):
    latest_url_list = RootUrl.objects.order_by('-last_update_date')
    context = {
        'latest_url_list': latest_url_list,
    }
    return render(request, 'crawler/index.html', context)
    
def detail(request, item_url_id):
    item_url = get_object_or_404(RootUrl, pk=item_url_id)
    files = item_url.fileExtract()
    if files != []:
        list_len = len(files)
        {'file': files, 'list_len': list_len}
    elif files == []:
        list_len = 'There are no '
        {'file': files, 'list_len': list_len}
    else: 
        files = ["There are no files to extract in this site."]
    return render(request, 'crawler/detail.html', {'item_url': item_url, 'files': files, 'list_len': list_len})
    
def download(request, item_url_id):
    item = get_object_or_404(RootUrl, pk=item_url_id)
    selected_url = item.fileExtract()
    counter = 0
    for file in selected_url:
        try:
            download = item.download(file)
        except IOError:
            continue
        else:
            counter += 1
            item_name = str(item.name) + " item " + str(counter)
            new_item = ItemUrl(item_url=RootUrl.objects.get(pk=item_url_id), item_content=item_name, acquired_date=timezone.now())
            new_item.save()
    return render(request, 'crawler/download.html', {'item': item, 'download':download})
