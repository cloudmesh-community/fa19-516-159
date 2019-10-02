from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.docopts_example.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE


class Docopts_exampleCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_docopts_example(self, args, arguments):
        """
        ::

            Usage:
                docopts_example --name
                docopts_example list

          This is an example of how to use docopts.

          Arguments:
              NAME   the users name

          Options:
              -n      specify the name

        """
        arguments.NAME = arguments['--name'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.NAME:
            print("Hello,", m.list(path_expand(arguments.NAME)), "this is an example of docopts")
        else:
            print("This is an example of docopts")