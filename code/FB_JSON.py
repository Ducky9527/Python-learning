import json

#Basic handling

#Load data raw string

data = r'"\u00e9\u0080\u0099\u00e5\u0080\u008b\u00e7\u00b5\u0090\u00e6\u009e\u009c\u00e9\u0082\u0084\u00e6\u00bb\u00bf\u00e4\u00b8\u008d\u00e9\u008c\u00af\u00e7\u009a\u0084www\n\u00e7\u0095\u00a2\u00e7\u00ab\u009f\u00e6\u0088\u0091\u00e5\u00be\u0088\u00e5\u0096\u009c\u00e6\u00ad\u00a1\u00e5\u00b7\u00b4\u00e5\u0093\u0088\u00e4\u00bb\u00a5\u00e5\u008f\u008a\u00e5\u00b7\u00b4\u00e5\u0093\u0088\u00e7\u009a\u0084\u00e7\u0084\u00a1\u00e4\u00bc\u00b4\u00e5\u00a5\u008fwww\n\n\u00e4\u00b8\u008d\u00e9\u0081\u008e\u00e6\u00b7\u0091\u00e5\u00a5\u00b3\u00e5\u0098\u009b...(\u00e6\u00b1\u0097"'

#note that, because facebook's json file is badly encoded, to decode any json file containing unicode, one must first encode the text
#as latin1 and then decode it as utf8
decode_data = json.loads(data).encode('latin1').decode('utf8')
print(decode_data)


########


#Advanced handling by Meow Meow


def parse_obj(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj

with open("FB_JSON.json") as f:
    d = json.load(f, object_hook=parse_obj)

print(d)
