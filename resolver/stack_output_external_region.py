import shlex

from sceptre.resolvers.stack_output import StackOutputBase

class StackOutputExternalRegion(StackOutputBase):
    def __init__(self, *args, **kwargs):
        super(StackOutputExternalRegion, self).__init__(*args, **kwargs)

    def resolve(self):
        self.logger.debug(
            "Resolving external Stack output: {0}".format(self.argument)
        )

        profile = None
        arguments = shlex.split(self.argument)

        stack_argument = arguments[0]
        region = arguments[1]
        if len(arguments) > 2:
            profile = arguments[2]

        dependency_stack_name, output_key = stack_argument.split("::")
        return self._get_output_value(
            dependency_stack_name, output_key, profile, region
        )
