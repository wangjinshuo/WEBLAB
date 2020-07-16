from datetime import date
from Data_Mind.models import BookInfo


def savebook():
    book=BookInfo(btitle='三国',
              bpub_date=date(1996,5,6),
              bread=18,
              bcomment=32)
    book.save()

def findallbook():
    all_entries = BookInfo.objects.all()
    name = list(all_entries.values_list('btitle', flat=True))
    nums = list(all_entries.values_list('bcomment', flat=True))
    ret = {'name': name, 'num': nums}
    return ret
