from search import search
import json
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrap Vocabulary from Dictionary App")
    parser.add_argument(
        "filepath",
        metavar="path",
        type=str,
        help="a json file path to vocabulary list.",
    )

    parser.add_argument(
        "--output",
        metavar="output",
        type=str,
        help="output file location",
        default="../html/public/data",
    )
    args = parser.parse_args()
    filepath = args.filepath
    output = args.output
    json_array = []
    with open(filepath) as json_file:
        vocabs = json.load(json_file)
        id = 0
        for n, vocab in enumerate(vocabs):
            try:
                result = search(vocab)
            except:
                print(f"word not found: {vocab}")
                pass
            if len(result["sections"]) == 1 and len(result["sections"][0][1]) == 0:
                print(f"No examples: {vocab}")
                pass
            else:
                id = id + 1
                result["id"] = id
                json_array.append(result)
        filename = os.path.basename(filepath)
        with open(f"{output}/{filename}", "w", encoding="utf8") as f:
            json.dump(json_array, f)
