def index_shuffle(txt):
    even = "".join(txt[i] for i in range(len(txt)) if i % 2 == 0)
    odd = "".join(txt[i] for i in range(len(txt)) if i % 2 != 0)
    return even + odd

