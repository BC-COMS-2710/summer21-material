test = {   'name': 'q2.7',
    'points': [1, 1, 1, 1, 1],
    'suites': [   {   'cases': [   {   'code': ">>> assert set(['Department Name', 'Department Id', 'Course Name', 'Course Listing', 'Course Id', 'Course Link']) ==  set(course_df.keys())\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert course_df.shape[0] > 1000\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert course_df.shape[0] > 1500\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert course_df.shape[0] > 2000\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert course_df.shape[0] > 2250\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
