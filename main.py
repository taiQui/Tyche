from parser import Parser
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--request',help="Burp request",required=True)
    parser.add_argument('-p','--parameter',help="Parameter where Tyche will inject payloads",required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse()
    request = Parser(args.request).parse()
    
