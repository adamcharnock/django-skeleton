from django.conf import settings
from django.test.runner import DiscoverRunner as DjangoDiscoverRunner


class DiscoverRunner(DjangoDiscoverRunner):

    def run_tests(self, test_labels, *args, **kwargs):
        test_labels = test_labels or ['src']
        super(DiscoverRunner, self).run_tests(test_labels, *args, **kwargs)