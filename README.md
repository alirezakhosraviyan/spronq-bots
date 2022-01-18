
# SpronQ 💚 Backend Assessment

&nbsp;In this task I had to simulate robots that compare two numbers But the question is HOW ?

### Assumptions 🤔

- From sample input, Each bot **only** gets two inputs

### Approache 🥇

&emsp;Everything was **abstract**, and I tried to add **anything** that could add value to the code. So I created a command-line application using different design-patterns whose main command is the "analysis of microchips comparisons" by robots. I could create robots as separate **processes** or **threads**, but from what I assumed (based on the sample input you gave me) each robot receives only 2 inputs and to compare microchips at least 2 inputs is required, in fact, there is practically **no competition** between microchips to compare with **two** inputs, so I wrote the problem in **sync way**. Of course, I tried to create a closer and more realistic feel for the simulator by creating pipes and state-management.

To make the solution clearer, I tried to do the following steps:

- 1 ) I created a map of robots and outputbins with the data structure - which I described below - so that I could interate reecursively on the robots tree and compare their microchips.
- 2 ) I find robots that have 2 microchips in their state initialy as entry points and run the algorithm reecursively on the robots.
- 3 ) Print result in cosole

&emsp;However, although I have assumed that it will have only two inputs, the code has been designed in such a way that more inputs can be entered into the robot if necessary, or more rules can be added to the microchip in addition to a simple comparison.

### Technologies 🐍
    python3+

### Entities
- Bots : Stores two numbers as a state, then writes numbers on its output lines (Pipes) based on a list of rules and finally empties its state.
- Micro Chip : Holds a number (robots work on microchips)
- Output Bins : The output of robot operations is dumped between them in the last step

### Data Structure Classes 🏗️

#### State Management 
&emsp;Since robots as well as microchips have to store some value as a state to be processed, the state management class is designed.

#### Microchip
&emsp;In addition to storing data, microchips must be comparable, so their operators must be overloaded.

#### Bot
&emsp;In addition to maintaining the state (in this case, two microchips), robots must be able to compare microchips and transfer them to other robots.

#### Pipe

&emsp;To communicate between two robots, or more generally the relationship between one robot and several other robots, requires a concept on which information is written. Pipes can provide a connection between a robot and a robot or a robot with an output

#### Bin

&emsp;Is a concept inherited from the State Manager to store the output.

### Tools 🧰

#### Map Builder

#### Terminal

#### Command

### Installation 👨‍💻
```python
    git clone https://github.com/alirezakhosraviyan/spronq-bots.git

    cd spronq-bots

    python main.py
```


## Usage (usefule commands)  👨‍💻

#### Help 

```bash
      help
```
Sample: 
```bash
command # help

	analyze <input file>

	This command starts bot process with provided instruction input file
	PAY ATTENTION : file address must be relative (close to main.py file!)	and also add file extension if exists (inp.txt)
```

#### Analyze

```http
	analyze <input file>
```
Sample:
```bash
command # analyze inp2.txt
** RUNNING MAP **

----------------------------------------
Entry point  bot 2 : ('2', 'H:5', 'L:2') -> ('1', 'H:3', 'L:2') -> ('0', 'H:5', 'L:3') -> 
----------------------------------------

OUTPUT BINS : 
BIN [1] : 2

BIN [0] : 5

BIN [2] : 3

 ** ANALYZING FINISHED IN 0.00041413307189941406 seconds ** 
```


## 🚀 About Me
Please check my linkedin profile .. :)

https://www.linkedin.com/in/alirezakhosravian/