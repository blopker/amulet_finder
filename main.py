import hashlib
from itertools import product

inp = b"So it goes."
rarity = 6  # Epic rarity
test_sha = "314a1c2d9193afbc99b86a1e2d92811ea00cb857b37255ee9221294c6209b6cd"
whitespace_chars = {
    "\u0020",
    "\u00A0",
    "\u180E",
    "\u2000",
    "\u2001",
    "\u2002",
    "\u2003",
    "\u2004",
    "\u2005",
    "\u2006",
    "\u2007",
    "\u2008",
    "\u2009",
    "\u200A",
    "\u200B",
    "\u202F",
    "\u205F",
    "\u3000",
    "\uFEFF",
}


def get_hash(inp):
    m = hashlib.sha256()
    m.update(inp)
    return m.hexdigest()


def check_amulet(inp):
    c = inp.decode("utf-8")
    h = get_hash(inp)
    return ("8" * rarity in str(h), h, inp, c)


def gen_amulets(inp, rarity=rarity):
    min_len = 0
    repeat = 1
    while min_len < 64:
        p = product(whitespace_chars, repeat=repeat)
        repeat += 1
        loop_min_len = 100
        for a in p:
            d = check_amulet(inp + "".join(a).encode("utf-8"))
            length = len(d[-1].encode("utf-8"))
            if length < loop_min_len:
                loop_min_len = length
            if d[0]:
                print(d[-1])
        min_len = loop_min_len


if __name__ == "__main__":
    assert get_hash(inp) == test_sha
    assert not check_amulet(inp)[0]
    gen_amulets(inp, rarity=rarity)
