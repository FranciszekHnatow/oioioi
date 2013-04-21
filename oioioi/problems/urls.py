from django.conf.urls import patterns, include, url

urlpatterns = patterns('oioioi.problems.views',
    url(r'^statement/(?P<statement_id>\d+)/$', 'show_statement_view',
        name='show_statement'),
    url(r'^problem_attachment/(?P<attachment_id>\d+)/$',
        'show_problem_attachment_view', name='show_problem_attachment'),

)
