"""This module contains the function's business logic.

Use the automation_context module to wrap your function in an Automate context helper.
"""

from pydantic import Field, SecretStr
from speckle_automate import (
    AutomationContext,
    execute_automate_function,
)

from flatten import flatten_base

from src import function


def automate_function_without_inputs(
    automate_context: AutomationContext
) -> None:
    """This is an example Speckle Automate function.

    Args:
        automate_context: A context-helper object that carries relevant information
            about the runtime context of this function.
            It gives access to the Speckle project data that triggered this run.
            It also has convenient methods for attaching result data to the Speckle model.
        function_inputs: An instance object matching the defined schema.
    """
    # The context provides a convenient way to receive the triggering version.
    version_root_object = automate_context.receive_version()

    function.bjorn_magic(version_root_object)

    automate_context.mark_run_success("No forbidden types found.")

    # If the function generates file results, this is how it can be
    # attached to the Speckle project/model
    # automate_context.store_file_result("./report.pdf")


# make sure to call the function with the executor
if __name__ == "__main__":
    # NOTE: always pass in the automate function by its reference; do not invoke it!

    # Pass in the function reference with the inputs schema to the executor.
    execute_automate_function(automate_function_without_inputs)