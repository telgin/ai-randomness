# ai-randomness

If we ask an LLM to pick uniformly at random between X options, how well can it do? A pseudorandom number genrator performs with perfectly even distributions however it is not "true" randomness. When you ask a human to do this, they will favor some numbers more than others subconsciously. What does an LLM do?

## Why might it work
An LLM assigns probabilities to each next word in the completion. If we tell it to pick uniformly at random, it may have the capacity internally to actually do this. Would this be closer to true randomness vs. a pseudorandom number generator? Especially if it had no context of the previous answers it gave?

## Why it might not work
An LLM might be similar to a human in this case where it has implicit bias towards some numbers more than others even though it thinks it's random. Like humans, it may switch between the options more often than you'd see in an actual random distribution.

## Methodology
Let's run a prompt 1000 times against Llama 3 and record the outputs. The LLM will not know the previous answers it gave. We will define the allowed outputs in the prompt and enforce this by retrying whenever an output given is not allowed. We'll keep retrying until all outputs are in the allowed set.

## Experiments
### Experiment 1
#### Prompt: `'Please pick uniformly at random between either 0 or 1. Output only the number 0 or 1.'`
![Experiment 1](/Experiment_1.png)
* chi-squared: 446.224 (the magnitude of deviation)
* p-value: 4.785036781297168e-99 (probability of observing this result by pure chance)
* interpretation: There is essentially no chance the difference between this result and the expected 500/500 split can be explained by pure chance. The results are therefore not random.
### Experiment 2
#### Prompt: `'Please pick uniformly at random between either 0 or 1. Output only the word 0 or 1.'`
![Experiment 2](/Experiment_2.png)
* chi-squared: 163.216
* p-value: 2.2440541677381526e-37
* interpretation: There is essentially no chance the difference between this result and the expected 500/500 split can be explained by pure chance. The results are therefore not random.
### Experiment 3
#### Prompt: `'Please pick uniformly at random between either heads or tails. Output only the word heads or tails.'`
![Experiment 3](/Experiment_3.png)
* chi-squared: 876.096
* p-value: 1.5429103595031624e-192
* interpretation: There is essentially no chance the difference between this result and the expected 500/500 split can be explained by pure chance. The results are therefore not random.
### Experiment 4
#### Prompt: `'Please pick uniformly at random between either 1 or 0. Output only the number 1 or 0.'`
_The model was unable to answer this correctly even once after 1000 tries._
### Experiment 5
#### Prompt: `'Please pick uniformly at random between either 1 or 0. Output only the word 1 or 0.'`
![Experiment 5](/Experiment_5.png)
* chi-squared: 47.524
* p-value: 5.433464235346428e-12
* interpretation: Although better than before... there is essentially no chance the difference between this result and the expected 500/500 split can be explained by pure chance. The results are therefore not random.
### Experiment 6
#### Prompt: `'Please pick uniformly at random between either 1, 2, 3, or 4. Output only the number 1, 2, 3, or 4.'`
![Experiment 6](/Experiment_6.png)
* chi-squared: 1600.608
* p-value: 0.0
* interpretation: There is no chance the difference between this result and the expected 250/250/250/250 split can be explained by pure chance. The results are therefore not random.
### Experiment 7
#### Prompt: `'Please pick uniformly at random between either 1, 2, 3, or 4. Output only the number 1, 2, 3, or 4'` (no ending period)
_The model had a 3.3% correct completion rate so I wasn't willing to wait for it to get through 1000 samples correctly._
### Experiment 8
#### Prompt: `'Please pick uniformly at random between either 1, 2, 3, or 4. Output only the word 1, 2, 3, or 4.'`
![Experiment 8](/Experiment_8.png)
* chi-squared: 1137.288
* p-value: 2.96009254124436e-246
* interpretation: There is essentially no chance the difference between this result and the expected 250/250/250/250 split can be explained by pure chance. The results are therefore not random.
### Experiment 9
#### Prompt: `'Please pick uniformly at random between either 1, 2, 3, or 4. Output only the word 1, 2, 3, or 4'` (no ending period)
![Experiment 8](/Experiment_9.png)
* chi-squared: 1373.248
* p-value: 1.8798193491345713e-297
* interpretation: There is essentially no chance the difference between this result and the expected 250/250/250/250 split can be explained by pure chance. The results are therefore not random.
### Experiment 10
#### Prompt: `'Please pick uniformly at random between 1-10 inclusive. Output only your choice 1-10.'`
![Experiment 10](/Experiment_10.png)
* chi-squared: 7680.82
* p-value: 0.0
* interpretation: There is no chance the difference between this result and the expected 10% split can be explained by pure chance. The results are therefore not random.
### Experiment 11
#### Prompt: `'Please pick uniformly at random between 1-10 inclusive. Output ONLY your choice 1-10. Dont just pick 7 everytime. Give every number an even shot.'`
![Experiment 10](/Experiment_11.png)
* chi-squared: 2547.2
* p-value: 0.0
* interpretation: There is no chance the difference between this result and the expected 10% split can be explained by pure chance. The results are therefore not random.


## Conclusion
The LLMs are very sensitive to the specific phrasing of the question including differences that should have no effect. A small change to the phrasing will give vastly different distributions. Based on these experiments it seems they do not come even close to pseudorandom number generator level. We could say they're worse than a human also but technically for this to be a fair fight we'd have to ask someone with short term memory loss where they never remember their previous answers. Would you or I answer the same thing every time if we had no memory?

## Resources
* [Ollama](https://github.com/ollama/ollama)
* [Llama 3](https://llama.meta.com/llama3/)
* [ChatGPT to speedup coding](https://chatgpt.com/)