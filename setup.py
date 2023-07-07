from setuptools import setup, find_packages

LONG_DESC = """
Do you also have a love-hate relationship with matplotlib? So do I! 
That's why I created this mini-project that can help you graph your data using natural language. 
The package dependencies require openai and matplotlib, and it is unbelievably easy to use. 
Calling OpenAI's GPT API, prompt engineering, and using few-shot learning, matplotlib_ai is capable 
of generating graphs without requiring you to write a single line of matplotlib code! Check out this GitHub link:
https://github.com/notY0rick/matplotlib_ai
"""

setup(name='matplotlib_ai',
      version='1.0.1',
      description='A GPT-powered tool to bring no-code data visualization to life!',
      long_description=LONG_DESC,
      author='Yorick Chern',
      author_email='yorichek.007@gmail.com',
      url='https://github.com/notY0rick/mpl_ai',
      packages=find_packages(),
      keywords=['python', 'gpt', 'matplotlib', 'no code', 'LLM'],
      license='MIT'
      )