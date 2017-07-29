import json
import requests
import sys

def slack_push(slack_data_text):
    webhook_url = 'https://hooks.slack.com/services/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'
    slack_data = {'text': slack_data_text}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
    	raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
    	    )

def main():
    slack_push("hello tej asshole")

if __name__ == '__main__':
    sys.exit(main())
