test = {   'name': 'q1_14',
    'points': [0.1, 0.4, 0.5, 0.5],
    'suites': [   {   'cases': [   {'code': '>>> assert len(sorted_pairs) == 30\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> for example in sorted_pairs:\n'
                                               '...     assert type(example) == tuple\n'
                                               '...     assert type(example[0]) == tuple\n'
                                               '...     assert type(example[1]) == float or type(example[1]) == int\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> assert (('furnace', ' stove'), 0) == sorted_pairs[-1]\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert (('car', 'automobile'), 1.0) in sorted_pairs[:3]\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
