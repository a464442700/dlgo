import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}


#json_str = json.dumps(data1)
#json_str="{\"name\":\"啊\"}"
json_str="X"
for i in range(1,1024*1024*4):
    json_str=json_str+"X"

print(len(json_str))
json_str="{\"name\":\""+json_str+"\"}"
json_obj=json.loads(json_str)
print(len(json_obj["name"]))
