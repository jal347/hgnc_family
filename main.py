from testparser3 import *
import json

if __name__ == '__main__':

    generator = load_family(".")

    # content = (x for _, x in zip(range(5), generator))
    content = list(next(generator) for x in range(5))
    # print(next(generator))
    out_file = open("myfile.json", "w")
    #
    json.dump(content, out_file, indent=4)
    #
    out_file.close()