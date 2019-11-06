import re
import sys
from DictionaryServices import DCSCopyTextDefinition


def remove_ipa(text):
    ipa_reg = r"(\|\s[美|英]\s\w+\s\|)"
    return re.sub(ipa_reg, "", text)


def remove_extra_data(text):
    removed_reg = r"(片語|衍生|同義|同義參見|反義|反義參見).*"
    return re.sub(removed_reg, "", text)


def get_ipa(text):
    ipa_reg = r"(?P<ipa>\|\s英\s(\w+)\s\|)"
    ipa = re.search(ipa_reg, text, re.MULTILINE)
    try:
        return ipa.group(2)
    except:
        return None


def split_definition_and_examples(text):
    # 完全的，徹底的 ▸ A more complete study of the subject is needed. 對這個問題需要作更加徹底的研究。
    splitted_texts = text.split("▸")
    return (
        splitted_texts[0].strip(),
        list(
            map(
                # split by chinese character
                lambda x: list(re.split(r"\s(?=[\u4e00-\ufaff]+)", x.strip())),
                splitted_texts[1:],
            )
        ),
    )


def split_list(text):
    splitted_texts = re.split(r"(\s\d{1}\s)[^a-z]", text)
    splitted_texts = list(filter(lambda x: x.find("▸") > -1, splitted_texts))
    return list(map(split_definition_and_examples, splitted_texts))


def search(vocab):
    wordrange = (0, len(vocab))
    text = DCSCopyTextDefinition(None, vocab, wordrange)
    text = remove_extra_data(text)
    result = {}
    part_of_speech_reg = (
        r"\s((?:n\.|a\.|vt\.|vi\.|ad\.|int\.|prep\.|pron\.|art\.))\s(?:\(.*?\))?"
    )
    # result["origin"] = text

    sessions = [x for x in re.split(part_of_speech_reg, text)]
    result["ipa"] = get_ipa(sessions[0])
    # re"\d$" is used to to remove some vocab have more than 1 definition.
    # e.g. aged1, aged2
    result["title"] = re.sub(r"\d$", "", remove_ipa(sessions[0]).strip())
    examples = list(map(split_list, sessions[2::2]))
    zipped = list(zip(sessions[1::2], examples))
    result["sessions"] = zipped
    return result


if __name__ == "__main__":

    # print(search("square")["origin"])
    print(search("square"))

