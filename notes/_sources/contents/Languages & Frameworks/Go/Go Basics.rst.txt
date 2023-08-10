Go Basics
=========

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents:

Module
------
A go project is called go module. A module is not just source code and also includes dependencies specification for that moudle.

To create a module:

.. code-block:: console

   $ go mod init hello_world
   go: creating new go.mod: module hello_world

Code Style
----------
Most languages allow a great deal of flexibility on how code is formatted. Go does not. Enforcing a standard format makes it a great deal easier to write tools that manipulate source code. This simplifies the compiler and allows the creation of some clever tools for generating code.

#. Go programs use tabs to indent
#. Semicolons in go is optional, because it automatically inserts them wherever required
#. It is a syntax error if the opening brace is not on the same line as the declaration or command that begins the block.

The Go development tools include a command, ``go fmt``, which automatically fixes the whitespace in your code to match the standard format. However, it can't fix braces on the wrong line. Run it with:

.. code-block:: console

   $ go fmt ./...
   hello.go

Using ``./...`` tells a Go tool to apply the command to all the files in the current directory and all subdirectories.

Semicolon Insertion rule
~~~~~~~~~~~~~~~~~~~~~~~~
The go fmt command won't fix braces on the wrong line because of the semicolon insertion rule. Like C or Java, Go requires a semicolon at the end of every statement. However, Go developers should never put the semicolons in themselves. The Go compiler adds them automatically following a very simple rule

If the last token before a newline is any of the following, the lexer inserts a semicolon after the token:
   #. An identifier (which includes words like int and float64)
   #. A basic literal such as a number or string constant
   #. One of the tokens: “break,” “continue,” “fallthrough,” “return,” “++,” “--,” “),” or “}”

With this simple rule in place, you can see why putting a brace in the wrong place breaks. If you write your code like this:

.. code-block:: go

   func main()
   {
      fmt.Println("Hello, world!")
   }

the semicolon insertion rule sees the “)” at the end of the func main() line and turns that into:

.. code-block:: go

   func main();
   {
      fmt.Println("Hello, world!");
   }

and that’s not valid Go.

go vet
------
tODO

