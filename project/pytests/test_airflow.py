################################################
# Austin Zebrowski
#
# test that there are dags available
# test that the dags have tasks
#
# pytest -q test_airflow.py
#
################################################

from cloudmesh.common.util import HEADING
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.debug import VERBOSE
from airflow.models import DagBag


class TestAirflow:

    def test_dags(self):
        HEADING()
        Benchmark.Start()
        self.dagbag = DagBag()
        VERBOSE("counting errors in dags")
        errors = len(self.dagbag.import_errors)
        Benchmark.Stop()
        assert errors == 0

    def test_task_counts(self):
        dag_id="cloudmesh_vm_boot"
        self.dagbag = DagBag()
        dag = self.dagbag.get_dag(dag_id)
        assert len(dag.tasks) > 0

    def test_benchmark(self):
        Benchmark.print()
