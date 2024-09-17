#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script can automatically generate blockstate and block model files for the BetterLeaves resourcepack."""

import sys
import json
import os

def main():
    mod_namespace = sys.argv[1] # Take namespace from the first argument
    block_name = sys.argv[2] # Take block name from the second argument

    # Create structure for blockstate file
    block_state_file = f"assets/{mod_namespace}/blockstates/{block_name}.json"
    block_state_data = {
        "variants": {
            "": []
        }
    }
    # Add four rotations for each of the eight individual leaf models
    for i in range(1, 9):
        block_state_data["variants"][""] += { "model": f"{mod_namespace}:block/{block_name}{i}" }, { "model": f"{mod_namespace}:block/{block_name}{i}", "y": 90 }, { "model": f"{mod_namespace}:block/{block_name}{i}", "y": 180 }, { "model": f"{mod_namespace}:block/{block_name}{i}", "y": 270 },

    # Create blockstates folder if it doesn't exist already
    if not os.path.exists("assets/{}/blockstates/".format(mod_namespace)):
        os.makedirs("assets/{}/blockstates/".format(mod_namespace))

    # Write blockstate file
    with open(block_state_file, "w") as f:
        json.dump(block_state_data, f, indent=4)


    # Create models folder if it doesn't exist already
    if not os.path.exists("assets/{}/models/block/".format(mod_namespace)):
        os.makedirs("assets/{}/models/block/".format(mod_namespace))

    # Create the eight individual leaf models
    for i in range(1, 9):
        # Create structure for block model file
        block_file = f"assets/{mod_namespace}/models/block/{block_name}{i}.json"
        block_data = {
            "parent": f"block/leaves{i}",
            "textures": {
                "0": f"{mod_namespace}:block/{block_name}"
            }
        }
        with open(block_file, "w") as f:
            json.dump(block_data, f, indent=4)

if __name__ == "__main__":
    main()