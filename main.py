from starknet_py.abi.v2.parser import AbiParser
import json
import timeit

file = open("abi.json", "r")
abi = json.load(file)
abi_parser = AbiParser(abi)


def parse_with_timer():
    abi_parser.parse()


execution_time = timeit.timeit(parse_with_timer, number=1)
print(f"Execution time: {execution_time} seconds")

file.close()
