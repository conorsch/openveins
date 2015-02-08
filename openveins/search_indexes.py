import datetime
from haystack import indexes
from openveins.models import Quote


class QuoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    quote_text = indexes.CharField(model_attr='text')
    post_date = indexes.DateTimeField(model_attr='post_date')

    def get_model(self):
        return Quote

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
