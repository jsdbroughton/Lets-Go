from typing import Any
from specklepy.objects.base import Base

class RevitRules:

    @staticmethod
    def get_parameter_value(
        speckle_object: Base,
        parameter_name: str,
        default_value: Any = None,
    ) -> Any | None:
        """
        Retrieves the value of the specified Revit parameter from the speckle_object.

        This method checks if the speckle_object has a parameter with the specified name,
        considering the following cases:
        1. The parameter is a named property at the root object level.
        2. The parameter is stored as a key in the "parameters" dictionary.
        3. The parameter is stored as a nested dictionary within the "parameters" property,
           and the parameter name is stored as the value of the "name" property within each nested dictionary.

        If the parameter exists and its value is not None or the specified default_value, it returns the value.
        If the parameter does not exist or its value is None or the specified default_value, it returns None.

        Args:
            speckle_object (Base): The Speckle object to retrieve the parameter value from.
            parameter_name (str): The name of the parameter to retrieve the value for.
            default_value: The default value to compare against. If the parameter value matches this value,
                           it will be treated the same as None.

        Returns:
            The value of the parameter if it exists and is not None or the specified default_value, or None otherwise.
        """
        # Attempt to retrieve the parameter from the root object level
        value = getattr(speckle_object, parameter_name, None)
        if value not in [None, default_value]:
            return value

        # If the "parameters" attribute is a Base object, extract its dynamic members
        parameters = getattr(speckle_object, "parameters", None)
        if parameters is None:
            return None

        # Prepare a dictionary of parameter values from the dynamic members of the parameters attribute
        parameters_dict = {
            key: getattr(parameters, key)
            for key in parameters.get_dynamic_member_names()
        }

        # Search for a direct match or a nested match in the parameters dictionary
        param_value = parameters_dict.get(parameter_name)
        if param_value is not None:
            if isinstance(param_value, Base):
                # Extract the nested value from a Base object if available
                nested_value = getattr(param_value, "value", None)
                if nested_value not in [None, default_value]:
                    return nested_value
            elif param_value not in [None, default_value]:
                return param_value

        # Use a generator to find the first matching 'value' for shared parameters stored in Base objects
        return next(
            (
                getattr(p, "value", None)
                for p in parameters_dict.values()
                if isinstance(p, Base) and getattr(p, "name", None) == parameter_name
            ),
            None,
        )
