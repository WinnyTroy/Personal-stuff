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

This pre-commit file that you just created needs to be written into. Right? So this is what needs to go into the file:

```
git diff --staged --name-only | grep -E '.py$'| xargs flake8 --exclude=migrations -

```
Save the file, then close the session. 

The following command has 3 sections that do 3 ultimately different things. You can obviously tell that it is involved somehow with git since it has the git command at the prefix section. 

The first part that includes the 'git diff --staged --name-only' basically checks all the files in staging ready to be committed. 

The second section 'grep -E '.py$'’ runs through all the files that have been staged and basically picks out all the files that have a '.py' extension. 

The final bit 'xargs flake8 --exclude=migrations' is to instruct flake8 to exclude testing migration files when checking python files. This could also be modified to exclude other files, as mentioned earlier.

This file we just created is redundant. Basically, we just made a file, but what next? The next step should be to make this file executable. So, every time you stage files with git, it runs flake8 against the files that you are invoking it against. We do this by running the following command:

```
chmod +x .git/hooks/pre-commit

```
chmod is a very useful tool for managing rights (which can be read, write, or execute) the user and group that own a file, and other system users have on the file. 'x' stands for execution rights, allowing the file, in this case to be an executable file. The ‘+’ symbol basically grants all users (including those that are not part of the group that owns the file) the right to execute the file. The last segment is a file path to the pre-commit file we initially began making.

Now, your machine is configured with a pre-commit hook that runs flake8 against all the files you stage(Basically `git add`, and try commiting them, the hook fires the following message and aborts committing).

<img width="754" alt="screen shot 2018-12-18 at 10 52 45" src="https://user-images.githubusercontent.com/11174326/50140281-4450e880-02b5-11e9-8c97-2a6d6e8890a0.png">


But I also learned a simpler way. Running through [Flake8's documentation]()http://flake8.pycqa.org/en/latest/user/using-hooks.html, it instructs that you can install a built-in hook using the following command:

```
flake8 --install-hook git

```
This will install the pre-commit hook into the folder '.git/hooks/'. Just like before, to invoke flake8, you would need to be committing a file to git.

These were my discoveries for this time. I'm sure to keep you posted on more along the road to building my coding fortress
