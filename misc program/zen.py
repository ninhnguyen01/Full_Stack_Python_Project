import this

print(this)

# Output text

python_zen = """ 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

print("Length count: " + str(len(python_zen)))
print("Count of 'better': " + str(python_zen.count("better")))

percentage_of_word = python_zen.count("better") / len(python_zen)
percentage = round(percentage_of_word, 2)
print("Percentage of 'better': " + str(percentage)+ '%')