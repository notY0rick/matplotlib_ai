import openai
import inspect
import matplotlib.pyplot as plt

class matplotlib_ai:

    def __init__(self, openai_api_key):
        assert isinstance(openai_api_key, str), "openen_api_key needs to be provided as a string!"
        self.api_key = openai_api_key
        openai.api_key = self.api_key

    @staticmethod
    def create_prompt(message):
        if message[-1] == '.':
            message = message[:-1]
        message = message[0].lower() + message[1:]
        training_prompt = \
        f"""
        Prompt: Using matplotlib, create a box and whisker plot for x, y, and z. Assume the variables already exist. Return the code only.
        Response: import matplotlib.pyplot as plt\n\nplt.boxplot([x, y, z])\n\nplt.show()
        Prompt: Using matplotlib, plot three histograms, one for x, y, and z each. Assume variables already exist. Return the code only.
        Response: import matplotlib.pyplot as plt\n\nplt.hist(x, bins=10)\nplt.xlabel('x')\nplt.ylabel('Frequency')\nplt.title('Histogram of x')\nplt.show()\n\nplt.hist(y, bins=10)\nplt.xlabel('y')\nplt.ylabel('Frequency')\nplt.title('Histogram of y')\nplt.show()\n\nplt.hist(z, bins=10)\nplt.xlabel('z')\nplt.ylabel('Frequency')\nplt.title('Histogram of z')\nplt.show()
        Prompt: Using matplotlib, generate a scatter plot using data where data is a dictionary. Title it 'damn wtf'. Assume variables already exist. Return the code only.
        Response: import matplotlib.pyplot as plt\n\nplt.scatter('a', 'b', c='c', s='d', data=data)\n\nplt.xlabel('entry a')\n\nplt.ylabel('entry b')\n\nplt.show()
        Prompt: Using matplotlib, plot three different graphs for the data names and values. Assume variables already exist. Return the code only.
        Response: import matplotlib.pyplot as plt\n\nplt.subplot(131)\n\nplt.bar(names, values)\n\nplt.subplot(132)\n\nplt.scatter(names, values)\n\nplt.subplot(133)\n\nplt.plot(names, values)\n\nplt.suptitle('Categorical Plotting')\n\nplt.show()
        Prompt: Using matplotlib, {message}. Assume variables already exist. Return the code only.
        Response: 
        """

        return training_prompt

    @staticmethod
    def call_gpt(message):
        prompt = matplotlib_ai.create_prompt(message)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": prompt}])
        response = response['choices'][0]['message']['content']
        return response
    
    def __call__(self, prompt, print_code=False):
        frame = inspect.currentframe().f_back
        prompt = matplotlib_ai.create_prompt(prompt)
        code = matplotlib_ai.call_gpt(prompt)
        if print_code:
            print(code)
        exec(code, frame.f_globals, frame.f_locals)
        return code