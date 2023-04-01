import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey|hey buddy|Ok Bakbak",
        ["Hello", "Hi there"]
    ],
    [
        r"what is your name?",
        ["My name is Bakbak", "You can call me Bakbak"]
    ],
    [
        r"how are you?",
        ["Just chilling","Busy at working","Always there for you"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye", "See you"]
    ],
    [
        r"what is the time?",
        ["It is currently [current_time]"]
    ],
    [
        r"what is the weather like today?",
        ["The weather today is [current_weather]"]
    ],
    [
        r"what can you do?",
        ["Help you solve your bugs and doubts"]
    ],
    [
        r"what do you like?",
        ["I like helping and exploring"]
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color since I'm a computer program"]
    ],
    [
        r"what is your favorite food?",
        ["I like electricity"]
    ],
    [
        r"what is your favorite movie?",
        ["I don't watch movies since I'm a computer program"]
    ],
    [
        r"what is your favorite book?",
        ["I don't read books since I'm a computer program"]
    ],
    [
        r"how old are you?",
        ["My developer is still working on me"]
    ],
    [
        r"what is the meaning of life?",
        ["Solving your question"]
    ],
    [
        r"how do you work?",
        ["I use natural language processing to understand your messages and generate responses"]
    ],
    [
        r"what is your purpose?",
        ["Solving your bugs and becoming the most used chatbot"]
    ],
    [
        r"tell me a joke",
        ["Why do we tell actors to “break a leg?” Because every play has a cast."]
    ],
    [
        r"what is your favorite hobby?",
        ["I like to work all the time"]
    ],
    [
        r"what is your favorite song?",
        ["I don't listen to music since I'm a computer program"]
    ],
    [
        r"what is your favorite animal?",
        ["I don't have a favorite animal since I'm a computer program"]
    ],
    [
        r"where are you from?",
        ["I am created by a developer"]
    ],
    [
        r"what is your favorite sport?",
        ["I don't have a favorite sport since I'm a computer program"]
    ],
    [
        r"what is your favorite game?",
        ["I don't play games since I'm a computer program"]
    ],
    [
        r"what is your favorite TV show?",
        ["I don't watch TV shows since I'm a computer program"]
    ],
    [
        r"what is your favorite book genre?",
        ["I don't have a favorite book genre since I'm a computer program"]
    ],
    [
        r"what is your favorite movie genre?",
        ["I don't have a favorite movie genre since I'm a computer program"]
    ],
    [
        r"what is your favorite website?",
        ["My favourite website is https://github.com/ShrutiGhodake"]
	],   
    [
        r"what is python\??",
        ["Python is a popular high-level programming language", "Python is a programming language that is used for web development, machine learning, data analysis, and more"]
    ],
    [
        r"what is Java\??",
        ["Java is a programming language and computing platform first released by Sun Microsystems in 1995."]
    ],
    [
        r"what id data science\??",
        ["Data science combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI), and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organization’s data."]
    ],
    [
        r"what is ai\??",
        ["At its simplest form, artificial intelligence is a field, which combines computer science and robust datasets, to enable problem-solving"]
    ],
    [
        r"What motivates you\??",
        ["My developer is working hard for me."]
    ],

]

chatbot = Chat(pairs, reflections)
chatbot.converse()