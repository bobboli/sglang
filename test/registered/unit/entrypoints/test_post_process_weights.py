import unittest

from fastapi.routing import APIRoute

from sglang.srt.entrypoints import http_server
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=5, suite="base-a-test-cpu")


class TestPostProcessWeightsRequestBinding(CustomTestCase):
    def test_payload_is_bound_from_json_body(self):
        route = next(
            route
            for route in http_server.app.routes
            if isinstance(route, APIRoute) and route.path == "/post_process_weights"
        )

        self.assertEqual(
            [param.name for param in route.dependant.body_params], ["obj"]
        )
        self.assertEqual([param.name for param in route.dependant.query_params], [])


if __name__ == "__main__":
    unittest.main()
