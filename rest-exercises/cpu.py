import platform
import re
import subprocess
import os

from cpuinfo import get_cpu_info
from flask import jsonify


def get_processor_name():

    pinfo = get_cpu_info()

    processor_name = pinfo["brand"]

    return jsonify(model=processor_name)


def get_cache_sizes(cache_level: str) -> str:

    cinfo = get_cpu_info()

    l2_cache_size = cinfo["l2_cache_size"]
    l3_cache_size = cinfo["l3_cache_size"]

    if cache_level == 'l2':
	
        caches = {
	        'l2': l2_cache_size
        }
		
    elif cache_level == 'l3':
        caches = {
	        'l3': l3_cache_size
        }
		
    else:
        caches = {
	        'l2': l2_cache_size,
	        'l3': l3_cache_size
        }	

    return jsonify(caches=caches)

def get_both_cache_sizes():

    cinfo = get_cpu_info()

    l2_cache_size = cinfo["l2_cache_size"]
    l3_cache_size = cinfo["l3_cache_size"]

    caches = {
	    'l2': l2_cache_size,
	    'l3': l3_cache_size
    }	

    return jsonify(caches=caches)
