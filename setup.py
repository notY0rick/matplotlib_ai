from setuptools import setup, find_packages

with open('README.md') as f:
    LONG_DESC = f.read()
setup(name='matplotlib_ai',
      version='1.0',
      description='A GPT-powered tool to bring no-code data visualization to life!',
      long_description=LONG_DESC,
      author='Yorick Chern',
      author_email='yorichek.007@gmail.com',
      url='https://github.com/notY0rick/mpl_ai',
      packages=find_packages(),
      keywords=['python', 'gpt', 'matplotlib', 'no code', 'LLM'],
      license='MIT'
      )