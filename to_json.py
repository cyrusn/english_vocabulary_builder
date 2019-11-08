from search import search
import json

if __name__ == "__main__":
    from vocab import vocabs

    json_array = []
    for n, vocab in enumerate(vocabs):
        result = search(vocab)
        result["id"] = n + 1
        json_array.append(result)

    with open("./html/vocabs.json", "w", encoding="utf8") as f:
        json.dump(json_array, f)
