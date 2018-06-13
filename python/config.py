
EXPERT_RULES = {
    # stat:   cla    inst   p1     p2       len
    0x6700: [(0,0), (0,0), (0,0), (0,0), (0, 0xFF)],
    0x6B00: [(0,0), (0,0),(0, 0xFF), (0, 0xFF), (0,0)],
    0x6E00: [(0, 0xFF), (0,0), (0,0), (0,0), (0,0)],
    0x9000: [(0,0), (0,0), (0, 0xFF), (0, 0xFF), (0,0)],
}

BLACKLIST = [
    {"ins": [0x14], "p1": [0x13, 0x33, 0x38, 0x94]},

]

CARD_READER_ID = 0