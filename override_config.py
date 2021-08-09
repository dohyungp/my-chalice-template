#!/usr/bin/python3
import json
import logging
import os


def override_config() -> None:
    """Override config.json"""
    directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(directory, ".chalice/config.json")

    with open(config_file_path) as fin:
        config = json.load(fin)

    stages = config["stages"]

    for stage in stages.keys():
        config["stages"][stage]["environment_variables"] = {
            key: os.environ.get(key, value) for key, value in stages[stage]["environment_variables"].items()
        }

    with open(config_file_path, "w") as fout:
        json.dump(config, fout, indent=2, sort_keys=True)

    logging.info("Successfully update config file")


if __name__ == "__main__":
    override_config()
