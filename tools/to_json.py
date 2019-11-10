from search import search
import json
import sys
import os

if __name__ == "__main__":
    filepath = sys.argv[1]
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
            if len(result["sessions"]) == 1 and len(result["sessions"][0][1]) == 0:
                print(f"No examples: {vocab}")
                pass
            else:
                id = id + 1
                result["id"] = id
                json_array.append(result)
        filename = os.path.basename(filepath)
        with open(f"../html/public/data/{filename}", "w", encoding="utf8") as f:
            json.dump(json_array, f)
