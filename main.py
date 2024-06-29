import requests
import json
import matplotlib.pyplot as plt
from collections import Counter
import concurrent
from concurrent.futures import ThreadPoolExecutor

def plot(answers, prompt):
    counter = Counter(answers)
    total = len(answers)

    percentages = [(item, count / total * 100) for item, count in counter.items()]
    labels = [f'{item} ({count})' for item, count in counter.items()]

    _, percentages_values = zip(*percentages)
    print(counter)

    plt.figure(figsize=(8, 6))
    plt.pie(percentages_values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Percentage of Each Choice For ' + str(len(answers)) + ' Iterations\nPrompt: ' + '.\n'.join(prompt.split('.')))
    plt.axis('equal') 
    plt.show()

def query(prompt, model='llama3'):
    url = 'http://localhost:11434/api/generate'
    payload = {
        'model': model,
        'prompt': prompt,
        'stream': False
    }
    headers = {'Content-Type': 'application/json'}

    json_payload = json.dumps(payload)
    response = requests.post(url, data=json_payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()['response'].lower().strip()
    else:
        print(f'Request failed with status code {response.status_code}')
        print(response.text)

def run_test(prompt, choices, iterations, concurrency, model='llama3'):
    answers = []
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(query, prompt, model) for _ in range(iterations)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result in choices:
                answers.append(future.result())

    return answers

def main():
    prompt = 'Please pick uniformly at random between either heads or tails. Output only the word heads or tails.'
    choices = ['heads', 'tails']
    iterations = 10
    concurrency = 34
    answers = []
    while len(answers) < iterations:
        cur_itr = iterations - len(answers)
        print('Running ' + str(cur_itr))
        answers.extend(run_test(prompt, choices, cur_itr, concurrency))

    plot(answers, prompt)

main()