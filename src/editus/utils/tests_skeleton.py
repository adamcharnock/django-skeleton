""" Run tests for skeleton app

This must be run directly thusly:

    python src/editus/utils/tests_skeleton.py

IMPORTANT: This doesn't use the test db or dummy email sending.
           It will actually do things in order to ensure you
           have everything setup correctly.

"""

from celery.result import AsyncResult
from django.conf import settings
import unittest
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
import requests
from termcolor import colored

if __name__ == '__main__':

    @unittest.skipUnless(settings.DEBUG, "Only available in debug mode")
    class RealWorldTestCase(unittest.TestCase):

        def test_celery(self):
            from editus.celery import debug_task
            result = debug_task.delay()
            self.assertIsInstance(result, AsyncResult)
            result.wait(timeout=3)
            self.assertEqual(result.result, 'Done',
                             "The task 'debug_task' returned an unxpected value")
            self.assertEqual(result.state, 'SUCCESS',
                             "The task 'debug_task' failed to run successfully")

        def test_registration(self):
            response = requests.get('http://127.0.0.1:8000/accounts/register/')
            self.assertEqual(response.status_code, 200,
                             "Bad response from registration page at "
                             "http://127.0.0.1:8000/accounts/register/")

        def test_django_ses(self):
            result = send_mail('Skeleton test email', 'Message content.', settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
            result = result[0]
            self.assertIsInstance(result, AsyncResult)
            result.wait(timeout=3)
            self.assertEqual(result.state, 'SUCCESS',
                             "Email failed to send. State was: %s" % result.state)

            print(colored(
                "A test email should be received by %s shortly" % settings.DEFAULT_FROM_EMAIL,
                'green'
            ))

        def test_docs(self):
            response = requests.get('http://127.0.0.1:8001')
            self.assertEqual(response.status_code, 200,
                             "Bad response from docs at http://127.0.0.1:8001")


    unittest.main()