test = {   'name': 'q3_2',
    'points': [1, 1],
    'suites': [   {   'cases': [   {   'code': ">>> # Make sure you are adding to each candidate's vocabulary;\n>>> for key,val in speakers.items():\n...     assert len(val) != 0\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure you are storing the counts as integers;\n'
                                               '>>> for key,val in speakers.items():\n'
                                               '...     assert type(list(val.values())[0]) == int;\n'
                                               '>>> # [(key, len(val)) for key, val in speakers.items()]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
