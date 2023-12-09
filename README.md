# Python Parser Project

## Overview
This project involves the creation of a parser for a subset of the Python programming language. Using ANTLR (ANother Tool for Language Recognition), we have developed a grammar that can parse and interpret basic Python syntax including conditional statements, loops, and basic arithmetic operations. The parser is designed to be a foundational tool for further language processing and understanding tasks.

## Team Members
- Christian VanMeter
- Crew Gamble
- Drew Rothweil
- Joshua Jaworski
- Logan Brenningmeyer

## Requirements
### Environment Setup
To run this parser, you'll need the following environment setup:
1. **Windows subsystem for Linux**
2. **Ubunutu on WSL**
3. **ANTLR4 Tool**


## Installation
1. Clone the repository: git clone https://github.com/cvanmeter-rl/CS4450ParserProject

## How to Run the Parser
1. Compile ANTLR4 file: antlr4 -Dlanguage=Python3 Expr.g4
2. Run testcase: python3 Driver.py "your_testcase_file.py"
