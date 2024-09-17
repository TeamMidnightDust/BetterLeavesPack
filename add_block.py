#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script can automatically generate blockstate and block model files for the Better Leaves resourcepack."""

import argparse
import json
import os

def generate(mod_namespace, block_name, notint):

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

    base_model = "leaves"
    if (notint):
        base_model = "leaves_notint"
    # Create the eight individual leaf models
    for i in range(1, 9):
        # Create structure for block model file
        block_model_file = f"assets/{mod_namespace}/models/block/{block_name}{i}.json"
        block_model_data = {
            "parent": f"block/{base_model}{i}",
            "textures": {
                "0": f"{mod_namespace}:block/{block_name}"
            }
        }
        with open(block_model_file, "w") as f:
            json.dump(block_model_data, f, indent=4)

def generateItemModel(mod_namespace, block_name):
    # Create models folder if it doesn't exist already
    if not os.path.exists("assets/{}/models/item/".format(mod_namespace)):
        os.makedirs("assets/{}/models/item/".format(mod_namespace))

    item_model_file = f"assets/{mod_namespace}/models/item/{block_name}.json"
    item_model_data = {
        "parent": f"{mod_namespace}:block/{block_name}1"
    }
    with open(item_model_file, "w") as f:
        json.dump(item_model_data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description='This script can automatically generate blockstate and block model files for the Better Leaves resourcepack.',
                    epilog='Feel free to ask for help at http://discord.midnightdust.eu/')

    parser.add_argument('--item', '-i', action='store_true')
    parser.add_argument('--notint', '-n', action='store_true')
    parser.add_argument('namespace', type=str) # Take namespace from the first argument
    parser.add_argument('block_names', nargs='+') # Take block names from the following arguments
    args = parser.parse_args()

    print(args)
    print()

    for block_name in args.block_names:
        if not args.item:
            print(f"Generating blockstate and block model for {args.namespace}:{block_name}")
            generate(args.namespace, block_name, args.notint)
        else:
            print(f"Generating item model for {args.namespace}:{block_name}")
            generateItemModel(args.namespace, block_name)