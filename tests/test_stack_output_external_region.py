import pytest
from mock import MagicMock, patch

from sceptre.connection_manager import ConnectionManager
from sceptre.resolvers.stack_output_external_region import StackOutputExternalRegion
from sceptre.stack import Stack

class TestStackOutputExternalRegionResolver(object):

    @patch(
        "sceptre.resolvers.stack_output.StackOutputExternalRegion._get_output_value"
    )
    def test_resolve(self, mock_get_output_value):
        stack = MagicMock(spec=Stack)
        stack.dependencies = []
        stack._connection_manager = MagicMock(spec=ConnectionManager)
        stack_output_external_resolver = StackOutputExternalRegion(
            "another/account-vpc::VpcId us-east-1", stack
        )
        mock_get_output_value.return_value = "output_value"
        stack_output_external_resolver.resolve()
        mock_get_output_value.assert_called_once_with(
            "another/account-vpc", "VpcId", None, "us-east-1"
        )
        assert stack.dependencies == []

    @patch(
        "sceptre.resolvers.stack_output.StackOutputExternalRegion._get_output_value"
    )
    def test_resolve_with_profile(self, mock_get_output_value):
        stack = MagicMock(spec=Stack)
        stack.dependencies = []
        stack._connection_manager = MagicMock(spec=ConnectionManager)
        stack_output_external_resolver = StackOutputExternalRegion(
            "another/account-vpc::VpcId us-east-1 my-other-profile", stack
        )
        mock_get_output_value.return_value = "output_value"
        stack_output_external_resolver.resolve()
        mock_get_output_value.assert_called_once_with(
            "another/account-vpc", "VpcId", "my-other-profile", "us-east-1"
        )
        assert stack.dependencies == []
