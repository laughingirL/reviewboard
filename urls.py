from django.conf import settings
from django.conf.urls.defaults import *
from reviewboard.reviews.models import ReviewRequest, Person, Group
from reviewboard.reviews.feeds import RssReviewsFeed, AtomReviewsFeed
from reviewboard.reviews.feeds import RssSubmitterReviewsFeed
from reviewboard.reviews.feeds import AtomSubmitterReviewsFeed
from reviewboard.reviews.feeds import RssGroupReviewsFeed
from reviewboard.reviews.feeds import AtomGroupReviewsFeed

rss_feeds = {
    'reviews': RssReviewsFeed,
    'submitters': RssSubmitterReviewsFeed,
    'groups': RssGroupReviewsFeed,
}

atom_feeds = {
    'reviews': AtomReviewsFeed,
    'submitters': AtomSubmitterReviewsFeed,
    'groups': AtomGroupReviewsFeed,
}

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),

    (r'^css/(.*)$', 'django.views.static.serve',
     {'document_root': settings.HTDOCS_ROOT + '/css'}),
    (r'^images/(.*)$', 'django.views.static.serve',
     {'document_root': settings.HTDOCS_ROOT + '/images'}),

    (r'^$', 'django.views.generic.simple.redirect_to',
     {'url': '/reviews/'}),

    (r'^reviews/$', 'reviewboard.reviews.views.review_list',
     {'queryset': ReviewRequest.objects.filter(public=True),
      'template_name': 'reviews/review_list.html'}),

    (r'^reviews/new/$', 'reviewboard.reviews.views.new_review_request',
     {'template_name': 'reviews/new.html',
      'changenum_path': '/reviews/new/changenum/'}),

    (r'^reviews/(?P<object_id>[0-9]+)/$',
     'django.views.generic.list_detail.object_detail',
     {'queryset': ReviewRequest.objects.all(),
      'template_name': 'reviews/review_detail.html'}),

    (r'^reviews/new/(?P<reviewreq_id>[0-9]+)/$',
      'reviewboard.reviews.views.edit_new_details',
     {'template_name': 'reviews/edit_new_details.html'}),

    (r'^submitters/$', 'reviewboard.reviews.views.submitter_list',
     {'template_name': 'reviews/submitter_list.html'}),

    (r'^submitters/(?P<username>[A-Za-z0-9_-]+)/$',
     'reviewboard.reviews.views.submitter',
     {'template_name': 'reviews/review_list.html'}),

    (r'^groups/$', 'reviewboard.reviews.views.group_list',
     {'template_name': 'reviews/group_list.html'}),

    (r'^groups/(?P<name>[A-Za-z0-9_-]+)/$',
     'reviewboard.reviews.views.group',
     {'template_name': 'reviews/review_list.html'}),

    # Feeds
    (r'^feeds/rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': rss_feeds}),
    (r'^feeds/atom/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': atom_feeds}),
)
