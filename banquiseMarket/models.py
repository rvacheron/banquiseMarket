from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from produit.models import Produit

class LatestEntriesFeed(Feed):
    title = "Banquise market"
    link = "/"
    description = "Derniers articles ajoutés"

    def items(self):
        return Produit.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.nom

    def item_description(self, item):
        return item.descriptif

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('produit_detail', args=[item.pk])