#!/usr/bin/python3
import json
import logging
import os

from chalicelib.core.config import settings


def override_config() -> None:
    """Override config.json"""
    directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(directory, ".chalice/config_template.json")
    output_file_path = os.path.join(directory, ".chalice/config.json")

    with open(input_file_path) as fin:
        config = json.load(fin)

    stages = config["stages"]

    for stage in stages.keys():
        config["stages"][stage]["environment_variables"] = settings.dict()

    with open(output_file_path, "w") as fout:
        json.dump(config, fout, indent=2, sort_keys=True)

    logging.info("Successfully update config file")


if __name__ == "__main__":
    override_config()
