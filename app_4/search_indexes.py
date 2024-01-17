from haystack import indexes
from .models import Section


class SectionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Section

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

