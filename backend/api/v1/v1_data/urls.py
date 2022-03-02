from django.urls import re_path

from api.v1.v1_data.views import submit_form, list_form_data, data_answers, \
    get_map_data_point, get_chart_data_point, list_pending_form_data, \
    pending_data_answers, approve_pending_data
from api.v1.v1_users.views import health_check, get_config_file

urlpatterns = [
    re_path(r'^(?P<version>(v1))/form-data/(?P<form_id>[0-9]+)', submit_form),
    re_path(r'^(?P<version>(v1))/list/form-data/(?P<form_id>[0-9]+)',
            list_form_data),
    re_path(r'^(?P<version>(v1))/data/(?P<data_id>[0-9]+)',
            data_answers),

    re_path(r'^(?P<version>(v1))/form-pending-data/(?P<form_id>[0-9]+)',
            list_pending_form_data),
    re_path(r'^(?P<version>(v1))/pending-data/(?P<pending_data_id>[0-9]+)',
            pending_data_answers),
    re_path(r'^(?P<version>(v1))/pending-data/approve',
            approve_pending_data),

    re_path(r'^(?P<version>(v1))/maps/(?P<form_id>[0-9]+)',
            get_map_data_point),
    re_path(r'^(?P<version>(v1))/chart/data/(?P<form_id>[0-9]+)',
            get_chart_data_point),

    re_path(r'^(?P<version>(v1))/health/check', health_check),
    re_path(r'^(?P<version>(v1))/config.js', get_config_file),
]
