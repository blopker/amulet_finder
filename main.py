import hashlib
from itertools import product

amulet = b"So it goes."
rarity = 7  # Epic rarity
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


def get_hash(amulet):
    m = hashlib.sha256()
    m.update(amulet)
    return m.hexdigest()


def check_amulet(amulet):
    c = amulet.decode("utf-8")
    h = get_hash(amulet)
    return ("8" * rarity in str(h), h, amulet, c)


def gen_amulets(amulet, rarity=rarity):
    min_len = 0
    repeat = 1
    while min_len <= 64:
        p = product(whitespace_chars, repeat=repeat)
        repeat += 1
        loop_min_len = 100
        for a in p:
            d = check_amulet(amulet + "".join(a).encode("utf-8"))
            length = len(d[-1].encode("utf-8"))
            if length < loop_min_len:
                loop_min_len = length
            if d[0]:
                print(d[-1])
        min_len = loop_min_len


if __name__ == "__main__":
    assert get_hash(amulet) == test_sha
    assert not check_amulet(amulet)[0]
    gen_amulets(amulet, rarity=rarity)
