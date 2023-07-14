import openai
import inspect


class matplotlib_ai:

    def __init__(self, api_key, engine='gpt', model_name='gpt-3.5-turbo'):
        """
        Initializer for matplotlib_ai.

        :param api_key: the api key needed to access the models - str
        :param engine: the type of engine to be used - str
        :param model_name: the specified model to be used - str or None
        """

        assert isinstance(api_key, str), "api_key needs to be provided as a string!"
        assert engine in ['gpt'], f"engine needs to be one of ['gpt']"

        self.api_key = api_key

        if engine == 'gpt':
            self.engine = 'gpt'
            if model_name is not None:
                self.model_name = model_name
            else:
                self.model_name = 'gpt-3.5-turbo'
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

    def call_gpt(self, message):
        prompt = matplotlib_ai.create_prompt(message)
        response = openai.ChatCompletion.create(model=self.model_name, messages=[{"role": "system", "content": prompt}])
        response = response['choices'][0]['message']['content']
        return response

    def __call__(self, prompt, print_code=False, auto_rerun=True, n_candidates=1):
        """
        Main function that takes a user prompt to produce the desired graph.
        :param prompt: the input prompt describing the graph(s) the user wants - str
        :param print_code: whether to print out the AI-generated code - bool
        :param auto_rerun: automatically reruns the AI if the generated code fails - bool
        :param n_candidates: how many candidate graphs it should generate - int
        :return: codes: a list of AI-generated code - list
        """
        assert isinstance(prompt, str), "prompt needs to be a string"
        assert isinstance(print_code, bool), "print_code needs to be a string"
        assert isinstance(auto_rerun, bool), "auto_rerun needs to be a boolean"
        assert isinstance(n_candidates, int), "n_candidates need to be an integer"
        assert n_candidates >= 1, "n_candidates need to be >= 1"

        count = 0
        codes = []
        if self.engine == 'gpt':
            frame = inspect.currentframe().f_back
            prompt = matplotlib_ai.create_prompt(prompt)
            keep_trying = auto_rerun
            while keep_trying:
                try:
                    code = self.call_gpt(prompt)
                    if print_code:
                        print(code)
                    exec(code, frame.f_globals, frame.f_locals)
                    count += 1
                    codes.append(code)
                    if count == n_candidates:
                        keep_trying = False
                except:
                    pass

            return codes
