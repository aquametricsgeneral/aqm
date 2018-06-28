import django_tables2 as tables
from .models import Post
from django_tables2.utils import A  # alias for Accessor
#from django_utils.safestring import mark_safe
#from django_urls import reverse

class PostTable(tables.Table):
    edit = tables.LinkColumn('post_detail', text='Edit', args=[A('pk')], orderable=False, empty_values=())

    class Meta:
        model = Post
        template_name = 'django_tables2/bootstrap.html'
        fields = ( 'published_date','title', 'text')