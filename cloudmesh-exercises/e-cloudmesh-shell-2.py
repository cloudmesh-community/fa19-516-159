from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.Austin.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class AustinCommand(PluginCommand):

	# noinspection PyUnusedLocal
	
	def do_Austin():
		print("This is my new command... Hello world!")
		
	do_Austin()