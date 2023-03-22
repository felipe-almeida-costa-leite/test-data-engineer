from enum import Enum


class JsonSchemaLoad(Enum):
    schema = {
        "all": {
            "type": "boolean"
        },
        "at_date": {
            "type": "object",
            "properties": {
                "start": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string"
                        },
                        "condition": {
                            "type": "string"
                        }
                    }
                },
                "end": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string"
                        },
                        "condition": {
                            "type": "string"
                        }
                    }
                },
                "reverser": {
                    "type": "boolean"
                },
                "format": {
                    "type": {
                        "enum": ["batch", "stream", "analysis"]
                    }
                }
            }
        }
    }
