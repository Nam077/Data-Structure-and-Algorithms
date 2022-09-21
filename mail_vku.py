import re


def mail_vku(full_name: str, class_: str):
    words = word_in_sentence(full_name)
    first_name = remove_diacritics(words[-1]).lower()
    start_mail = ''
    for word in words[:-1]:
        start_mail += remove_diacritics(word)[0].lower()
    return start_mail + first_name.lower() + '.' + remove_diacritics(class_.lower()) + '@vku.udn.vn'


def word_in_sentence(sentence: str):
    return sentence.split()


# xoá dấu tiếng việt dùng regex
def remove_diacritics(text):
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ]', 'A', text)
    text = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', text)
    text = re.sub(r'[ÌÍỊỈĨ]', 'I', text)
    text = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', text)
    text = re.sub(r'[ÙÚỤỦŨƯỪỨỰỬỮ]', 'U', text)
    text = re.sub(r'[ỲÝỴỶỸ]', 'Y', text)
    text = re.sub(r'[Đ]', 'D', text)
    return text


if __name__ == '__main__':
    print("Enter full name: ")
    full_name_input = input()
    print("Enter class: ")
    class_input = input()
    print("Mail =", mail_vku(full_name_input, class_input).capitalize())
