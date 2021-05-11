test = {   'name': 'q2_7',
    'points': [0.25, 0.25, 0.25],
    'suites': [   {   'cases': [   {'code': '>>> for tok in spacy_tokens:\n...     assert type(tok) != int\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> assert spacy_tokens[0].lower() == 'when'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert spacy_tokens[-1] == '.'\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
