from src.model.factory import model_loader


def bjorn_magic(received_object) -> list:

    structural_model = model_loader("Revit2024", received_object)
    structural_model.load()
    return structural_model.data_lens()