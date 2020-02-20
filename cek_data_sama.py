###framework django
'''
Analogi no ktp yg sama.
Mengambil data jika ada no ktp yang sama, sample model namanya Konsumen
'''

from django.db.models import Count
from .models import Konsumen

cek = Konsumen.objects.values('noktp').annotate(name_count=Count('noktp')).filter(name_count__gt=1)
cek_2 = Konsumen.objects.filter( noktp__in=[item['noktp'] for item in cek ])
cek_3 = ([ int(item.id) for item in cek_2 ])
hasil = Konsumen.objects.filter(pk__in=cek_3)
