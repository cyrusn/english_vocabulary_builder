import re
import sys
from DictionaryServices import DCSCopyTextDefinition

special_words = {
    "wound": "wound | 美 wund | | 英 wuːnd | n. [C] (plural wounds) 1 創傷，傷；傷口；傷疤 ▸ He had a bullet wound in his chest. 他胸部有槍傷。 2 (對感情，名譽等的) 傷害，創傷 ▸ That was a wound to the child's pride. 那是對孩子自尊心的傷害。 vt. (past wounded, pp wounded, present wounding) 使受傷；傷害 ▸ The shot wounded her left arm. 子彈打傷了她的左臂。 vi. (past wounded, pp wounded, present wounding) 打傷，傷害",
    "can": "n. [C] (plural cans) 1 (食物) 罐頭 2 金屬容器 3 一罐 [（+of）] ▸ Add three cans of water to make the orange juice. 加進三罐水調橘子汁。 vt. (past canned, pp canned, present canning) 1 把（食品等）裝罐 ▸ I don't like canned food. 我不喜歡罐頭食品。 2 【美國英語 】【口語】 解僱 ",
}


def remove_ipa(text):
    ipa_reg = r"(\|\s[美|英]\s.*?\s\|)"
    return re.sub(ipa_reg, "", text)


def remove_extra_data(text):
    removed_reg = r"(片語|衍生|同義|同義參見|反義|反義參見).*"
    return re.sub(removed_reg, "", text)


def parse_ipa(text):
    ipa_reg = r"(?P<ipa>\|\s英\s(\w+)\s\|)"
    ipa = re.search(ipa_reg, text, re.MULTILINE)
    try:
        return ipa.group(2)
    except:
        return None


def split_definition_and_examples(text):
    # convert
    # 完全的，徹底的 ▸ A more complete study of the subject is needed. 對這個問題需要作更加徹底的研究。
    # to
    # ("完全的，徹底的", ()
    #   "A more complete study of the subject is needed.",
    #   "對這個問題需要作更加徹底的研究。"
    # ))
    splitted_texts = text.split("▸")
    return (
        splitted_texts[0].strip(),
        tuple(
            map(
                # split by chinese character
                lambda x: list(re.split(r"\s(?=[\u4e00-\ufaff]+)", x.strip())),
                splitted_texts[1:],
            )
        ),
    )


def split_list(text):
    # split by definition index
    splitted_texts = re.split(r"(\s\d{1}\s)(?=[^a-z])", text)
    # filter out the definition that have no examples.
    splitted_texts = list(filter(lambda x: x.find("▸") > -1, splitted_texts))
    return list(map(split_definition_and_examples, splitted_texts))


def search(vocab):
    result = {}
    if vocab in special_words.keys():
        text = special_words[vocab]
    else:
        wordrange = (0, len(vocab))
        text = DCSCopyTextDefinition(None, vocab, wordrange)
    # result["origin"] = text
    text = remove_extra_data(text)

    part_of_speech_reg = r"\s((?:n\.|a\.|vt\.|vi\.|ad\.|int\.|prep\.|pron\.|art\.|conj\.|v\.aux\.))\s(?:\(.*?\))?"

    sessions = re.split(part_of_speech_reg, text)
    result["ipa"] = parse_ipa(sessions[0])

    # re"\d$" is used to to remove some vocab have more than 1 definition.
    # e.g. aged1, aged2
    result["title"] = re.sub(r"\d$", "", remove_ipa(sessions[0]).strip())
    examples = list(map(split_list, sessions[2::2]))
    zipped = list(zip(sessions[1::2], examples))
    result["sessions"] = zipped
    return result


if __name__ == "__main__":
    # print(search("complete")['origin'])
    print(search("wound"))

