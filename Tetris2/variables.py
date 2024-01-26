colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'grey': (100, 100, 100),
    'dark grey': (50, 50, 50),
    'turquoise': (64, 224, 208),
    'salmon': (250, 128, 114),
    'lime': (50, 205, 50),
    'gold': (255, 215, 0),
    'lavender': (230, 230, 250),
    'maroon': (128, 0, 0),
    'teal': (0, 128, 128),
    'orchid': (218, 112, 214),
    'sky blue': (135, 206, 235),
    'coral': (255, 127, 80),
    'mint': (152, 255, 152),
    'indigo': (75, 0, 130),
    'olive': (128, 128, 0),
    'steel blue': (70, 130, 180),
    'peach': (255, 218, 185),
    'medium violet red': (199, 21, 133),
    'aquamarine': (127, 255, 212),
    'khaki': (240, 230, 140),
    'plum': (221, 160, 221),
    'dark orange': (255, 140, 0),
    'spring green': (0, 255, 127),
    'cornflower blue': (100, 149, 237),
    'dark red': (139, 0, 0),
    'medium sea green': (60, 179, 113),
    'thistle': (216, 191, 216),
    'sandy brown': (244, 164, 96),
    'deep pink': (255, 20, 147),
    'medium spring green': (0, 250, 154),
    'dodger blue': (30, 144, 255),
    'firebrick': (178, 34, 34),
    'medium aquamarine': (102, 205, 170),
    'dark goldenrod': (184, 134, 11),
    'pale violet red': (219, 112, 147),
    'chartreuse': (127, 255, 0),
    'rosy brown': (188, 143, 143),
    'medium orchid': (186, 85, 211),
    'light sky blue': (135, 206, 250),
    'sienna': (160, 82, 45),
    'pale green': (152, 251, 152),
    'dark slate gray': (47, 79, 79),
    'peru': (205, 133, 63),
    'light coral': (240, 128, 128),
    'dark turquoise': (0, 206, 209),
    'thunderbird': (190, 0, 50),
    'light sea green': (32, 178, 170),
    'papaya whip': (255, 239, 213),
    'medium blue': (0, 0, 205),
    'chocolate': (210, 105, 30),
    'dark orchid': (153, 50, 204),
    'light goldenrod yellow': (250, 250, 210),
    'hot pink': (255, 105, 180),
    'dark green': (0, 100, 0),
    'light pink': (255, 182, 193),
    'medium purple': (147, 112, 219),
    'burlywood': (222, 184, 135),
    'deep sky blue': (0, 191, 255),
    'crimson': (220, 20, 60),
    'medium turquoise': (72, 209, 204),
    'dark salmon': (233, 150, 122),
    'medium slate blue': (123, 104, 238),
    'goldenrod': (218, 165, 32),
    'green yellow': (173, 255, 47),
    'slate blue': (106, 90, 205),
    'dark khaki': (189, 183, 107),
    'misty rose': (255, 228, 225),
    'dark violet': (148, 0, 211),
    'light steel blue': (176, 196, 222),
    'tomato': (255, 99, 71),
    'cadet blue': (95, 158, 160),
    'dark slate blue': (72, 61, 139),
    'sienna': (160, 82, 45),
    'medium slate blue': (123, 104, 238),
    'goldenrod': (218, 165, 32),
    'green yellow': (173, 255, 47),
    'slate blue': (106, 90, 205),
    'dark khaki': (189, 183, 107),
    'misty rose': (255, 228, 225),
    'dark violet': (148, 0, 211),
    'light steel blue': (176, 196, 222),
    'tomato': (255, 99, 71),
    'cadet blue': (95, 158, 160),
    'dark slate blue': (72, 61, 139),
    'chocolate': (210, 105, 30),
    'dark olive green': (85, 107, 47),
    'light salmon': (255, 160, 122),
    'medium brown': (165, 42, 42),
    'medium violet': (199, 21, 133),
    'dark cyan': (0, 139, 139),
    'light orchid': (230, 168, 215),
    'indian red': (205, 92, 92),
    'medium gray': (169, 169, 169),
    'dark magenta': (139, 0, 139),
    'pale turquoise': (175, 238, 238),
    'medium indigo': (75, 0, 130),
    'dark sienna': (60, 20, 20),
    'spring green': (0, 255, 127),
    'violet red': (208, 32, 144),
    'lime green': (50, 205, 50)
}

tetrominos = {
    'O': [
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
    ],
    'I': [
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1]
        ],
        [
            [0, 1],
            [0, 1],
            [0, 1],
            [0, 1]
        ]
    ],
    'T': [
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 0]
        ]
    ],
    'L': [
        [
            [0, 0, 0],
            [1, 1, 1],
            [1, 0, 0]
        ],
        [
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ]
    ],
    'J': [
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 1]
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]
        ],
        [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        [
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ]
    ],
    'S': [
        [
            [0, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 1]
        ]
    ],
    'Z': [
        [
            [0, 0, 0],
            [1, 1, 0],
            [0, 1, 1]
        ],
        [
            [0, 0, 1],
            [0, 1, 1],
            [0, 1, 0]
        ]
    ]
}

# tetrominos = {
#     'O': [
#         [1, 1],
#         [1, 1]
#     ],
#     'I': [
#         [1, 1, 1, 1]
#     ],
#     'T': [
#         [1, 1, 1],
#         [0, 1, 0]
#     ],
#     'L': [
#         [1, 0],
#         [1, 0],
#         [1, 1]
#     ],
#     'J': [
#         [0, 1],
#         [0, 1],
#         [1, 1]
#     ],
#     'S': [
#         [0, 1, 1],
#         [1, 1, 0]
#     ],
#     'Z': [
#         [1, 1, 0],
#         [0, 1, 1]
#     ]
# }