import jsonschema
from jsonschema import validate

# Describe what kind of json you expect.
tripSchema = {
    "type": "object",
    "required": [ "region", "origin_coord","destination_coord","datetime","datasource"],
    "properties": {
        "region": {"type": "string"},
        "origin_coord": {"type": "string"},
        "destination_coord": {"type": "string"},
        "datetime": {"type": "string"},
        "datasource": {"type": "string"}
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=tripSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

