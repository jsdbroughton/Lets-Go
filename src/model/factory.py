from src.model.structural_model import StructuralModel
from src.model.revit import RevitModel

def model_loader(source_application: str,
                 received_object) -> StructuralModel:
    if source_application == 'Revit2024':
        return RevitModel(received_object)
    else:
        raise NotImplementedError('The proof of concept is currently limited to ETABS')
