"""
        Burp Requests Parser
"""

from os.path import isfile

class Parser:
    def __init__(self,file):
        if not isfile(file):
            raise Exception("File not found ! => {}".format(file))
        self.request = open(file,'r').read()
        self.header = self.request.split('\r\n\r\n')[0].split('\r\n')[1:]
        if len(self.request.split('\r\n\r\n')) > 1:
            self.data = self.request.split('\r\n\r\n')[1].split('\r\n')[0]
        else:
            self.data = None
        self.parse()
    def parse(self):
        dic = {}
        dic['method'] = self.request.split('\r\n')[0].split(' ')[0]
        dic['url']    = self.request.split('\r\n')[0].split(' ')[1]
        dic['http_version'] = self.request.split('\r\n')[0].split(' ')[2]
        head = {}
        for header in self.header:
            head[header.split(': ')[0]] = ''.join(header.split(': ')[1:])
        dic['header'] = head
        if self.data != None:
            d = {}
            for data in self.data.split('&'):
                d[data.split('=')[0]] = ''.join(data.split('=')[1:])
            dic['data'] = d
        else:
            dic['data'] = None
        return dic

if __name__ == "__main__":
    a = Parser("/home/taiqui/Documents/WORKDIR/doctor/req2").parse()
    print(a)
