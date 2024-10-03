from abc import ABC, abstractmethod

class StructuralModel(ABC):
    """StructuralModel base class"""

    def __init__(self, received_object):
        self.received_object = received_object
        self.model: 'Model' = None

    def load(self, model_attribute: str) -> None:
        """Load the model object from a given commit (i.e. received_object)"""
        model = getattr(self.received_object, model_attribute, None)
        if not model:
            raise ValueError(f'"{model_attribute}" not found in commit')
        self.model = model

    @abstractmethod
    def data_lens(self):
        """Filter elements and prepare table of data for Speckle Data Lens"""