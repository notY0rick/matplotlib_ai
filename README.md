# matplotlib_ai
Do you also have a love-hate relationship with [matplotlib](https://matplotlib.org/)? So do I! That's why I created this mini-project that can help you graph your data using natural language. The package dependencies require `openai` and `matplotlib`, and it is unbelievably easy to use. Calling OpenAI's GPT API, prompt engineering, and using few-shot learning, `matplotlib_ai` is capable of generating graphs without requiring you to write a single line of `matplotlib` code!

Say we have a dictionary `data` with 4 curves labeled `'a'`, `'b'`, `'c'`, and `'d'`:
```python
import numpy as np
data = {'a': np.arange(50),
		'c': np.random.randint(0, 50, 50),
		'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
If we wanted to graph each curve and make curve `'a'` dashed and call this graph "my ekg when i see you :)", the most sensible thing would be to write `matplotlib` code as such:
```python
import matplotlib.pyplot as plt
plt.plot(data['a'], linestyle='dashed', label='a')
plt.plot(data['b'], label='b')
plt.plot(data['c'], label='c')
plt.plot(data['d'], label='d')
plt.title('my ekg when i see you :)')
plt.legend()
plt.show()
```
However, with `matplotlib_ai` it is as easy as:
```python
from matplotlib_ai.matplotlib_ai import matplotlib_ai
mpl_ai = matplotlib_ai("YOUR-OPENAI-API-KEY")
prompt = "graph a curve for each item in data and title the graph 'my ekg when i see you :)'. " + 
		 "Make curve 'a' in data a dashed line.""
code = mpl_ai(prompt)
```
Then, `mpl_ai` would generate:


![yuhhhh](https://scontent.xx.fbcdn.net/v/t1.15752-9/358351553_1042559263392780_1124760776888830793_n.png?stp=dst-png_p403x403&_nc_cat=108&cb=99be929b-3346023f&ccb=1-7&_nc_sid=aee45a&_nc_ohc=w_K4__DK_HMAX89R78B&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdS4drpaM2oqdda3Xpu_gWoU3Lv0wmRGzSGGPBBaF9hE9g&oe=64CF178D)



To see the code generated by GPT, simply print it like so:
```
>>> print(code)		# the code generated by GPT
import matplotlib.pyplot as plt
for key, value in data.items():
  if key == 'a':
    plt.plot(value, linestyle='dashed', label=key)
  else:
    plt.plot(value, label=key)
plt.title('my ekg when i see you :)')
plt.legend()
plt.show()
```
