test = {   'name': 'q2_19',
    'points': [0.1, 0.2, 0.5, 0.5],
    'suites': [   {   'cases': [   {'code': '>>> assert trump_100_days_tweet_df.shape[0] > 50\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert trump_100_days_tweet_df.shape[0] > 200\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> assert max(trump_100_days_tweet_df['created_at']) < pd.to_datetime('2017-05-01')\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert min(trump_100_days_tweet_df['created_at']) > pd.to_datetime('2017-01-19')\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
