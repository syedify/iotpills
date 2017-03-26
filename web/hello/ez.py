import json

def printitems(dictObj, indent=0):
    p=[]
    p.append('<ul>\n')
    for k,v in dictObj.iteritems():
        if isinstance(v, dict):
            p.append('<li>'+ str(k)+ ':')
            p.append(printitems(v))
            p.append('</li>')
        else:
            p.append('<li>'+ str(k)+ ':'+ str(v)+ '</li>')
    p.append('</ul>\n')
    return '\n'.join(p)

def main():
    json_data = json.load(open("dummy.json"))
    # df = pandas.DataFrame(data).T
    # df.fillna("-", inplace=True)
    s = printitems(json_data,"")
    # json_str = json.dumps(json_data)
    #close("static/dummy.json")
    print type(s)
    #print s

main()