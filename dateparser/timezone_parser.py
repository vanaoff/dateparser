# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta
from math import ceil

from dateparser.timezones import timezone_info_list

HOUR = 3600


def get_tz_offsets():
    return {re.compile(r'\b%s$' % tz_info[0]): timedelta(seconds=tz_info[1]) for tz_info in timezone_info_list}


def pop_tz_offset_from_string(date_string):
    for timezone_re, offset in _tz_offsets.iteritems():
        if timezone_re.search(date_string):
            date_string = timezone_re.sub('', date_string).rstrip()
            return date_string, offset
    else:
        return date_string, None


def convert_to_local_tz(datetime_obj, datetime_tz_offset):
    return datetime_obj - datetime_tz_offset + local_tz_offset


def get_local_tz_offset():
    delta = datetime.now() - datetime.utcnow()
    days, seconds, microseconds = delta.days, delta.seconds, delta.microseconds
    return timedelta(seconds=days * 24 * HOUR + seconds + ceil(microseconds / 1000000.0))


_tz_offsets = get_tz_offsets()
local_tz_offset = get_local_tz_offset()
