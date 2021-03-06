#!/usr/bin/env python
from cms.test_utils.cli import configure
from cms.test_utils.tmpdir import temp_dir
import os

def main():
    with temp_dir() as STATIC_ROOT:
        with temp_dir() as MEDIA_ROOT:
            configure(
                'sqlite://localhost/cmstestdb.sqlite',
                ROOT_URLCONF='cms.test_utils.project.urls',
                STATIC_ROOT=STATIC_ROOT,
                MEDIA_ROOT=MEDIA_ROOT,
            )
            from django.core.management import call_command
            os.chdir('cms')
            call_command('compilemessages', all=True)

if __name__ == '__main__':
    main()
