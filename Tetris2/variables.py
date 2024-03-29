colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'grey': (100, 100, 100),
    'dark grey': (50, 50, 50),
    'electric crimson': (255, 0, 63),
    'vivid tangerine': (255, 160, 137),
    'laser orange': (255, 165, 0),
    'luminous vivid amber': (255, 191, 0),
    'ultraviolet': (102, 0, 255),
    'razzle dazzle rose': (255, 51, 204),
    'brilliant shocking pink': (255, 33, 135),
    'cyan azure': (0, 255, 255),
    'bright indigo': (90, 0, 255),
    'lime green': (50, 205, 50)
}

tetrominos = {
    'O': [
        [
            [0, 0],
            [1, 1],
            [1, 1]
        ]
    ],
    'I': [
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1]
        ],
        [
            [0, 0],
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