# Personal-stuff

  
troy is the basic setup of a blogging site. It has been structured using HTML/CSS.  It also uses Bootsrap for front-end styling.


**RIVETING INTRODUCTION TO FLAKE8**

  

Recently, I was learning about tools that make me a better python developer. Having previously had the mindset that having a strong enough skill-set would reduce your chances of having linting issues within your code, I was in shock to realize that other factors were in play too. At the time, I had just heard about linting..never really got around to finding out how to actually do it, or the tools available that could help you do it.

  

So, in my discovery, I stumbled upon Flake8. This is a good python code linter that you can use. It encompasses other coding standards like Pep8 and Pylint. To install it, just run the command:

```
python -m pip install flake8

```

**COOL FEATURES FROM FLAKE8**

You could choose to either check a single file by narrowing down to that specific file. This could be done by running:

```
flake8 path/to/your/code/example_main.py

```

As well, you could run flake8 to reveal the problems within the entire project by narrowing down to the project folder. 

```
flake8 path/to/your_project

```

I was mind blown when I learned that you could also exclude other files that you did not necessarily need to be tested against. This could be as a result of the syntax used within these files. Files such as configuration files and migration files do not necessarily need to conform to the Flake8 standards, thus the reason to exclude them from the rest of the files that you would run Flake8 against. The flake8 documentation too could guide you configure this linting tool to do just what you need it to do. Really cool right?

Back to the matter at hand, I feel I need to mention that although you can install it, and use Flake8 locally on your machine, organizations that are somewhat organized, also integrate it into their continuous integration(CI). This is done to ensure code quality, as it would prevent pushing code with syntax errors and obvious semantic errors to the remote repository hosting the project. Semantic errors though should ideally be caught by the tests you write.

**SETTING UP FLAKE8**

How, I got to setup flake8, was quite different. I ran the following command first, which simply created a file in that directory for me to write into. You could modify it to cater to whichever editor you have, I personally got used to sublime and kinda stuck to it.

 
```
subl .git/hooks/pre-commit

```
