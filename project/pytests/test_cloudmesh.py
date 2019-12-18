################################################
# Austin Zebrowski
# test the list of running VMs
#
# pytest -q test_cloudmesh.py
#
################################################

from cloudmesh.common.util import HEADING
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.debug import VERBOSE
from cloudmesh.mongo.CmDatabase import CmDatabase
from cloudmesh.common.Shell import Shell


class TestCloudmesh:

    def test_aws_list(self):
        HEADING()
        Benchmark.Start()
        Shell.execute("cms init", shell=True)
        Shell.execute("cms set cloud=aws", shell=True)
        list = Shell.execute("cms vm list --refresh", shell=True)
        Benchmark.Stop()
        VERBOSE(list)

    def test_azure_list(self):
        HEADING()
        Benchmark.Start()
        Shell.execute("cms init", shell=True)
        Shell.execute("cms set cloud=azure", shell=True)
        list = Shell.execute("cms vm list --refresh", shell=True)
        Benchmark.Stop()
        VERBOSE(list)


    def test_benchmark(self):
        Benchmark.print()
