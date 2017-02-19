#! /usr/bin/env python
import argparse
import random

def readFile(filename):
    with open(filename,'r') as file:
        text = file.read().replace('\n',' ').strip().split(' ')

    return text

def createChain(text, nprefix):
    chain = dict()

    for idx in range(nprefix,len(text)):
        suffix = text[idx]
        # Make prefix
        prefix = ''
        for j in reversed(range(nprefix)): prefix += text[idx-(j+1)] + ' '
        prefix = prefix[:-1]    

        #Add to chain
        if prefix not in chain: chain[prefix] = [suffix]
        else: chain[prefix].append(suffix)

    return chain

def generateMessage(chain, nprefix):
    
    prefix = random.choice(chain.keys())
    message = prefix.capitalize()

    count, total = 0., 1
    count = 0. if len(chain[prefix])<2 else 1    
    #Walk the chain
    while not message.endswith('.'):
        #Get non-uniequeness count
        if len(chain[prefix])>1: count += 1
        total += 1
        
        #Get the suffix
        suffix = random.choice(chain[prefix])
        message += ' ' + suffix
        #Make the prefix for the next step        
        prefix = prefix.split(' ',1)[1] + ' '+ suffix if nprefix != 1 else suffix

    print(message)
    print("(Message had "+str(round(count/total*100,1))+"% non-unique steps)")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Output text in the style of a sample input text using a Markov Chain model')
    parser.add_argument('infile', help='The sample file')
    parser.add_argument('--prefix','-p', type=int, help='The number of words to use for the prefix. Default = 2')
    args=parser.parse_args()

    nprefix = args.prefix if args.prefix else 2

    text = readFile(args.infile)
    chain = createChain(text, nprefix)
    generateMessage(chain, nprefix)
