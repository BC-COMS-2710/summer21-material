test = {   'name': 'q2_1',
    'points': [0.75, 0.75],
    'suites': [   {   'cases': [   {   'code': ">>> # This tests that there are no Nan's in the Translated_Review column;\n"
                                               ">>> assert reviews_df['Translated_Review'].isna().value_counts().shape[0] == 1\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # This tests that there are no Nan's in the Translated_Review column;\n>>> assert reviews_df['Sentiment'].isna().value_counts().shape[0] == 1\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
