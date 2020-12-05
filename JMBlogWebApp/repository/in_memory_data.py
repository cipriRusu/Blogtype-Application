import uuid
from models.blog_post import BlogPost
from models.user import User

in_memory_posts = [BlogPost("FirstTitle", uuid.UUID('6ee39856-2721-46c4-bda7-3faf8e4a60f5')\
                             ,"Lorem Ipsum is simply dummy ,\
                             'text of the printing and typesetting industry. Lorem Ipsum \
                             has been the industry's , standard dummy text ever since the \
                             1500s,when an unknown printer took a galley of , type and scrambled \
                             it to make a type specimen book. It has survived not only five \
                             centuries, but also the leap into electronic typesetting, \
                             remaining essentially unchanged. It was popularised, in the,\
                             1960s with the release of Letraset sheets containing Lorem Ipsum \
                             passages,and more recently with desktop , publishing software like \
                             Aldus PageMaker including versions of Lorem Ipsum.\
                             Specific content first post"),

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
                             of Lorem Ipsum."),

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
                             versions of Lorem Ipsum.")]

in_memory_posts[0].post_id = uuid.UUID('f9c3a576-28bc-4b63-931d-04d6488d2f0d')
in_memory_posts[0].stamp.creation_time = '2019-09-03 19:40:33'
in_memory_posts[1].post_id = uuid.UUID('daca57d1-c180-4e0a-8394-f5c95a5d5f23')
in_memory_posts[1].stamp.creation_time = '1991-03-02 12:30:44'
in_memory_posts[2].post_id = uuid.UUID('a656f973-5b82-462d-aff7-8d2c6c3e4fa2')
in_memory_posts[2].stamp.creation_time = '2017-04-05 21:40:32'

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
