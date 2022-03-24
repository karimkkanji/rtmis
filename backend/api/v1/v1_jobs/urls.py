from django.urls import re_path

from api.v1.v1_jobs.views import download_generate, download_status, \
    download_file

urlpatterns = [
    re_path(r'^(?P<version>(v1))/download/generate', download_generate),
    re_path(r'^(?P<version>(v1))/download/status/(?P<task_id>.*)$',
            download_status),
    re_path(r'^(?P<version>(v1))/download/file/(?P<file_name>.*)$',
            download_file),
]