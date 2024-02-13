import os
import argparse
from assistant.assistant import summarize

def main():
    parser = argparse.ArgumentParser(description='Digital Agentso')
    parser.add_argument('--agent', type=str, help='Name of the agent')
    parser.add_argument('--input', type=str, help='Input promot')
    parser.add_argument('--openaikey', default=os.environ.get('OPENAI_API_KEY'), help='OPEN AI KEY')
    parser.add_argument('--temperature', default=0, help='Temperature')
    args = parser.parse_args()
    agent = args.agent
    input = args.input
    openaikey = args.openaikey
    temperature = args.temperature
    if agent == 'assistant':       
        result = summarize('prompts/summarize_newsletter/system.md', input, openaikey, temperature)
        print(result)

if __name__ =='__main__':
    main()