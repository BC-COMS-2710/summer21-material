test = {   'name': 'q2.3',
    'points': [0.1, 0.1, 0.4],
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like you might have forgotten to add a return statement to get_total_word_count();\n'
                                               '>>> assert get_total_word_count(["hello"]) != None\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Make sure the function is returning a int;\n>>> assert "int" in str(type(get_total_word_count(["hello"])))\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure to get the total number of words used, not the size of the vocabulary;\n>>> assert get_total_word_count(["hello hello"]) == 2\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
