import uuid
from datetime import datetime
from models.blog_post import BlogPost
from models.user import User

ENCODED_HEADER = 'data:image/jpeg;charset=utf-8;base64, '

in_memory_photos = {}
in_memory_photos['default'] = "R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="
in_memory_photos['local1'] = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC\
0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
in_memory_photos['local2'] = "R0lGODdhAQABAPAAAP8AAAAAACwAAAAAAQABAAACAkQBADs="
in_memory_photos['local3'] = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAD\
UlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

in_memory_posts = [BlogPost("FirstTitle", uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')\
                             , "Lorem Ipsum is simply dummy ,\
                             'text of the printing and typesetting industry. Lorem Ipsum \
                             has been the industry's , standard dummy text ever since the \
                             1500s,when an unknown printer took a galley of , type and scrambled \
                             it to make a type specimen book. It has survived not only five \
                             centuries, but also the leap into electronic typesetting, \
                             remaining essentially unchanged. It was popularised, in the,\
                             1960s with the release of Letraset sheets containing Lorem Ipsum \
                             passages,and more recently with desktop , publishing software like \
                             Aldus PageMaker including versions of Lorem Ipsum.\
                             Specific content first post",
                            ENCODED_HEADER +
                            in_memory_photos['local2']),

                   BlogPost("SecondTitle", uuid.UUID('25447284-aa74-4fb6-b7a0-2bb955f2b2b1')\
                             , "Lorem Ipsum is simply \
                             dummy text of the, printing and typesetting industry. \
                             Lorem Ipsum has been the industry's standard dummy text \
                             ever since, the 1500s, when an unknown printer took a galley\
                             of type and scrambled it to make a type specimen book. \
                             It has survived not only five centuries, but also the leap\
                             into electronic typesetting, remaining essentially unchanged.\
                             It was popularised in the 1960s with the release of Letraset sheets , \
                             containing Lorem Ipsum passages, and more recently with desktop \
                             publishing software like Aldus PageMaker , including versions \
                             of Lorem Ipsum.",
                            ENCODED_HEADER +
                            in_memory_photos['local1']),

                   BlogPost("ThirdTitle", uuid.UUID('99ae0e65-372b-4f4a-be88-776d6a4d92bd')\
                             , "Lorem Ipsum is simply \
                             dummy text of the printing ,and typesetting industry.\
                             Lorem Ipsum has been the industry's standard dummy text\
                             ever since the 1500s,when an unknown printer took a galley\
                             of type and scrambled it to make a type specimen book. It has \
                             survived ,not only five centuries, but also the leap into \
                             electronic typesetting, remaining essentially unchanged. It was \
                             popularised in the 1960s with the release of Letraset sheets \
                             containing Lorem Ipsum passages, and more recently , with desktop \
                             publishing software like Aldus PageMaker including \
                             versions of Lorem Ipsum.",
                            ENCODED_HEADER +
                            in_memory_photos['local3']),

                   BlogPost("FourthTitle", uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')\
                            , "There are many variations of passages of Lorem Ipsum available,\
                            but the majority have suffered alteration in some form, by injected\
                            humour, or randomised words which don't look even slightly believable. \
                            If you are going to use a passage of Lorem Ipsum, you need to\
                            be sure there isn't anything embarrassing hidden in the middle\
                            of text. All the Lorem Ipsum generators on the Internet tend to\
                            repeat predefined chunks as necessary, making this the first \
                            true generator on the Internet. It uses a dictionary of over 200\
                            Latin words, combined with a handful of model sentence structures,\
                            to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                            Ipsum is therefore always free from repetition, injected humour, \
                            or non-characteristic words etc.", None),

                   BlogPost("FifthTitle", uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("SixthTitle", uuid.UUID('25447284-aa74-4fb6-b7a0-2bb955f2b2b1')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("SeventhTitle", uuid.UUID('99ae0e65-372b-4f4a-be88-776d6a4d92bd')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("EightTitle", uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("NinthTitle", uuid.UUID('25447284-aa74-4fb6-b7a0-2bb955f2b2b1')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("TenthTitle", uuid.UUID('99ae0e65-372b-4f4a-be88-776d6a4d92bd')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None),

                   BlogPost("EleventhTitle", uuid.UUID('99ae0e65-372b-4f4a-be88-776d6a4d92bd')\
                              , "There are many variations of passages of Lorem Ipsum available,\
                              but the majority have suffered alteration in some form, by injected\
                              humour, or randomised words which don't look even slightly believable. \
                              If you are going to use a passage of Lorem Ipsum, you need to\
                              be sure there isn't anything embarrassing hidden in the middle\
                              of text. All the Lorem Ipsum generators on the Internet tend to\
                              repeat predefined chunks as necessary, making this the first \
                              true generator on the Internet. It uses a dictionary of over 200\
                              Latin words, combined with a handful of model sentence structures,\
                              to generate Lorem Ipsum which looks reasonable. The generated Lorem \
                              Ipsum is therefore always free from repetition, injected humour, \
                              or non-characteristic words etc.", None)]

in_memory_posts[0].post_id = uuid.UUID('f9c3a576-28bc-4b63-931d-04d6488d2f0d')
in_memory_posts[0].stamp.creation_time = (datetime.strptime('1997-February-03, \
                                                            19:40:33', "%Y-%B-%d, \
                                                            %H:%M:%S"))

in_memory_posts[1].post_id = uuid.UUID('daca57d1-c180-4e0a-8394-f5c95a5d5f23')
in_memory_posts[1].stamp.creation_time = datetime.strptime('1997-March-02, 12:30:44',\
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[2].post_id = uuid.UUID('a656f973-5b82-462d-aff7-8d2c6c3e4fa2')
in_memory_posts[2].stamp.creation_time = datetime.strptime('1997-April-05, 21:40:32', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[3].post_id = uuid.UUID('fcd27650-ddee-479b-b029-af68c6f0ef90')
in_memory_posts[3].stamp.creation_time = datetime.strptime('2000-April-02, 20:12:22',\
                                                           "%Y-%B-%d,\
                                                           %H:%M:%S")

in_memory_posts[4].post_id = uuid.UUID('0d816f70-0ed1-4cee-b156-112462e6ea52')
in_memory_posts[4].stamp.creation_time = datetime.strptime('2000-April-02, 20:20:40', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[5].post_id = uuid.UUID('c98026b6-08b2-45c9-981b-a6159124189d')
in_memory_posts[5].stamp.creation_time = datetime.strptime('2000-June-01, 18:11:12', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[6].post_id = uuid.UUID('2bb62474-43fb-4643-b38e-a333f3999254')
in_memory_posts[6].stamp.creation_time = datetime.strptime('2000-July-02, 19:10:11', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[7].post_id = uuid.UUID('3cb862a3-3bf7-44a2-83d8-7b7440588b68')
in_memory_posts[7].stamp.creation_time = datetime.strptime('2010-April-05, 10:11:12', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[8].post_id = uuid.UUID('f4968b20-92fc-4ef6-a9f7-e84bafec6b9e')
in_memory_posts[8].stamp.creation_time = datetime.strptime('2010-April-05, 20:12:11', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[9].post_id = uuid.UUID('1e260899-2bfb-4fc3-8175-17ecaf7c68e3')
in_memory_posts[9].stamp.creation_time = datetime.strptime('2010-May-03, 09:01:11', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_posts[10].post_id = uuid.UUID('be3e1383-d296-4956-85d2-d0da74c78531')
in_memory_posts[10].stamp.creation_time = datetime.strptime('2010-May-05, 11:13:00', \
                                                            "%Y-%B-%d, \
                                                            %H:%M:%S")

in_memory_users = [
    User('admin', 'admin@admin.com', 'adminpass'),
    User('FirstAuthor', 'f_author@blog.com', 'fpass'),
    User('SecondAuthor', 's_author@blog.com', 'spass'),
    User('ThirdAuthor', 't_author@blog.com', 'tpass')]

in_memory_users[0].user_id = uuid.UUID('afa28c0c-4e89-468f-8709-a7583c666cb4')
in_memory_users[0].user_timestamp.creation_time = '2017-03-21 21:20:33'
in_memory_users[1].user_id = uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')
in_memory_users[1].user_timestamp.creation_time = '2015-03-12 12:02:31'
in_memory_users[2].user_id = uuid.UUID('25447284-aa74-4fb6-b7a0-2bb955f2b2b1')
in_memory_users[2].user_timestamp.creation_time = '2009-06-15 13:21:35'
in_memory_users[3].user_id = uuid.UUID('99ae0e65-372b-4f4a-be88-776d6a4d92bd')
in_memory_users[3].user_timestamp.creation_time = '2009-06-15 13:21:35'
