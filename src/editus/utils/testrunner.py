from django.conf import settings
from django.test.runner import DiscoverRunner as DjangoDiscoverRunner


class DiscoverRunner(DjangoDiscoverRunner):

    def run_tests(self, *args, **kwargs):
        if not kwargs.get('test_labels'):
            kwargs['test_labels'] = ['src']
        super(DiscoverRunner, self).run_tests(*args, **kwargs)