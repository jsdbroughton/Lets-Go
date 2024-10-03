from src.utils.parameters import RevitRules

from src.model.structural_model import StructuralModel

class RevitModel(StructuralModel):
    """Implementation StructuralModel base class specific for Revit"""

    def load(self, model_attribute = 'elements') -> None:
        super().load(model_attribute = model_attribute)

    def data_lens(self) -> list:
        """Filter elements and prepare table of data for Speckle Data Lens"""
        data = [["id", "Type", "Material", "Grade", "Volume", "Mass"]]
        for category in self.model:
            if category.name == "Walls":
                for wall in category.elements:
                    volume = RevitRules.get_parameter_value(wall, "Volume", 0.0)
                    material = RevitRules.get_parameter_value(wall, "Structural Material", 0.0)
                    if "Concrete" in material:
                        mass = volume * 2.5
                        row_data = [wall.id, "Wall", "Concrete", material, volume, mass]
                        data.append(row_data)
                    else:
                        raise ValueError(f"Material of type {material} not anticipated.")
            elif category.name == "Floors":
                for floor in category.elements:
                    volume = RevitRules.get_parameter_value(floor, "Volume", 0.0)
                    material = RevitRules.get_parameter_value(floor, "Structural Material", 0.0)
                    if "Concrete" in material:
                        mass = volume * 2.5
                        row_data = [floor.id, "Floor", "Concrete", material, volume, mass]
                        data.append(row_data)
                    else:
                        row_data = [floor.id, "Other", None, None, None, None]
                        row_data.append(row_data)
            elif category.name == "Structural Foundation":
                for foundation in category.elements:
                    volume = RevitRules.get_parameter_value(foundation, "Volume", 0.0)
                    material = RevitRules.get_parameter_value(foundation, "Structural Material", 0.0)
                    if "Concrete" in material:
                        mass = volume * 2.5
                        row_data = [foundation.id, "Foundation", "Concrete", material, volume, mass]
                        data.append(row_data)
                    else:
                        row_data = [foundation.id, "Other", None, None, None, None]
                        row_data.append(row_data)
            elif category.name == "Structural Columns":
                for column in category.elements:
                    volume = RevitRules.get_parameter_value(column, "Volume", 0.0)
                    material = RevitRules.get_parameter_value(column, "Structural Material", 0.0)
                    if "Concrete" in material:
                        mass = volume * 2.5
                        row_data = [column.id, "Column", "Concrete", material, volume, mass]
                        data.append(row_data)
                    elif "Steel" in material:
                        mass = volume * 7.85
                        row_data = [column.id, "Column", "Steel", material, volume, mass]
                        data.append(row_data)
                    else:
                        row_data = [column.id, "Other", None, None, None, None]
                        row_data.append(row_data)
            elif category.name == "Structural Framing":
                for beam in category.elements:
                    volume = RevitRules.get_parameter_value(beam, "Volume", 0.0)
                    material = RevitRules.get_parameter_value(beam, "Structural Material", 0.0)
                    if "Concrete" in material:
                        mass = volume * 2.5
                        row_data = [beam.id, "Beam", "Concrete", material, volume, mass]
                        data.append(row_data)
                    elif "Steel" in material:
                        mass = volume * 7.85
                        row_data = [beam.id, "Beam", "Steel", material, volume, mass]
                        data.append(row_data)
                    elif "wood" in material:
                        mass = volume * 0.65
                        row_data = [beam.id, "Beam", "Timber", material, volume, mass]
                        data.append(row_data)
                    elif "Aluminum" in material:
                        mass = volume * 2.7
                        row_data = [beam.id, "Purlin", "Aluminum", material, volume, mass]
                        data.append(row_data)
                    else:
                        mass = volume * 2.7
                        row_data = [beam.id, "Compound Truss", "Timber", material, volume, mass]
                        data.append(row_data)
            else:
                for element in category.elements:
                    row_data = [element.id, "Other", None, None, None, None]
                    data.append(row_data)
        return data
