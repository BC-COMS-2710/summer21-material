test = {   'name': 'q3.1',
    'points': [1, 1, 1],
    'suites': [   {   'cases': [   {'code': '>>> assert "clean_text_one" in obits_df;\n>>> assert "clean_text_two" in obits_df\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> assert np.all(obits_df['clean_text_one'].map(lambda x: type(x)) == str);\n"
                                               ">>> assert np.all(obits_df['clean_text_two'].map(lambda x: type(x)) == str)\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert np.all(obits_df['clean_text_two'].map(lambda x: x.islower()));\n>>> assert np.all(obits_df['clean_text_one'].map(lambda x: x.islower()))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
