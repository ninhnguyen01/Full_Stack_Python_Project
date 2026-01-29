"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-10239.c289.us-west-1-2.ec2.cloud.redislabs.com',
    port=10239,
    decode_responses=True,
    username="default",
    password="MuXFoi4qdxKHj1CwVQHhK46sW8uNyLtx",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

string_var = r.set('secret', 'ni!')
string_result = r.get('secret')

string_var2 = r.set('carats', 24)
string_result2 = r.get('carats')

string_var3 = r.set('fever', '101.5')
string_result3 = r.get('fever')

print(string_result, string_result2, string_result3)

new_string_var = r.getset('secret', 'niGHT')
new_string_var_result = r.get('secret')
print(new_string_var_result) 

multi_key = r.mset({'pie': 'cherry', 'cordial': 'sherry'})
multi_val = r.mget(['pie', 'cordial'])
print(multi_val)

r.lpush('zoo', 'alligator', 'duck')

r.hmset('song', {'do': 'a deer', 're': 'about a deer'})
r.hset('song', 'mi', 'a note to follow re')
get_1_val = r.hget('song', 'mi')
print(get_1_val)
get_multi_val = r.hmget('song', 're', 'do')
print(get_multi_val)
