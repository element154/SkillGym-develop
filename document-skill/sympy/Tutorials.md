## Source: https://docs.sympy.org/latest/tutorials/index.html

# Tutorials¶

Tutorials are the best place to start for anyone new to SymPy or one of SymPy’s features.

## Introductory Tutorial¶

If you are new to SymPy, start here.

## Physics Tutorial¶

For physics features in SymPy, start here.

Tutorials are the best place to start for anyone new to SymPy or one of SymPy’s features.

If you are new to SymPy, start here.

For physics features in SymPy, start here.

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html

# Introductory Tutorial¶

This tutorial aims to give an introduction to SymPy for someone who has not used the library before. Many features of SymPy will be introduced in this tutorial, but they will not be exhaustive. In fact, virtually every functionality shown in this tutorial will have more options or capabilities than what will be shown. The rest of the SymPy documentation serves as API documentation, which extensively lists every feature and option of each function.

These are the goals of this tutorial:

To give a guide, suitable for someone who has never used SymPy (but who has used Python and knows the necessary mathematics).

To be written in a narrative format, which is both easy and fun to follow. It should read like a book.

To give insightful examples and exercises, to help the reader learn and to make it entertaining to work through.

To introduce concepts in a logical order.

To use good practices and idioms, and avoid antipatterns. Functions or methodologies that tend to lead to antipatterns are avoided. Features that are only useful to advanced users are not shown.

To be consistent. If there are multiple ways to do it, only the best way is shown.

To avoid unnecessary duplication, it is assumed that previous sections of the tutorial have already been read.

Feedback on this tutorial, or on SymPy in general is always welcome. Just write to our mailing list.

**Content**

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/preliminaries.html

# Preliminaries¶

This tutorial assumes that the reader already knows the basics of the Python programming language. If you do not, the official Python tutorial is excellent.

This tutorial assumes a decent mathematical background. Most examples require knowledge lower than a calculus level, and some require knowledge at a calculus level. Some of the advanced features require more than this. If you come across a section that uses some mathematical function you are not familiar with, you can probably skip over it, or replace it with a similar one that you are more familiar with. Or look up the function on Wikipedia and learn something new. Some important mathematical concepts that are not common knowledge will be introduced as necessary.

## Installation¶

You will need to install SymPy first. See the installation guide.

## Exercises¶

This tutorial was the basis for a tutorial given at the 2013 SciPy conference in Austin, TX. The website for that tutorial is here. It has links to videos, materials, and IPython notebook exercises. The IPython notebook exercises in particular are recommended to anyone going through this tutorial.

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html

# Introduction¶

## What is Symbolic Computation?¶

Symbolic computation deals with the computation of mathematical objects symbolically. This means that the mathematical objects are represented exactly, not approximately, and mathematical expressions with unevaluated variables are left in symbolic form.

Let’s take an example. Say we wanted to use the built-in Python functions to compute square roots. We might do something like this

```
>>> import math
>>> math.sqrt(9)
3.0
```

9 is a perfect square, so we got the exact answer, 3. But suppose we computed the square root of a number that isn’t a perfect square

```
>>> math.sqrt(8)
2.82842712475
```

Here we got an approximate result. 2.82842712475 is not the exact square root of 8 (indeed, the actual square root of 8 cannot be represented by a finite decimal, since it is an irrational number). If all we cared about was the decimal form of the square root of 8, we would be done.

But suppose we want to go further. Recall that \(\sqrt{8} = \sqrt{4\cdot 2} = 2\sqrt{2}\). We would have a hard time deducing this from the above result. This is where symbolic computation comes in. With a symbolic computation system like SymPy, square roots of numbers that are not perfect squares are left unevaluated by default

```
>>> import sympy
>>> sympy.sqrt(3)
sqrt(3)
```

Furthermore—and this is where we start to see the real power of symbolic computation—symbolic results can be symbolically simplified.

```
>>> sympy.sqrt(8)
2*sqrt(2)
```

## A More Interesting Example¶

The above example starts to show how we can manipulate irrational numbers exactly using SymPy. But it is much more powerful than that. Symbolic computation systems (which by the way, are also often called computer algebra systems, or just CASs) such as SymPy are capable of computing symbolic expressions with variables.

As we will see later, in SymPy, variables are defined using `symbols`

.
Unlike many symbolic manipulation systems, variables in SymPy must be defined
before they are used (the reason for this will be discussed in the next
section).

Let us define a symbolic expression, representing the mathematical expression \(x + 2y\).

```
>>> from sympy import symbols
>>> x, y = symbols('x y')
>>> expr = x + 2*y
>>> expr
x + 2*y
```

Note that we wrote `x + 2*y`

just as we would if `x`

and `y`

were
ordinary Python variables. But in this case, instead of evaluating to
something, the expression remains as just `x + 2*y`

. Now let us play around
with it:

```
>>> expr + 1
x + 2*y + 1
>>> expr - x
2*y
```

Notice something in the above example. When we typed `expr - x`

, we did not
get `x + 2*y - x`

, but rather just `2*y`

. The `x`

and the `-x`

automatically canceled one another. This is similar to how `sqrt(8)`

automatically turned into `2*sqrt(2)`

above. This isn’t always the case in
SymPy, however:

```
>>> x*expr
x*(x + 2*y)
```

Here, we might have expected \(x(x + 2y)\) to transform into \(x^2 + 2xy\), but instead we see that the expression was left alone. This is a common theme in SymPy. Aside from obvious simplifications like \(x - x = 0\) and \(\sqrt{8} = 2\sqrt{2}\), most simplifications are not performed automatically. This is because we might prefer the factored form \(x(x + 2y)\), or we might prefer the expanded form \(x^2 + 2xy\). Both forms are useful in different circumstances. In SymPy, there are functions to go from one form to the other

```
>>> from sympy import expand, factor
>>> expanded_expr = expand(x*expr)
>>> expanded_expr
x**2 + 2*x*y
>>> factor(expanded_expr)
x*(x + 2*y)
```

## The Power of Symbolic Computation¶

The real power of a symbolic computation system such as SymPy is the ability to do all sorts of computations symbolically. SymPy can simplify expressions, compute derivatives, integrals, and limits, solve equations, work with matrices, and much, much more, and do it all symbolically. It includes modules for plotting, printing (like 2D pretty printed output of math formulas, or \(\mathrm{\LaTeX}\)), code generation, physics, statistics, combinatorics, number theory, geometry, logic, and more. Here is a small sampling of the sort of symbolic power SymPy is capable of, to whet your appetite.

```
>>> from sympy import *
>>> x, t, z, nu = symbols('x t z nu')
```

This will make all further examples pretty print with unicode characters.

```
>>> init_printing(use_unicode=True)
```

Take the derivative of \(\sin{(x)}e^x\).

```
>>> diff(sin(x)*exp(x), x)
x x
ℯ ⋅sin(x) + ℯ ⋅cos(x)
```

Compute \(\int(e^x\sin{(x)} + e^x\cos{(x)})\,dx\).

```
>>> integrate(exp(x)*sin(x) + exp(x)*cos(x), x)
x
ℯ ⋅sin(x)
```

Compute \(\int_{-\infty}^\infty \sin{(x^2)}\,dx\).

```
>>> integrate(sin(x**2), (x, -oo, oo))
√2⋅√π
─────
2
```

Find \(\lim_{x\to 0}\frac{\sin{(x)}}{x}\).

```
>>> limit(sin(x)/x, x, 0)
1
```

Solve \(x^2 - 2 = 0\).

```
>>> solve(x**2 - 2, x)
[-√2, √2]
```

Solve the differential equation \(y'' - y = e^t\).

```
>>> y = Function('y')
>>> dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))
-t ⎛ t⎞ t
y(t) = C₂⋅ℯ + ⎜C₁ + ─⎟⋅ℯ
⎝ 2⎠
```

Find the eigenvalues of \(\left[\begin{smallmatrix}1 & 2\\2 & 2\end{smallmatrix}\right]\).

```
>>> Matrix([[1, 2], [2, 2]]).eigenvals()
⎧3 √17 3 √17 ⎫
⎨─ - ───: 1, ─ + ───: 1⎬
⎩2 2 2 2 ⎭
```

Rewrite the Bessel function \(J_{\nu}\left(z\right)\) in terms of the spherical Bessel function \(j_\nu(z)\).

```
>>> besselj(nu, z).rewrite(jn)
√2⋅√z⋅jn(ν - 1/2, z)
────────────────────
√π
```

Print \(\int_{0}^{\pi} \cos^{2}{\left (x \right )}\, dx\) using \(\mathrm{\LaTeX}\).

```
>>> latex(Integral(cos(x)**2, (x, 0, pi)))
\int\limits_{0}^{\pi} \cos^{2}{\left(x \right)}\, dx
```

## Why SymPy?¶

There are many computer algebra systems out there. This Wikipedia article lists many of them. What makes SymPy a better choice than the alternatives?

First off, SymPy is completely free. It is open source, and licensed under the liberal BSD license, so you can modify the source code and even sell it if you want to. This contrasts with popular commercial systems like Maple or Mathematica that cost hundreds of dollars in licenses.

Second, SymPy uses Python. Most computer algebra systems invent their own language. Not SymPy. SymPy is written entirely in Python, and is executed entirely in Python. This means that if you already know Python, it is much easier to get started with SymPy, because you already know the syntax (and if you don’t know Python, it is really easy to learn). We already know that Python is a well-designed, battle-tested language. The SymPy developers are confident in their abilities in writing mathematical software, but programming language design is a completely different thing. By reusing an existing language, we are able to focus on those things that matter: the mathematics.

Another computer algebra system, Sage also uses Python as its language. But
Sage is large, with a download of over a gigabyte. An advantage of SymPy is
that it is lightweight. In addition to being relatively small, it has no
dependencies other than Python, so it can be used almost anywhere easily.
Furthermore, the goals of Sage and the goals of SymPy are different. Sage
aims to be a full featured system for mathematics, and aims to do so by
compiling all the major open source mathematical systems together into
one. When you call some function in Sage, such as `integrate`

, it calls out
to one of the open source packages that it includes. In fact, SymPy is
included in Sage. SymPy on the other hand aims to be an independent system,
with all the features implemented in SymPy itself.

A final important feature of SymPy is that it can be used as a library. Many computer algebra systems focus on being usable in interactive environments, but if you wish to automate or extend them, it is difficult to do. With SymPy, you can just as easily use it in an interactive Python environment or import it in your own Python application. SymPy also provides APIs to make it easy to extend it with your own custom functions.

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/features.html

SymPy Features¶ This section discusses the common and advanced SymPy operations and features. Content Basic Operations Substitution Converting Strings to SymPy Expressions evalf() lambdify() Printing Printers Setting up Pretty Printing Printing Functions Simplification simplify Polynomial/Rational Function Simplification Trigonometric Simplification Powers Exponentials and logarithms Special Functions Example: Continued Fractions Calculus Derivatives Integrals Numeric Integration Limits Series Expansion Finite differences Solvers A Note about Equations Solving Equations Algebraically Solving Differential Equations Matrices Basic Operations Basic Methods Matrix Constructors Advanced Methods Possible Issues Advanced Expression Manipulation Understanding Expression Trees Recursing through an Expression Tree Prevent expression evaluation

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html

# Basic Operations¶

Here we discuss some of the most basic operations needed for expression manipulation in SymPy. Some more advanced operations will be discussed later in the advanced expression manipulation section.

```
>>> from sympy import *
>>> x, y, z = symbols("x y z")
```

## Substitution¶

One of the most common things you might want to do with a mathematical
expression is substitution. Substitution replaces all instances of something
in an expression with something else. It is done using the
`subs()`

method.
For example

```
>>> expr = cos(x) + 1
>>> expr.subs(x, y)
cos(y) + 1
```

Substitution is usually done for one of two reasons:

Evaluating an expression at a point. For example, if our expression is

`cos(x) + 1`

and we want to evaluate it at the point`x = 0`

, so that we get`cos(0) + 1`

, which is 2.>>> expr.subs(x, 0) 2

Replacing a subexpression with another subexpression. There are two reasons we might want to do this. The first is if we are trying to build an expression that has some symmetry, such as \(x^{x^{x^x}}\). To build this, we might start with

`x**y`

, and replace`y`

with`x**y`

. We would then get`x**(x**y)`

. If we replaced`y`

in this new expression with`x**x`

, we would get`x**(x**(x**x))`

, the desired expression.>>> expr = x**y >>> expr x**y >>> expr = expr.subs(y, x**y) >>> expr x**(x**y) >>> expr = expr.subs(y, x**x) >>> expr x**(x**(x**x))

The second is if we want to perform a very controlled simplification, or perhaps a simplification that SymPy is otherwise unable to do. For example, say we have \(\sin(2x) + \cos(2x)\), and we want to replace \(\sin(2x)\) with \(2\sin(x)\cos(x)\). As we will learn later, the function

`expand_trig()`

does this. However, this function will also expand \(\cos(2x)\), which we may not want. While there are ways to perform such precise simplification, and we will learn some of them in the advanced expression manipulation section, an easy way is to just replace \(\sin(2x)\) with \(2\sin(x)\cos(x)\).>>> expr = sin(2*x) + cos(2*x) >>> expand_trig(expr) 2*sin(x)*cos(x) + 2*cos(x)**2 - 1 >>> expr.subs(sin(2*x), 2*sin(x)*cos(x)) 2*sin(x)*cos(x) + cos(2*x)

There are two important things to note about
`subs()`

. First, it returns a new expression.
SymPy objects are immutable. That means that
`subs()`

does not modify it in-place. For example

```
>>> expr = cos(x)
>>> expr.subs(x, 0)
1
>>> expr
cos(x)
>>> x
x
```

Here, we see that performing `expr.subs(x, 0)`

leaves `expr`

unchanged.
In fact, since SymPy expressions are immutable, no function will change them
in-place. All functions will return new expressions.

To perform multiple substitutions at once, pass a list of `(old, new)`

pairs
to `subs()`

.

```
>>> expr = x**3 + 4*x*y - z
>>> expr.subs([(x, 2), (y, 4), (z, 0)])
40
```

It is often useful to combine this with a list comprehension to do a large set of similar replacements all at once. For example, say we had \(x^4 - 4x^3 + 4x^2 - 2x + 3\) and we wanted to replace all instances of \(x\) that have an even power with \(y\), to get \(y^4 - 4x^3 + 4y^2 - 2x + 3\).

```
>>> expr = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
>>> replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
>>> expr.subs(replacements)
-4*x**3 - 2*x + y**4 + 4*y**2 + 3
```

## Converting Strings to SymPy Expressions¶

The `sympy.core.sympify.sympify()`

function (that’s
`sympy.core.sympify.sympify()`

, not to be confused with
`simplify()`

) can be used to convert strings into
SymPy expressions.

For example

```
>>> str_expr = "x**2 + 3*x - 1/2"
>>> expr = sympify(str_expr)
>>> expr
x**2 + 3*x - 1/2
>>> expr.subs(x, 2)
19/2
```

Warning

`sympy.core.sympify.sympify()`

uses `eval`

. Don’t use it on
unsanitized input.

`evalf()`

¶

To evaluate a numerical expression into a floating point number, use
`evalf()`

.

```
>>> expr = sqrt(8)
>>> expr.evalf()
2.82842712474619
```

SymPy can evaluate floating point expressions to arbitrary precision. By
default, 15 digits of precision are used, but you can pass any number as the
argument to `evalf()`

. Let’s compute the
first 100 digits of \(\pi\).

```
>>> pi.evalf(100)
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068
```

To numerically evaluate an expression with a Symbol at a point, we might use
`subs()`

followed by
`evalf()`

, but it is more efficient and
numerically stable to pass the substitution to
`evalf()`

using the
`subs()`

flag, which takes a dictionary of
`Symbol: point`

pairs.

```
>>> expr = cos(2*x)
>>> expr.evalf(subs={x: 2.4})
0.0874989834394464
```

Sometimes there are roundoff errors smaller than the desired precision that
remain after an expression is evaluated. Such numbers can be removed at the
user’s discretion by setting the `chop`

flag to True.

```
>>> one = cos(1)**2 + sin(1)**2
>>> (one - 1).evalf()
-0.e-124
>>> (one - 1).evalf(chop=True)
0
```

`lambdify()`

¶

`subs()`

and
`evalf()`

are good if you want to do simple
evaluation, but if you intend to evaluate an expression at many points, there
are more efficient ways. For example, if you wanted to evaluate an expression
at a thousand points, using SymPy would be far slower than it needs to be,
especially if you only care about machine precision. Instead, you should use
libraries like NumPy and SciPy.

The easiest way to convert a SymPy expression to an expression that can be
numerically evaluated is to use the `lambdify()`

function. `lambdify()`

acts like a `lambda`

function, except it converts the SymPy names to the names of the given
numerical library, usually NumPy. For example

```
>>> import numpy
>>> a = numpy.arange(10)
>>> expr = sin(x)
>>> f = lambdify(x, expr, "numpy")
>>> f(a)
[ 0. 0.84147098 0.90929743 0.14112001 -0.7568025 -0.95892427
-0.2794155 0.6569866 0.98935825 0.41211849]
```

Warning

`lambdify()`

uses `eval`

. Don’t
use it on unsanitized input.

You can use other libraries than NumPy. For example, to use the standard
library math module, use `"math"`

.

```
>>> f = lambdify(x, expr, "math")
>>> f(0.1)
0.0998334166468
```

To use lambdify with numerical libraries that it does not know about, pass a
dictionary of `sympy_name:numerical_function`

pairs. For example

```
>>> def mysin(x):
... """
... My sine. Note that this is only accurate for small x.
... """
... return x
>>> f = lambdify(x, expr, {"sin":mysin})
>>> f(0.1)
0.1
```

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/printing.html

# Printing¶

As we have already seen, SymPy can pretty print its output using Unicode characters. This is a short introduction to the most common printing options available in SymPy.

## Printers¶

There are several printers available in SymPy. The most common ones are

str

srepr

ASCII pretty printer

Unicode pretty printer

LaTeX

MathML

Dot

In addition to these, there are also “printers” that can output SymPy objects to code, such as C, Fortran, Javascript, Theano, and Python. These are not discussed in this tutorial.

## Setting up Pretty Printing¶

If all you want is the best pretty printing, use the `init_printing()`

function. This will automatically enable the best printer available in your
environment.

```
>>> from sympy import init_printing
>>> init_printing()
```

If you plan to work in an interactive calculator-type session, the
`init_session()`

function will automatically import everything in SymPy,
create some common Symbols, setup plotting, and run `init_printing()`

.

>>> from sympy import init_session >>> init_session()Python console for SymPy 1.13.0 (Python 3.12.4-64-bit) (ground types: gmpy) These commands were executed: >>> from sympy import * >>> x, y, z, t = symbols('x y z t') >>> k, m, n = symbols('k m n', integer=True) >>> f, g, h = symbols('f g h', cls=Function) >>> init_printing() # doctest: +SKIP Documentation can be found at https://docs.sympy.org/1.13.0/`>>>`

In any case, this is what will happen:

In the IPython QTConsole, if \(\mathrm{\LaTeX}\) is installed, it will enable a printer that uses \(\mathrm{\LaTeX}\).

If \(\mathrm{\LaTeX}\) is not installed, but Matplotlib is installed, it will use the Matplotlib rendering engine. If Matplotlib is not installed, it uses the Unicode pretty printer.

In the IPython notebook, it will use MathJax to render \(\mathrm{\LaTeX}\).

In an IPython console session, or a regular Python session, it will use the Unicode pretty printer if the terminal supports Unicode.

In a terminal that does not support Unicode, the ASCII pretty printer is used.

To explicitly not use \(\mathrm{\LaTeX}\), pass `use_latex=False`

to `init_printing()`

or `init_session()`

. To explicitly not use Unicode, pass
`use_unicode=False`

.

## Printing Functions¶

In addition to automatic printing, you can explicitly use any one of the printers by calling the appropriate function.

### str¶

To get a string form of an expression, use `str(expr)`

. This is also the
form that is produced by `print(expr)`

. String forms are designed to be
easy to read, but in a form that is correct Python syntax so that it can be
copied and pasted. The `str()`

form of an expression will usually look
exactly the same as the expression as you would enter it.

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> str(Integral(sqrt(1/x), x))
'Integral(sqrt(1/x), x)'
>>> print(Integral(sqrt(1/x), x))
Integral(sqrt(1/x), x)
```

### srepr¶

The srepr form of an expression is designed to show the exact form of an
expression. It will be discussed more in the Advanced Expression Manipulation
section. To get it, use `srepr()`

[1].

```
>>> srepr(Integral(sqrt(1/x), x))
"Integral(Pow(Pow(Symbol('x'), Integer(-1)), Rational(1, 2)), Tuple(Symbol('x')))"
```

The srepr form is mostly useful for understanding how an expression is built internally.

### ASCII Pretty Printer¶

The ASCII pretty printer is accessed from `pprint()`

. If the terminal does
not support Unicode, the ASCII printer is used by default. Otherwise, you
must pass `use_unicode=False`

.

```
>>> pprint(Integral(sqrt(1/x), x), use_unicode=False)
/
|
| ___
| / 1
| / - dx
| \/ x
|
/
```

`pprint()`

prints the output to the screen. If you want the string form,
use `pretty()`

.

```
>>> pretty(Integral(sqrt(1/x), x), use_unicode=False)
' / \n | \n | ___ \n | / 1 \n | / - dx\n | \\/ x \n | \n/ '
>>> print(pretty(Integral(sqrt(1/x), x), use_unicode=False))
/
|
| ___
| / 1
| / - dx
| \/ x
|
/
```

### Unicode Pretty Printer¶

The Unicode pretty printer is also accessed from `pprint()`

and
`pretty()`

. If the terminal supports Unicode, it is used automatically. If
`pprint()`

is not able to detect that the terminal supports unicode, you can
pass `use_unicode=True`

to force it to use Unicode.

```
>>> pprint(Integral(sqrt(1/x), x), use_unicode=True)
⌠
⎮ ___
⎮ ╱ 1
⎮ ╱ ─ dx
⎮ ╲╱ x
⌡
```

### \(\mathrm{\LaTeX}\)¶

To get the \(\mathrm{\LaTeX}\) form of an expression, use `latex()`

.

```
>>> print(latex(Integral(sqrt(1/x), x)))
\int \sqrt{\frac{1}{x}}\, dx
```

The `latex()`

function has many options to change the formatting of
different things. See `its documentation`

for more details.

### MathML¶

There is also a printer to MathML, called `print_mathml()`

. It must be
imported from `sympy.printing.mathml`

.

```
>>> from sympy.printing.mathml import print_mathml
>>> print_mathml(Integral(sqrt(1/x), x))
<apply>
<int/>
<bvar>
<ci>x</ci>
</bvar>
<apply>
<root/>
<apply>
<power/>
<ci>x</ci>
<cn>-1</cn>
</apply>
</apply>
</apply>
```

`print_mathml()`

prints the output. If you want the string, use the
function `mathml()`

.

### Dot¶

The `dotprint()`

function in `sympy.printing.dot`

prints output to dot
format, which can be rendered with Graphviz. See the
Advanced Expression Manipulation section for some examples of the output of this
printer.

Here is an example of the raw output of the `dotprint()`

function

```
>>> from sympy.printing.dot import dotprint
>>> from sympy.abc import x
>>> print(dotprint(x+2))
digraph{
# Graph style
"ordering"="out"
"rankdir"="TD"
#########
# Nodes #
#########
"Add(Integer(2), Symbol('x'))_()" ["color"="black", "label"="Add", "shape"="ellipse"];
"Integer(2)_(0,)" ["color"="black", "label"="2", "shape"="ellipse"];
"Symbol('x')_(1,)" ["color"="black", "label"="x", "shape"="ellipse"];
#########
# Edges #
#########
"Add(Integer(2), Symbol('x'))_()" -> "Integer(2)_(0,)";
"Add(Integer(2), Symbol('x'))_()" -> "Symbol('x')_(1,)";
}
```

Footnotes

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html

# Simplification¶

To make this document easier to read, we are going to enable pretty printing.

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> init_printing(use_unicode=True)
```

`simplify`

¶

Now let’s jump in and do some interesting mathematics. One of the most useful
features of a symbolic manipulation system is the ability to simplify
mathematical expressions. SymPy has dozens of functions to perform various
kinds of simplification. There is also one general function called
`simplify()`

that attempts to apply
all of these functions in an intelligent
way to arrive at the simplest form of an expression. Here are some examples

```
>>> simplify(sin(x)**2 + cos(x)**2)
1
>>> simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
x - 1
>>> simplify(gamma(x)/gamma(x - 2))
(x - 2)⋅(x - 1)
```

Here, `gamma(x)`

is \(\Gamma(x)\), the gamma function. We see that
`simplify()`

is capable of handling a large class of expressions.

But `simplify()`

has a pitfall. It
just applies all the major
simplification operations in SymPy, and uses heuristics to determine the
simplest result. But “simplest” is not a well-defined term. For example, say
we wanted to “simplify” \(x^2 + 2x + 1\) into \((x + 1)^2\):

```
>>> simplify(x**2 + 2*x + 1)
2
x + 2⋅x + 1
```

We did not get what we want. There is a function to perform this
simplification, called `factor()`

, which
will be discussed below.

Another pitfall to `simplify()`

is
that it can be unnecessarily slow, since
it tries many kinds of simplifications before picking the best one. If you
already know exactly what kind of simplification you are after, it is better
to apply the specific simplification function(s) that apply those
simplifications.

Applying specific simplification functions instead of
`simplify()`

also has
the advantage that specific functions have certain guarantees about the form
of their output. These will be discussed with each function below. For
example, `factor()`

, when called on a
polynomial with rational coefficients,
is guaranteed to factor the polynomial into irreducible factors.
`simplify()`

has no guarantees. It is
entirely heuristical, and, as we saw
above, it may even miss a possible type of simplification that SymPy is
capable of doing.

`simplify()`

is best when used
interactively, when you just want to whittle
down an expression to a simpler form. You may then choose to apply specific
functions once you see what `simplify()`

returns, to get a more precise result. It is also useful when you have no idea
what form an expression will take, and you need a catchall function to simplify it.

## Polynomial/Rational Function Simplification¶

### expand¶

`expand()`

is one of the most common simplification
functions in SymPy. Although it has a lot of scopes, for now, we will consider
its function in expanding polynomial expressions. For example:

```
>>> expand((x + 1)**2)
2
x + 2⋅x + 1
>>> expand((x + 2)*(x - 3))
2
x - x - 6
```

Given a polynomial, `expand()`

will put it into
a canonical form of a sum of monomials.

`expand()`

may not sound like a simplification
function. After all, by its very name, it makes expressions bigger, not
smaller. Usually this is the case, but often an expression will become
smaller upon calling on `expand()`

it due to cancellation.

```
>>> expand((x + 1)*(x - 2) - (x - 1)*x)
-2
```

### factor¶

`factor()`

takes a polynomial and factors
it into irreducible factors over
the rational numbers. For example:

```
>>> factor(x**3 - x**2 + x - 1)
⎛ 2 ⎞
(x - 1)⋅⎝x + 1⎠
>>> factor(x**2*z + 4*x*y*z + 4*y**2*z)
2
z⋅(x + 2⋅y)
```

For polynomials, `factor()`

is the opposite of
`expand()`

. `factor()`

uses a complete multivariate factorization algorithm over the rational
numbers, which means that each of the factors returned by
`factor()`

is
guaranteed to be irreducible.

If you are interested in the factors themselves, `factor_list`

returns a
more structured output.

```
>>> factor_list(x**2*z + 4*x*y*z + 4*y**2*z)
(1, [(z, 1), (x + 2⋅y, 2)])
```

Note that the input to `factor()`

and
`expand()`

need not be polynomials in
the strict sense. They will intelligently factor or expand any kind of
expression (though note that the factors may not be irreducible if the input
is no longer a polynomial over the rationals).

```
>>> expand((cos(x) + sin(x))**2)
2 2
sin (x) + 2⋅sin(x)⋅cos(x) + cos (x)
>>> factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2)
2
(sin(x) + cos(x))
```

### collect¶

`collect()`

collects common powers of a
term in an expression. For example

```
>>> expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
>>> expr
3 2 2
x - x ⋅z + 2⋅x + x⋅y + x - 3
>>> collected_expr = collect(expr, x)
>>> collected_expr
3 2
x + x ⋅(2 - z) + x⋅(y + 1) - 3
```

`collect()`

is particularly useful in
conjunction with the `coeff()`

method. `expr.coeff(x, n)`

gives the coefficient of `x**n`

in `expr`

:

```
>>> collected_expr.coeff(x, 2)
2 - z
```

### cancel¶

`cancel()`

will take any rational function
and put it into the standard
canonical form, \(\frac{p}{q}\), where \(p\) and \(q\) are expanded polynomials with
no common factors, and the leading coefficients of \(p\) and \(q\) do not have
denominators (i.e., are integers).

```
>>> cancel((x**2 + 2*x + 1)/(x**2 + x))
x + 1
─────
x
```

```
>>> expr = 1/x + (3*x/2 - 2)/(x - 4)
>>> expr
3⋅x
─── - 2
2 1
─────── + ─
x - 4 x
>>> cancel(expr)
2
3⋅x - 2⋅x - 8
──────────────
2
2⋅x - 8⋅x
```

```
>>> expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
>>> expr
2 2 2 2
x⋅y - 2⋅x⋅y⋅z + x⋅z + y - 2⋅y⋅z + z
───────────────────────────────────────
2
x - 1
>>> cancel(expr)
2 2
y - 2⋅y⋅z + z
───────────────
x - 1
```

Note that since `factor()`

will completely
factorize both the numerator and
the denominator of an expression, it can also be used to do the same thing:

```
>>> factor(expr)
2
(y - z)
────────
x - 1
```

However, if you are only interested in making sure that the expression is in
canceled form, `cancel()`

is more
efficient than `factor()`

.

### apart¶

`apart()`

performs a partial fraction
decomposition on a rational
function.

```
>>> expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
>>> expr
3 2
4⋅x + 21⋅x + 10⋅x + 12
────────────────────────
4 3 2
x + 5⋅x + 5⋅x + 4⋅x
>>> apart(expr)
2⋅x - 1 1 3
────────── - ───── + ─
2 x + 4 x
x + x + 1
```

## Trigonometric Simplification¶

Note

SymPy follows Python’s naming conventions for inverse trigonometric
functions, which is to append an `a`

to the front of the function’s
name. For example, the inverse cosine, or arc cosine, is called
`acos()`

.

```
>>> acos(x)
acos(x)
>>> cos(acos(x))
x
>>> asin(1)
π
─
2
```

### trigsimp¶

To simplify expressions using trigonometric identities, use
`trigsimp()`

.

```
>>> trigsimp(sin(x)**2 + cos(x)**2)
1
>>> trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
cos(4⋅x) 1
──────── + ─
2 2
>>> trigsimp(sin(x)*tan(x)/sec(x))
2
sin (x)
```

`trigsimp()`

also works with
hyperbolic trig functions.

```
>>> trigsimp(cosh(x)**2 + sinh(x)**2)
cosh(2⋅x)
>>> trigsimp(sinh(x)/tanh(x))
cosh(x)
```

Much like `simplify()`

,
`trigsimp()`

applies various
trigonometric identities to
the input expression, and then uses a heuristic to return the “best” one.

### expand_trig¶

To expand trigonometric functions, that is, apply the sum or double angle
identities, use `expand_trig()`

.

```
>>> expand_trig(sin(x + y))
sin(x)⋅cos(y) + sin(y)⋅cos(x)
>>> expand_trig(tan(2*x))
2⋅tan(x)
───────────
2
1 - tan (x)
```

Because `expand_trig()`

tends to make trigonometric
expressions larger, and `trigsimp()`

tends to
make them smaller, these identities can be applied in
reverse using `trigsimp()`

```
>>> trigsimp(sin(x)*cos(y) + sin(y)*cos(x))
sin(x + y)
```

## Powers¶

Before we introduce the power simplification functions, a mathematical discussion on the identities held by powers is in order. There are three kinds of identities satisfied by exponents

\(x^ax^b = x^{a + b}\)

\(x^ay^a = (xy)^a\)

\((x^a)^b = x^{ab}\)

Identity 1 is always true.

Identity 2 is not always true. For example, if \(x = y = -1\) and \(a = \frac{1}{2}\), then \(x^ay^a = \sqrt{-1}\sqrt{-1} = i\cdot i = -1\), whereas \((xy)^a = \sqrt{-1\cdot-1} = \sqrt{1} = 1\). However, identity 2 is true at least if \(x\) and \(y\) are nonnegative and \(a\) is real (it may also be true under other conditions as well). A common consequence of the failure of identity 2 is that \(\sqrt{x}\sqrt{y} \neq \sqrt{xy}\).

Identity 3 is not always true. For example, if \(x = -1\), \(a = 2\), and \(b = \frac{1}{2}\), then \((x^a)^b = {\left((-1)^2\right)}^{1/2} = \sqrt{1} = 1\) and \(x^{ab} = (-1)^{2\cdot1/2} = (-1)^1 = -1\). However, identity 3 is true when \(b\) is an integer (again, it may also hold in other cases as well). Two common consequences of the failure of identity 3 are that \(\sqrt{x^2}\neq x\) and that \(\sqrt{\frac{1}{x}} \neq \frac{1}{\sqrt{x}}\).

To summarize

Identity |
Sufficient conditions to hold |
Counterexample when conditions are not met |
Important consequences |
|---|---|---|---|
\(x^ax^b = x^{a + b}\)
|
Always true |
None |
None |
\(x^ay^a = (xy)^a\)
|
\(x, y \geq 0\) and \(a \in \mathbb{R}\) |
\((-1)^{1/2}(-1)^{1/2} \neq (-1\cdot-1)^{1/2}\) |
\(\sqrt{x}\sqrt{y} \neq \sqrt{xy}\) in general |
\((x^a)^b = x^{ab}\)
|
\(b \in \mathbb{Z}\) |
\({\left((-1)^2\right)}^{1/2} \neq (-1)^{2\cdot1/2}\) |
\(\sqrt{x^2}\neq x\) and \(\sqrt{\frac{1}{x}}\neq\frac{1}{\sqrt{x}}\) in general |

This is important to remember, because by default, SymPy will not perform simplifications if they are not true in general.

In order to make SymPy perform simplifications involving identities that are only true under certain assumptions, we need to put assumptions on our Symbols. We will undertake a full discussion of the assumptions system later, but for now, all we need to know are the following.

By default, SymPy Symbols are assumed to be complex (elements of \(\mathbb{C}\)). That is, a simplification will not be applied to an expression with a given Symbol unless it holds for all complex numbers.

Symbols can be given different assumptions by passing the assumption to

`symbols()`

. For the rest of this section, we will be assuming that`x`

and`y`

are positive, and that`a`

and`b`

are real. We will leave`z`

,`t`

, and`c`

as arbitrary complex Symbols to demonstrate what happens in that case.>>> x, y = symbols('x y', positive=True) >>> a, b = symbols('a b', real=True) >>> z, t, c = symbols('z t c')

Note

In SymPy, `sqrt(x)`

is just a shortcut to `x**Rational(1, 2)`

. They
are exactly the same object.

```
>>> sqrt(x) == x**Rational(1, 2)
True
```

### powsimp¶

`powsimp()`

applies identities 1 and 2
from above, from left to right.

```
>>> powsimp(x**a*x**b)
a + b
x
>>> powsimp(x**a*y**a)
a
(x⋅y)
```

Notice that :`powsimp()`

refuses to do
the simplification if it is not valid.

```
>>> powsimp(t**c*z**c)
c c
t ⋅z
```

If you know that you want to apply this simplification, but you don’t want to
mess with assumptions, you can pass the `force=True`

flag. This will force
the simplification to take place, regardless of assumptions.

```
>>> powsimp(t**c*z**c, force=True)
c
(t⋅z)
```

Note that in some instances, in particular, when the exponents are integers or rational numbers, and identity 2 holds, it will be applied automatically.

```
>>> (z*t)**2
2 2
t ⋅z
>>> sqrt(x*y)
√x⋅√y
```

This means that it will be impossible to undo this identity with
`powsimp()`

, because even if
`powsimp()`

were to put the bases
together,
they would be automatically split apart again.

```
>>> powsimp(z**2*t**2)
2 2
t ⋅z
>>> powsimp(sqrt(x)*sqrt(y))
√x⋅√y
```

### expand_power_exp / expand_power_base¶

`expand_power_exp()`

and
`expand_power_base()`

apply identities 1 and 2
from right to left, respectively.

```
>>> expand_power_exp(x**(a + b))
a b
x ⋅x
```

```
>>> expand_power_base((x*y)**a)
a a
x ⋅y
```

As with `powsimp()`

, identity 2 is not
applied if it is not valid.

```
>>> expand_power_base((z*t)**c)
c
(t⋅z)
```

And as with `powsimp()`

, you can force
the expansion to happen without
fiddling with assumptions by using `force=True`

.

```
>>> expand_power_base((z*t)**c, force=True)
c c
t ⋅z
```

As with identity 2, identity 1 is applied automatically if the power is a
number, and hence cannot be undone with `expand_power_exp()`

.

```
>>> x**2*x**3
5
x
>>> expand_power_exp(x**5)
5
x
```

### powdenest¶

`powdenest()`

applies identity 3, from
left to right.

```
>>> powdenest((x**a)**b)
a⋅b
x
```

As before, the identity is not applied if it is not true under the given assumptions.

```
>>> powdenest((z**a)**b)
b
⎛ a⎞
⎝z ⎠
```

And as before, this can be manually overridden with `force=True`

.

```
>>> powdenest((z**a)**b, force=True)
a⋅b
z
```

## Exponentials and logarithms¶

Note

In SymPy, as in Python and most programming languages, `log`

is the
natural logarithm, also known as `ln`

. SymPy automatically provides an
alias `ln = log`

in case you forget this.

```
>>> ln(x)
log(x)
```

Logarithms have similar issues as powers. There are two main identities

\(\log{(xy)} = \log{(x)} + \log{(y)}\)

\(\log{(x^n)} = n\log{(x)}\)

Neither identity is true for arbitrary complex \(x\) and \(y\), due to the branch cut in the complex plane for the complex logarithm. However, sufficient conditions for the identities to hold are if \(x\) and \(y\) are positive and \(n\) is real.

```
>>> x, y = symbols('x y', positive=True)
>>> n = symbols('n', real=True)
```

As before, `z`

and `t`

will be Symbols with no additional assumptions.

Note that the identity \(\log{\left(\frac{x}{y}\right)} = \log(x) - \log(y)\) is a special case of identities 1 and 2 by \(\log{\left(\frac{x}{y}\right)} =\) \(\log{\left(x\cdot\frac{1}{y}\right)} =\) \(\log(x) + \log{\left( y^{-1}\right)} =\) \(\log(x) - \log(y)\), and thus it also holds if \(x\) and \(y\) are positive, but may not hold in general.

We also see that \(\log{\left( e^x \right)} = x\) comes from \(\log{\left( e^x \right)} = x\log(e) = x\), and thus holds when \(x\) is real (and it can be verified that it does not hold in general for arbitrary complex \(x\), for example, \(\log{\left(e^{x + 2\pi i}\right)} = \log{\left(e^x\right)} = x \neq x + 2\pi i\)).

### expand_log¶

To apply identities 1 and 2 from left to right, use
`expand_log()`

. As always, the identities
will not be applied unless they are valid.

```
>>> expand_log(log(x*y))
log(x) + log(y)
>>> expand_log(log(x/y))
log(x) - log(y)
>>> expand_log(log(x**2))
2⋅log(x)
>>> expand_log(log(x**n))
n⋅log(x)
>>> expand_log(log(z*t))
log(t⋅z)
```

As with `powsimp()`

and
`powdenest()`

,
`expand_log()`

has a `force`

option that can be used to ignore assumptions.

```
>>> expand_log(log(z**2))
⎛ 2⎞
log⎝z ⎠
>>> expand_log(log(z**2), force=True)
2⋅log(z)
```

### logcombine¶

To apply identities 1 and 2 from right to left, use
`logcombine()`

.

```
>>> logcombine(log(x) + log(y))
log(x⋅y)
>>> logcombine(n*log(x))
⎛ n⎞
log⎝x ⎠
>>> logcombine(n*log(z))
n⋅log(z)
```

`logcombine()`

also has a `force`

option that can be used to ignore assumptions.

```
>>> logcombine(n*log(z), force=True)
⎛ n⎞
log⎝z ⎠
```

## Special Functions¶

SymPy implements dozens of special functions, ranging from functions in combinatorics to mathematical physics.

An extensive list of the special functions included with SymPy and their documentation is at the Functions Module page.

For the purposes of this tutorial, let’s introduce a few special functions in SymPy.

Let’s define `x`

, `y`

, and `z`

as regular, complex Symbols, removing any
assumptions we put on them in the previous section. We will also define `k`

,
`m`

, and `n`

.

```
>>> x, y, z = symbols('x y z')
>>> k, m, n = symbols('k m n')
```

The factorial function is
`factorial`

.
`factorial(n)`

represents \(n!= 1\cdot2\cdots(n - 1)\cdot
n\). \(n!\) represents the number of permutations of \(n\) distinct items.

```
>>> factorial(n)
n!
```

The binomial coefficient function is
`binomial`

.
`binomial(n, k)`

represents \(\binom{n}{k}\), the number of ways to
choose \(k\) items from a set of \(n\) distinct items. It is also often
written as \(nCk\), and is pronounced “\(n\) choose \(k\)”.

```
>>> binomial(n, k)
⎛n⎞
⎜ ⎟
⎝k⎠
```

The factorial function is closely related to the gamma function,
`gamma`

`gamma(z)`

represents \(\Gamma(z) = \int_0^\infty t^{z - 1}e^{-t}\,dt\), which for positive
integer
\(z\) is the same as \((z - 1)!\).

```
>>> gamma(z)
Γ(z)
```

The generalized hypergeometric function is
`hyper`

.
`hyper([a_1, ..., a_p], [b_1, ..., b_q], z)`

represents
\({}_pF_q\left(\begin{matrix} a_1, \cdots, a_p \\ b_1, \cdots, b_q \end{matrix}
\middle| z \right)\). The most common case is \({}_2F_1\), which is often
referred to as the ordinary hypergeometric function.

```
>>> hyper([1, 2], [3], z)
┌─ ⎛1, 2 │ ⎞
├─ ⎜ │ z⎟
2╵ 1 ⎝ 3 │ ⎠
```

### rewrite¶

A common way to deal with special functions is to rewrite them in terms of one
another. This works for any function in SymPy, not just special functions.
To rewrite an expression in terms of a function, use
`expr.rewrite(function)`

. For example,

```
>>> tan(x).rewrite(cos)
⎛ π⎞
cos⎜x - ─⎟
⎝ 2⎠
──────────
cos(x)
>>> factorial(x).rewrite(gamma)
Γ(x + 1)
```

For some tips on applying more targeted rewriting, see the Advanced Expression Manipulation section.

### expand_func¶

To expand special functions in terms of some identities, use
`expand_func()`

. For example

```
>>> expand_func(gamma(x + 3))
x⋅(x + 1)⋅(x + 2)⋅Γ(x)
```

### hyperexpand¶

To rewrite `hyper`

in terms of more standard functions, use
`hyperexpand()`

.

```
>>> hyperexpand(hyper([1, 1], [2], z))
-log(1 - z)
────────────
z
```

`hyperexpand()`

also works on
the more general Meijer G-function (see
`meijerg`

for more
information).

```
>>> expr = meijerg([[1],[1]], [[1],[]], -z)
>>> expr
╭─╮1, 1 ⎛1 1 │ ⎞
│╶┐ ⎜ │ -z⎟
╰─╯2, 1 ⎝1 │ ⎠
>>> hyperexpand(expr)
1
─
z
ℯ
```

### combsimp¶

To simplify combinatorial expressions, use
`combsimp()`

.

```
>>> n, k = symbols('n k', integer = True)
>>> combsimp(factorial(n)/factorial(n - 3))
n⋅(n - 2)⋅(n - 1)
>>> combsimp(binomial(n+1, k+1)/binomial(n, k))
n + 1
─────
k + 1
```

### gammasimp¶

To simplify expressions with gamma functions or combinatorial functions with
non-integer argument, use `gammasimp()`

.

```
>>> gammasimp(gamma(x)*gamma(1 - x))
π
────────
sin(π⋅x)
```

## Example: Continued Fractions¶

Let’s use SymPy to explore continued fractions. A continued fraction is an expression of the form

where \(a_0, \ldots, a_n\) are integers, and \(a_1, \ldots, a_n\) are positive. A continued fraction can also be infinite, but infinite objects are more difficult to represent in computers, so we will only examine the finite case here.

A continued fraction of the above form is often represented as a list \([a_0; a_1, \ldots, a_n]\). Let’s write a simple function that converts such a list to its continued fraction form. The easiest way to construct a continued fraction from a list is to work backwards. Note that despite the apparent symmetry of the definition, the first element, \(a_0\), must usually be handled differently from the rest.

```
>>> def list_to_frac(l):
... expr = Integer(0)
... for i in reversed(l[1:]):
... expr += i
... expr = 1/expr
... return l[0] + expr
>>> list_to_frac([x, y, z])
1
x + ─────
1
y + ─
z
```

We use `Integer(0)`

in `list_to_frac`

so that the result will always be a
SymPy object, even if we only pass in Python ints.

```
>>> list_to_frac([1, 2, 3, 4])
43
──
30
```

Every finite continued fraction is a rational number, but we are interested in
symbolics here, so let’s create a symbolic continued fraction. The
`symbols()`

function that we have been using
has a shortcut to create
numbered symbols. `symbols('a0:5')`

will create the symbols `a0`

, `a1`

,
…, `a4`

.

```
>>> syms = symbols('a0:5')
>>> syms
(a₀, a₁, a₂, a₃, a₄)
>>> a0, a1, a2, a3, a4 = syms
>>> frac = list_to_frac(syms)
>>> frac
1
a₀ + ─────────────────
1
a₁ + ────────────
1
a₂ + ───────
1
a₃ + ──
a₄
```

This form is useful for understanding continued fractions, but lets put it
into standard rational function form using
`cancel()`

.

```
>>> frac = cancel(frac)
>>> frac
a₀⋅a₁⋅a₂⋅a₃⋅a₄ + a₀⋅a₁⋅a₂ + a₀⋅a₁⋅a₄ + a₀⋅a₃⋅a₄ + a₀ + a₂⋅a₃⋅a₄ + a₂ + a₄
─────────────────────────────────────────────────────────────────────────
a₁⋅a₂⋅a₃⋅a₄ + a₁⋅a₂ + a₁⋅a₄ + a₃⋅a₄ + 1
```

Now suppose we were given `frac`

in the above canceled form. In fact, we
might be given the fraction in any form, but we can always put it into the
above canonical form with `cancel()`

.
Suppose that we knew that it could be
rewritten as a continued fraction. How could we do this with SymPy? A
continued fraction is recursively \(c + \frac{1}{f}\), where \(c\) is an integer
and \(f\) is a (smaller) continued fraction. If we could write the expression
in this form, we could pull out each \(c\) recursively and add it to a list. We
could then get a continued fraction with our `list_to_frac()`

function.

The key observation here is that we can convert an expression to the form \(c +
\frac{1}{f}\) by doing a partial fraction decomposition with respect to
\(c\). This is because \(f\) does not contain \(c\). This means we need to use the
`apart()`

function. We use
`apart()`

to pull the term out, then
subtract it from the expression, and take the reciprocal to get the \(f\) part.

```
>>> l = []
>>> frac = apart(frac, a0)
>>> frac
a₂⋅a₃⋅a₄ + a₂ + a₄
a₀ + ───────────────────────────────────────
a₁⋅a₂⋅a₃⋅a₄ + a₁⋅a₂ + a₁⋅a₄ + a₃⋅a₄ + 1
>>> l.append(a0)
>>> frac = 1/(frac - a0)
>>> frac
a₁⋅a₂⋅a₃⋅a₄ + a₁⋅a₂ + a₁⋅a₄ + a₃⋅a₄ + 1
───────────────────────────────────────
a₂⋅a₃⋅a₄ + a₂ + a₄
```

Now we repeat this process

```
>>> frac = apart(frac, a1)
>>> frac
a₃⋅a₄ + 1
a₁ + ──────────────────
a₂⋅a₃⋅a₄ + a₂ + a₄
>>> l.append(a1)
>>> frac = 1/(frac - a1)
>>> frac = apart(frac, a2)
>>> frac
a₄
a₂ + ─────────
a₃⋅a₄ + 1
>>> l.append(a2)
>>> frac = 1/(frac - a2)
>>> frac = apart(frac, a3)
>>> frac
1
a₃ + ──
a₄
>>> l.append(a3)
>>> frac = 1/(frac - a3)
>>> frac = apart(frac, a4)
>>> frac
a₄
>>> l.append(a4)
>>> list_to_frac(l)
1
a₀ + ─────────────────
1
a₁ + ────────────
1
a₂ + ───────
1
a₃ + ──
a₄
```

Of course, this exercise seems pointless, because we already know that our
`frac`

is `list_to_frac([a0, a1, a2, a3, a4])`

. So try the following
exercise. Take a list of symbols and randomize them, and create the canceled
continued fraction, and see if you can reproduce the original list. For
example

```
>>> import random
>>> l = list(symbols('a0:5'))
>>> random.shuffle(l)
>>> orig_frac = frac = cancel(list_to_frac(l))
>>> del l
```

In SymPy, on the above example, try to reproduce `l`

from
`frac`

. I have deleted `l`

at the end to remove the temptation for
peeking (you can check your answer at the end by calling
`cancel(list_to_frac(l))`

on the list that you generate at the end, and
comparing it to `orig_frac`

.

See if you can think of a way to figure out what symbol to pass to
`apart()`

at each stage (hint: think of what happens to \(a_0\) in the formula \(a_0 +
\frac{1}{a_1 + \cdots}\) when it is canceled).

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html

# Calculus¶

This section covers how to do basic calculus tasks such as derivatives, integrals, limits, and series expansions in SymPy. If you are not familiar with the math of any part of this section, you may safely skip it.

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> init_printing(use_unicode=True)
```

## Derivatives¶

To take derivatives, use the `diff()`

function.

```
>>> diff(cos(x), x)
-sin(x)
>>> diff(exp(x**2), x)
⎛ 2⎞
⎝x ⎠
2⋅x⋅ℯ
```

`diff()`

can take multiple derivatives at once. Totake multiple derivatives, pass the variable as many times as you wish to following find the third derivative of \(x^4\).

>>> diff(x**4, x, x, x) 24⋅x >>> diff(x**4, x, 3) 24⋅x

You can also take derivatives with respect to many variables at once. Just pass each derivative in order, using the same syntax as for single variable derivatives. For example, each of the following will compute \(\frac{\partial^7}{\partial x\partial y^2\partial z^4} e^{x y z}\).

```
>>> expr = exp(x*y*z)
>>> diff(expr, x, y, y, z, z, z, z)
3 2 ⎛ 3 3 3 2 2 2 ⎞ x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z + 14⋅x ⋅y ⋅z + 52⋅x⋅y⋅z + 48⎠⋅ℯ
>>> diff(expr, x, y, 2, z, 4)
3 2 ⎛ 3 3 3 2 2 2 ⎞ x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z + 14⋅x ⋅y ⋅z + 52⋅x⋅y⋅z + 48⎠⋅ℯ
>>> diff(expr, x, y, y, z, 4)
3 2 ⎛ 3 3 3 2 2 2 ⎞ x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z + 14⋅x ⋅y ⋅z + 52⋅x⋅y⋅z + 48⎠⋅ℯ
```

`diff()`

can also be called as a method. The two waysof calling

`diff()`

are exactly the same, and are provided only for convenience.>>> expr.diff(x, y, y, z, 4) 3 2 ⎛ 3 3 3 2 2 2 ⎞ x⋅y⋅z x ⋅y ⋅⎝x ⋅y ⋅z + 14⋅x ⋅y ⋅z + 52⋅x⋅y⋅z + 48⎠⋅ℯ

To create an unevaluated derivative, use the `Derivative`

class. It has the
same syntax as `diff()`

.

```
>>> deriv = Derivative(expr, x, y, y, z, 4)
>>> deriv
7
∂ ⎛ x⋅y⋅z⎞
──────────⎝ℯ ⎠
4 2
∂z ∂y ∂x
```

To evaluate an unevaluated derivative, use the
`doit()`

method.

```
>>> deriv.doit()
3 2 ⎛ 3 3 3 2 2 2 ⎞ x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z + 14⋅x ⋅y ⋅z + 52⋅x⋅y⋅z + 48⎠⋅ℯ
```

These unevaluated objects are useful for delaying the evaluation of the derivative, or for printing purposes. They are also used when SymPy does not know how to compute the derivative of an expression (for example, if it contains an undefined function, which are described in the Solving Differential Equations section).

Derivatives of unspecified order can be created using tuple `(x, n)`

where
`n`

is the order of the derivative with respect to `x`

.

```
>>> m, n, a, b = symbols('m n a b')
>>> expr = (a*x + b)**m
>>> expr.diff((x, n))
n
∂ ⎛ m⎞
───⎝(a⋅x + b) ⎠
n
∂x
```

## Integrals¶

To compute an integral, use the `integrate()`

function. There are two kinds of integrals, definite and indefinite. To
compute an indefinite integral, that is, an antiderivative, or primitive, just
pass the variable after the expression.

```
>>> integrate(cos(x), x)
sin(x)
```

Note that SymPy does not include the constant of integration. If you want it,
you can add one yourself, or rephrase your problem as a differential equation
and use `dsolve()`

to solve it, which does add the
constant (see Solving Differential Equations).

To compute a definite integral, pass the argument ```
(integration_variable,
lower_limit, upper_limit)
```

. For example, to compute

we would do

```
>>> integrate(exp(-x), (x, 0, oo))
1
```

As with indefinite integrals, you can pass multiple limit tuples to perform a multiple integral. For example, to compute

do

```
>>> integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
π
```

If `integrate()`

is unable to compute an
integral, it returns an unevaluated `Integral`

object.

```
>>> expr = integrate(x**x, x)
>>> print(expr)
Integral(x**x, x)
>>> expr
⌠
⎮ x
⎮ x dx
⌡
```

As with `Derivative`

, you can create an unevaluated integral using
`Integral`

. To later evaluate this integral, call
`doit()`

.

```
>>> expr = Integral(log(x)**2, x)
>>> expr
⌠
⎮ 2
⎮ log (x) dx
⌡
>>> expr.doit()
2
x⋅log (x) - 2⋅x⋅log(x) + 2⋅x
```

`integrate()`

uses powerful algorithms that are
always improving to compute both definite and indefinite integrals, including
heuristic pattern matching type algorithms, a partial implementation of the
Risch algorithm, and an
algorithm using
Meijer G-functions that is
useful for computing integrals in terms of special functions, especially
definite integrals. Here is a sampling of some of the power of
`integrate()`

.

```
>>> integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -
... exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
>>> integ
⌠
⎮ ⎛ 4 2 x 2 x x⎞ x
⎮ ⎝x + x ⋅ℯ - x - 2⋅x⋅ℯ - 2⋅x - ℯ ⎠⋅ℯ
⎮ ──────────────────────────────────────── dx
⎮ 2 2 ⎛ x ⎞
⎮ (x - 1) ⋅(x + 1) ⋅⎝ℯ + 1⎠
⌡
>>> integ.doit()
x
⎛ x ⎞ ℯ
log⎝ℯ + 1⎠ + ──────
2
x - 1
```

```
>>> integ = Integral(sin(x**2), x)
>>> integ
⌠
⎮ ⎛ 2⎞
⎮ sin⎝x ⎠ dx
⌡
>>> integ.doit()
⎛√2⋅x⎞
3⋅√2⋅√π⋅S⎜────⎟⋅Γ(3/4)
⎝ √π ⎠
──────────────────────
8⋅Γ(7/4)
```

```
>>> integ = Integral(x**y*exp(-x), (x, 0, oo))
>>> integ
∞
⌠
⎮ y -x
⎮ x ⋅ℯ dx
⌡
0
>>> integ.doit()
⎧ Γ(y + 1) for re(y) > -1
⎪
⎪∞
⎪⌠
⎨⎮ y -x
⎪⎮ x ⋅ℯ dx otherwise
⎪⌡
⎪0
⎩
```

This last example returned a `Piecewise`

expression because the integral
does not converge unless \(\Re(y) > -1.\)

## Numeric Integration¶

Numeric integration is a method employed in mathematical analysis to estimate
the definite integral of a function across a simplified range. SymPy not only
facilitates symbolic integration but also provides support for
numeric integration. It leverages the precision capabilities of the `mpmath`

library to enhance the accuracy of numeric integration calculations.

```
>>> from sympy import Integral, Symbol, sqrt
>>> x = Symbol('x')
>>> integral = Integral(sqrt(2)*x, (x, 0, 1))
>>> integral
1
⌠
⎮ √2⋅x dx
⌡
0
>>> integral.evalf()
0.707106781186548
```

To compute the integral with a specified precision:

```
>>> integral.evalf(50)
0.70710678118654752440084436210484903928483593768847
```

Numeric integration becomes a viable approach in situations where symbolic integration is impractical or impossible. This method allows for the computation of integrals through numerical techniques, even when dealing with infinite intervals or integrands:

```
>>> Integral(exp(-(x ** 2)), (x, -oo, oo)).evalf()
1.77245385090552
```

```
>>> Integral(1 / sqrt(x), (x, 0, 1)).evalf()
2.00000000000000
```

## Limits¶

SymPy can compute symbolic limits with the `limit()`

function. The syntax to compute

is `limit(f(x), x, x0)`

.

```
>>> limit(sin(x)/x, x, 0)
1
```

`limit()`

should be used instead of
`subs()`

whenever the point of evaluation is a
singularity. Even though SymPy has objects to represent \(\infty\), using them
for evaluation is not reliable because they do not keep track of things like
rate of growth. Also, things like \(\infty - \infty\) and
\(\frac{\infty}{\infty}\) return \(\mathrm{nan}\) (not-a-number). For example

```
>>> expr = x**2/exp(x)
>>> expr.subs(x, oo)
nan
>>> limit(expr, x, oo)
0
```

Like `Derivative`

and `Integral`

, `limit()`

has an unevaluated counterpart, `Limit`

. To evaluate it, use
`doit()`

.

```
>>> expr = Limit((cos(x) - 1)/x, x, 0)
>>> expr
⎛cos(x) - 1⎞
lim ⎜──────────⎟
x─→0⁺⎝ x ⎠
>>> expr.doit()
0
```

To evaluate a limit at one side only, pass `'+'`

or `'-'`

as a fourth
argument to `limit()`

. For example, to compute

do

```
>>> limit(1/x, x, 0, '+')
∞
```

As opposed to

```
>>> limit(1/x, x, 0, '-')
-∞
```

## Series Expansion¶

SymPy can compute asymptotic series expansions of functions around a point. To
compute the expansion of \(f(x)\) around the point \(x = x_0\) terms of order
\(x^n\), use `f(x).series(x, x0, n)`

. `x0`

and `n`

can be omitted, in
which case the defaults `x0=0`

and `n=6`

will be used.

```
>>> expr = exp(sin(x))
>>> expr.series(x, 0, 4)
2
x ⎛ 4⎞
1 + x + ── + O⎝x ⎠
2
```

The \(O\left(x^4\right)\) term at the end represents the Landau order term at
\(x=0\) (not to be confused with big O notation used in computer science, which
generally represents the Landau order term at \(x\) where \(x \rightarrow \infty\))
. It means that all x terms with power greater than or equal to \(x^4\) are
omitted. Order terms can be created and manipulated outside of `series`

.
They automatically absorb higher order terms.

```
>>> x + x**3 + x**6 + O(x**4)
3 ⎛ 4⎞
x + x + O⎝x ⎠
>>> x*O(1)
O(x)
```

If you do not want the order term, use the
`removeO()`

method.

```
>>> expr.series(x, 0, 4).removeO()
2
x
── + x + 1
2
```

The `O`

notation supports arbitrary limit points (other than 0):

```
>>> exp(x - 6).series(x, x0=6)
2 3 4 5
(x - 6) (x - 6) (x - 6) (x - 6) ⎛ 6 ⎞
-5 + ──────── + ──────── + ──────── + ──────── + x + O⎝(x - 6) ; x → 6⎠
2 6 24 120
```

## Finite differences¶

So far we have looked at expressions with analytic derivatives and primitive functions respectively. But what if we want to have an expression to estimate a derivative of a curve for which we lack a closed form representation, or for which we don’t know the functional values for yet. One approach would be to use a finite difference approach.

The simplest way the differentiate using finite differences is to use
the `differentiate_finite()`

function:

```
>>> f, g = symbols('f g', cls=Function)
>>> differentiate_finite(f(x)*g(x))
-f(x - 1/2)⋅g(x - 1/2) + f(x + 1/2)⋅g(x + 1/2)
```

If you already have a `Derivative`

instance, you can use the
`as_finite_difference()`

method to generate
approximations of the derivative to arbitrary order:

```
>>> f = Function('f')
>>> dfdx = f(x).diff(x)
>>> dfdx.as_finite_difference()
-f(x - 1/2) + f(x + 1/2)
```

here the first order derivative was approximated around x using a minimum number of points (2 for 1st order derivative) evaluated equidistantly using a step-size of 1. We can use arbitrary steps (possibly containing symbolic expressions):

```
>>> f = Function('f')
>>> d2fdx2 = f(x).diff(x, 2)
>>> h = Symbol('h')
>>> d2fdx2.as_finite_difference([-3*h,-h,2*h])
f(-3⋅h) f(-h) 2⋅f(2⋅h)
─────── - ───── + ────────
2 2 2
5⋅h 3⋅h 15⋅h
```

If you are just interested in evaluating the weights, you can do so manually:

```
>>> finite_diff_weights(2, [-3, -1, 2], 0)[-1][-1]
[1/5, -1/3, 2/15]
```

note that we only need the last element in the last sublist
returned from `finite_diff_weights`

. The reason for this is that
the function also generates weights for lower derivatives and
using fewer points (see the documentation of `finite_diff_weights`

for more details).

If using `finite_diff_weights`

directly looks complicated, and the
`as_finite_difference()`

method of
`Derivative`

instances is not flexible enough, you can use
`apply_finite_diff`

which takes `order`

, `x_list`

, `y_list`

and `x0`

as parameters:

```
>>> x_list = [-3, 1, 2]
>>> y_list = symbols('a b c')
>>> apply_finite_diff(1, x_list, y_list, 0)
3⋅a b 2⋅c
- ─── - ─ + ───
20 4 5
```

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html

# Solvers¶

Note

For a beginner-friendly guide focused on solving common types of equations, refer to Solve Equations.

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> init_printing(use_unicode=True)
```

## A Note about Equations¶

Recall from the gotchas section of this
tutorial that symbolic equations in SymPy are not represented by `=`

or
`==`

, but by `Eq`

.

```
>>> Eq(x, y)
x = y
```

However, there is an even easier way. In SymPy, any expression not in an
`Eq`

is automatically assumed to equal 0 by the solving functions. Since \(a
= b\) if and only if \(a - b = 0\), this means that instead of using `x == y`

,
you can just use `x - y`

. For example

```
>>> solveset(Eq(x**2, 1), x)
{-1, 1}
>>> solveset(Eq(x**2 - 1, 0), x)
{-1, 1}
>>> solveset(x**2 - 1, x)
{-1, 1}
```

This is particularly useful if the equation you wish to solve is already equal
to 0. Instead of typing `solveset(Eq(expr, 0), x)`

, you can just use
`solveset(expr, x)`

.

## Solving Equations Algebraically¶

The main function for solving algebraic equations is `solveset`

.
The syntax for `solveset`

is `solveset(equation, variable=None, domain=S.Complexes)`

Where `equations`

may be in the form of `Eq`

instances or expressions
that are assumed to be equal to zero.

Please note that there is another function called `solve`

which
can also be used to solve equations. The syntax is `solve(equations, variables)`

However, it is recommended to use `solveset`

instead.

When solving a single equation, the output of `solveset`

is a `FiniteSet`

or
an `Interval`

or `ImageSet`

of the solutions.

```
>>> solveset(x**2 - x, x)
{0, 1}
>>> solveset(x - x, x, domain=S.Reals)
ℝ
>>> solveset(sin(x) - 1, x, domain=S.Reals)
⎧ π │ ⎫
⎨2⋅n⋅π + ─ │ n ∊ ℤ⎬
⎩ 2 │ ⎭
```

If there are no solutions, an `EmptySet`

is returned and if it
is not able to find solutions then a `ConditionSet`

is returned.

```
>>> solveset(exp(x), x) # No solution exists
∅
>>> solveset(cos(x) - x, x) # Not able to find solution
{x │ x ∊ ℂ ∧ (-x + cos(x) = 0)}
```

In the `solveset`

module, the linear system of equations is solved using `linsolve`

.
In future we would be able to use linsolve directly from `solveset`

. Following
is an example of the syntax of `linsolve`

.

List of Equations Form:

>>> linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z)) {(-y - 1, y, 2)}

Augmented Matrix Form:

>>> linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z)) {(-y - 1, y, 2)}

A*x = b Form

>>> M = Matrix(((1, 1, 1, 1), (1, 1, 2, 3))) >>> system = A, b = M[:, :-1], M[:, -1] >>> linsolve(system, x, y, z) {(-y - 1, y, 2)}

Note

The order of solution corresponds the order of given symbols.

In the `solveset`

module, the non linear system of equations is solved using
`nonlinsolve`

. Following are examples of `nonlinsolve`

.

When only real solution is present:

>>> a, b, c, d = symbols('a, b, c, d', real=True) >>> nonlinsolve([a**2 + a, a - b], [a, b]) {(-1, -1), (0, 0)} >>> nonlinsolve([x*y - 1, x - 2], x, y) {(2, 1/2)}

When only complex solution is present:

>>> nonlinsolve([x**2 + 1, y**2 + 1], [x, y]) {(-ⅈ, -ⅈ), (-ⅈ, ⅈ), (ⅈ, -ⅈ), (ⅈ, ⅈ)}

When both real and complex solution are present:

>>> from sympy import sqrt >>> system = [x**2 - 2*y**2 -2, x*y - 2] >>> vars = [x, y] >>> nonlinsolve(system, vars) {(-2, -1), (2, 1), (-√2⋅ⅈ, √2⋅ⅈ), (√2⋅ⅈ, -√2⋅ⅈ)}

>>> system = [exp(x) - sin(y), 1/y - 3] >>> nonlinsolve(system, vars) {({2⋅n⋅ⅈ⋅π + log(sin(1/3)) │ n ∊ ℤ}, 1/3)}

When the system is positive-dimensional system (has infinitely many solutions):

>>> nonlinsolve([x*y, x*y - x], [x, y]) {(0, y)}

>>> system = [a**2 + a*c, a - b] >>> nonlinsolve(system, [a, b]) {(0, 0), (-c, -c)}

Note

The order of solution corresponds the order of given symbols.

2. Currently `nonlinsolve`

doesn’t return solution in form of `LambertW`

(if there
is solution present in the form of `LambertW`

).

`solve`

can be used for such cases:

```
>>> solve([x**2 - y**2/exp(x)], [x, y], dict=True)
⎡⎧ ____⎫ ⎧ ____⎫⎤
⎢⎨ ╱ x ⎬ ⎨ ╱ x ⎬⎥
⎣⎩y: -x⋅╲╱ ℯ ⎭, ⎩y: x⋅╲╱ ℯ ⎭⎦
>>> solve(x**2 - y**2/exp(x), x, dict=True)
⎡⎧ ⎛-y ⎞⎫ ⎧ ⎛y⎞⎫⎤
⎢⎨x: 2⋅W⎜───⎟⎬, ⎨x: 2⋅W⎜─⎟⎬⎥
⎣⎩ ⎝ 2 ⎠⎭ ⎩ ⎝2⎠⎭⎦
```

3. Currently `nonlinsolve`

is not properly capable of solving the system of equations
having trigonometric functions.

`solve`

can be used for such cases (but does not give all solution):

```
>>> solve([sin(x + y), cos(x - y)], [x, y])
⎡⎛-3⋅π 3⋅π⎞ ⎛-π π⎞ ⎛π 3⋅π⎞ ⎛3⋅π π⎞⎤
⎢⎜─────, ───⎟, ⎜───, ─⎟, ⎜─, ───⎟, ⎜───, ─⎟⎥
⎣⎝ 4 4 ⎠ ⎝ 4 4⎠ ⎝4 4 ⎠ ⎝ 4 4⎠⎦
```

`solveset`

reports each solution only once. To get the solutions of a
polynomial including multiplicity use `roots`

.

```
>>> solveset(x**3 - 6*x**2 + 9*x, x)
{0, 3}
>>> roots(x**3 - 6*x**2 + 9*x, x)
{0: 1, 3: 2}
```

The output `{0: 1, 3: 2}`

of `roots`

means that `0`

is a root of
multiplicity 1 and `3`

is a root of multiplicity 2.

Note

Currently `solveset`

is not capable of solving the following types of equations:

Equations solvable by LambertW (Transcendental equation solver).

`solve`

can be used for such cases:

```
>>> solve(x*exp(x) - 1, x )
[W(1)]
```

## Solving Differential Equations¶

To solve differential equations, use `dsolve`

. First, create an undefined
function by passing `cls=Function`

to the `symbols`

function.

```
>>> f, g = symbols('f g', cls=Function)
```

`f`

and `g`

are now undefined functions. We can call `f(x)`

, and it
will represent an unknown function.

```
>>> f(x)
f(x)
```

Derivatives of `f(x)`

are unevaluated.

```
>>> f(x).diff(x)
d
──(f(x))
dx
```

(see the Derivatives section for more on derivatives).

To represent the differential equation \(f''(x) - 2f'(x) + f(x) = \sin(x)\), we would thus use

```
>>> diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
>>> diffeq
2
d d
f(x) - 2⋅──(f(x)) + ───(f(x)) = sin(x)
dx 2
dx
```

To solve the ODE, pass it and the function to solve for to `dsolve`

.

```
>>> dsolve(diffeq, f(x))
x cos(x)
f(x) = (C₁ + C₂⋅x)⋅ℯ + ──────
2
```

`dsolve`

returns an instance of `Eq`

. This is because, in general,
solutions to differential equations cannot be solved explicitly for the
function.

```
>>> dsolve(f(x).diff(x)*(1 - sin(f(x))) - 1, f(x))
x - f(x) - cos(f(x)) = C₁
```

The arbitrary constants in the solutions from dsolve are symbols of the form
`C1`

, `C2`

, `C3`

, and so on.

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html

# Matrices¶

```
>>> from sympy import *
>>> init_printing(use_unicode=True)
```

To make a matrix in SymPy, use the `Matrix`

object. A matrix is constructed
by providing a list of row vectors that make up the matrix. For example,
to construct the matrix

use

```
>>> Matrix([[1, -1], [3, 4], [0, 2]])
⎡1 -1⎤
⎢ ⎥
⎢3 4 ⎥
⎢ ⎥
⎣0 2 ⎦
```

To make it easy to make column vectors, a list of elements is considered to be a column vector.

```
>>> Matrix([1, 2, 3])
⎡1⎤
⎢ ⎥
⎢2⎥
⎢ ⎥
⎣3⎦
```

Matrices are manipulated just like any other object in SymPy or Python.

```
>>> M = Matrix([[1, 2, 3], [3, 2, 1]])
>>> N = Matrix([0, 1, 1])
>>> M*N
⎡5⎤
⎢ ⎥
⎣3⎦
```

One important thing to note about SymPy matrices is that, unlike every other
object in SymPy, they are mutable. This means that they can be modified in
place, as we will see below. The downside to this is that `Matrix`

cannot
be used in places that require immutability, such as inside other SymPy
expressions or as keys to dictionaries. If you need an immutable version of
`Matrix`

, use `ImmutableMatrix`

.

## Basic Operations¶

Here are some basic operations on `Matrix`

.

### Shape¶

To get the shape of a matrix, use `shape()`

function.

```
>>> from sympy import shape
>>> M = Matrix([[1, 2, 3], [-2, 0, 4]])
>>> M
⎡1 2 3⎤
⎢ ⎥
⎣-2 0 4⎦
>>> shape(M)
(2, 3)
```

### Accessing Rows and Columns¶

To get an individual row or column of a matrix, use `row`

or `col`

. For
example, `M.row(0)`

will get the first row. `M.col(-1)`

will get the last
column.

```
>>> M.row(0)
[1 2 3]
>>> M.col(-1)
⎡3⎤
⎢ ⎥
⎣4⎦
```

### Deleting and Inserting Rows and Columns¶

To delete a row or column, use `row_del`

or `col_del`

. These operations
will modify the Matrix **in place**.

```
>>> M.col_del(0)
>>> M
⎡2 3⎤
⎢ ⎥
⎣0 4⎦
>>> M.row_del(1)
>>> M
[2 3]
```

To insert rows or columns, use `row_insert`

or `col_insert`

. These
operations **do not** operate in place.

```
>>> M
[2 3]
>>> M = M.row_insert(1, Matrix([[0, 4]]))
>>> M
⎡2 3⎤
⎢ ⎥
⎣0 4⎦
>>> M = M.col_insert(0, Matrix([1, -2]))
>>> M
⎡1 2 3⎤
⎢ ⎥
⎣-2 0 4⎦
```

Unless explicitly stated, the methods mentioned below do not operate in
place. In general, a method that does not operate in place will return a new
`Matrix`

and a method that does operate in place will return `None`

.

## Basic Methods¶

As noted above, simple operations like addition, multiplication and power are
done just by using `+`

, `*`

, and `**`

. To find the inverse of a matrix,
just raise it to the `-1`

power.

```
>>> M = Matrix([[1, 3], [-2, 3]])
>>> N = Matrix([[0, 3], [0, 7]])
>>> M + N
⎡1 6 ⎤
⎢ ⎥
⎣-2 10⎦
>>> M*N
⎡0 24⎤
⎢ ⎥
⎣0 15⎦
>>> 3*M
⎡3 9⎤
⎢ ⎥
⎣-6 9⎦
>>> M**2
⎡-5 12⎤
⎢ ⎥
⎣-8 3 ⎦
>>> M**-1
⎡1/3 -1/3⎤
⎢ ⎥
⎣2/9 1/9 ⎦
>>> N**-1
Traceback (most recent call last):
...
NonInvertibleMatrixError: Matrix det == 0; not invertible.
```

To take the transpose of a Matrix, use `T`

.

```
>>> M = Matrix([[1, 2, 3], [4, 5, 6]])
>>> M
⎡1 2 3⎤
⎢ ⎥
⎣4 5 6⎦
>>> M.T
⎡1 4⎤
⎢ ⎥
⎢2 5⎥
⎢ ⎥
⎣3 6⎦
```

## Matrix Constructors¶

Several constructors exist for creating common matrices. To create an
identity matrix, use `eye`

. `eye(n)`

will create an \(n\times n\) identity matrix.

```
>>> eye(3)
⎡1 0 0⎤
⎢ ⎥
⎢0 1 0⎥
⎢ ⎥
⎣0 0 1⎦
>>> eye(4)
⎡1 0 0 0⎤
⎢ ⎥
⎢0 1 0 0⎥
⎢ ⎥
⎢0 0 1 0⎥
⎢ ⎥
⎣0 0 0 1⎦
```

To create a matrix of all zeros, use `zeros`

. `zeros(n, m)`

creates an
\(n\times m\) matrix of \(0\)s.

```
>>> zeros(2, 3)
⎡0 0 0⎤
⎢ ⎥
⎣0 0 0⎦
```

Similarly, `ones`

creates a matrix of ones.

```
>>> ones(3, 2)
⎡1 1⎤
⎢ ⎥
⎢1 1⎥
⎢ ⎥
⎣1 1⎦
```

To create diagonal matrices, use `diag`

. The arguments to `diag`

can be
either numbers or matrices. A number is interpreted as a \(1\times 1\)
matrix. The matrices are stacked diagonally. The remaining elements are
filled with \(0\)s.

```
>>> diag(1, 2, 3)
⎡1 0 0⎤
⎢ ⎥
⎢0 2 0⎥
⎢ ⎥
⎣0 0 3⎦
>>> diag(-1, ones(2, 2), Matrix([5, 7, 5]))
⎡-1 0 0 0⎤
⎢ ⎥
⎢0 1 1 0⎥
⎢ ⎥
⎢0 1 1 0⎥
⎢ ⎥
⎢0 0 0 5⎥
⎢ ⎥
⎢0 0 0 7⎥
⎢ ⎥
⎣0 0 0 5⎦
```

## Advanced Methods¶

### Determinant¶

To compute the determinant of a matrix, use `det`

.

```
>>> M = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
>>> M
⎡1 0 1⎤
⎢ ⎥
⎢2 -1 3⎥
⎢ ⎥
⎣4 3 2⎦
>>> M.det()
-1
```

### RREF¶

To put a matrix into reduced row echelon form, use `rref`

. `rref`

returns
a tuple of two elements. The first is the reduced row echelon form, and the
second is a tuple of indices of the pivot columns.

```
>>> M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
>>> M
⎡1 0 1 3 ⎤
⎢ ⎥
⎢2 3 4 7 ⎥
⎢ ⎥
⎣-1 -3 -3 -4⎦
>>> M.rref()
⎛⎡1 0 1 3 ⎤ ⎞
⎜⎢ ⎥ ⎟
⎜⎢0 1 2/3 1/3⎥, (0, 1)⎟
⎜⎢ ⎥ ⎟
⎝⎣0 0 0 0 ⎦ ⎠
```

Note

The first element of the tuple returned by `rref`

is of type
`Matrix`

. The second is of type `tuple`

.

### Nullspace¶

To find the nullspace of a matrix, use `nullspace`

. `nullspace`

returns a
`list`

of column vectors that span the nullspace of the matrix.

```
>>> M = Matrix([[1, 2, 3, 0, 0], [4, 10, 0, 0, 1]])
>>> M
⎡1 2 3 0 0⎤
⎢ ⎥
⎣4 10 0 0 1⎦
>>> M.nullspace()
⎡⎡-15⎤ ⎡0⎤ ⎡ 1 ⎤⎤
⎢⎢ ⎥ ⎢ ⎥ ⎢ ⎥⎥
⎢⎢ 6 ⎥ ⎢0⎥ ⎢-1/2⎥⎥
⎢⎢ ⎥ ⎢ ⎥ ⎢ ⎥⎥
⎢⎢ 1 ⎥, ⎢0⎥, ⎢ 0 ⎥⎥
⎢⎢ ⎥ ⎢ ⎥ ⎢ ⎥⎥
⎢⎢ 0 ⎥ ⎢1⎥ ⎢ 0 ⎥⎥
⎢⎢ ⎥ ⎢ ⎥ ⎢ ⎥⎥
⎣⎣ 0 ⎦ ⎣0⎦ ⎣ 1 ⎦⎦
```

### Columnspace¶

To find the columnspace of a matrix, use `columnspace`

. `columnspace`

returns a
`list`

of column vectors that span the columnspace of the matrix.

```
>>> M = Matrix([[1, 1, 2], [2 ,1 , 3], [3 , 1, 4]])
>>> M
⎡1 1 2⎤
⎢ ⎥
⎢2 1 3⎥
⎢ ⎥
⎣3 1 4⎦
>>> M.columnspace()
⎡⎡1⎤ ⎡1⎤⎤
⎢⎢ ⎥ ⎢ ⎥⎥
⎢⎢2⎥, ⎢1⎥⎥
⎢⎢ ⎥ ⎢ ⎥⎥
⎣⎣3⎦ ⎣1⎦⎦
```

### Eigenvalues, Eigenvectors, and Diagonalization¶

To find the eigenvalues of a matrix, use `eigenvals`

. `eigenvals`

returns a dictionary of `eigenvalue: algebraic_multiplicity`

pairs (similar to the
output of roots).

```
>>> M = Matrix([[3, -2, 4, -2], [5, 3, -3, -2], [5, -2, 2, -2], [5, -2, -3, 3]])
>>> M
⎡3 -2 4 -2⎤
⎢ ⎥
⎢5 3 -3 -2⎥
⎢ ⎥
⎢5 -2 2 -2⎥
⎢ ⎥
⎣5 -2 -3 3 ⎦
>>> M.eigenvals()
{-2: 1, 3: 1, 5: 2}
```

This means that `M`

has eigenvalues -2, 3, and 5, and that the
eigenvalues -2 and 3 have algebraic multiplicity 1 and that the eigenvalue 5
has algebraic multiplicity 2.

To find the eigenvectors of a matrix, use `eigenvects`

. `eigenvects`

returns a list of tuples of the form ```
(eigenvalue, algebraic_multiplicity,
[eigenvectors])
```

.

```
>>> M.eigenvects()
⎡⎛ ⎡⎡0⎤⎤⎞ ⎛ ⎡⎡1⎤⎤⎞ ⎛ ⎡⎡1⎤ ⎡0 ⎤⎤⎞⎤
⎢⎜ ⎢⎢ ⎥⎥⎟ ⎜ ⎢⎢ ⎥⎥⎟ ⎜ ⎢⎢ ⎥ ⎢ ⎥⎥⎟⎥
⎢⎜ ⎢⎢1⎥⎥⎟ ⎜ ⎢⎢1⎥⎥⎟ ⎜ ⎢⎢1⎥ ⎢-1⎥⎥⎟⎥
⎢⎜-2, 1, ⎢⎢ ⎥⎥⎟, ⎜3, 1, ⎢⎢ ⎥⎥⎟, ⎜5, 2, ⎢⎢ ⎥, ⎢ ⎥⎥⎟⎥
⎢⎜ ⎢⎢1⎥⎥⎟ ⎜ ⎢⎢1⎥⎥⎟ ⎜ ⎢⎢1⎥ ⎢0 ⎥⎥⎟⎥
⎢⎜ ⎢⎢ ⎥⎥⎟ ⎜ ⎢⎢ ⎥⎥⎟ ⎜ ⎢⎢ ⎥ ⎢ ⎥⎥⎟⎥
⎣⎝ ⎣⎣1⎦⎦⎠ ⎝ ⎣⎣1⎦⎦⎠ ⎝ ⎣⎣0⎦ ⎣1 ⎦⎦⎠⎦
```

This shows us that, for example, the eigenvalue 5 also has geometric
multiplicity 2, because it has two eigenvectors. Because the algebraic and
geometric multiplicities are the same for all the eigenvalues, `M`

is
diagonalizable.

To diagonalize a matrix, use `diagonalize`

. `diagonalize`

returns a tuple
\((P, D)\), where \(D\) is diagonal and \(M = PDP^{-1}\).

```
>>> P, D = M.diagonalize()
>>> P
⎡0 1 1 0 ⎤
⎢ ⎥
⎢1 1 1 -1⎥
⎢ ⎥
⎢1 1 1 0 ⎥
⎢ ⎥
⎣1 1 0 1 ⎦
>>> D
⎡-2 0 0 0⎤
⎢ ⎥
⎢0 3 0 0⎥
⎢ ⎥
⎢0 0 5 0⎥
⎢ ⎥
⎣0 0 0 5⎦
>>> P*D*P**-1
⎡3 -2 4 -2⎤
⎢ ⎥
⎢5 3 -3 -2⎥
⎢ ⎥
⎢5 -2 2 -2⎥
⎢ ⎥
⎣5 -2 -3 3 ⎦
>>> P*D*P**-1 == M
True
```

Note that since `eigenvects`

also includes the eigenvalues, you should use
it instead of `eigenvals`

if you also want the eigenvectors. However, as
computing the eigenvectors may often be costly, `eigenvals`

should be
preferred if you only wish to find the eigenvalues.

If all you want is the characteristic polynomial, use `charpoly`

. This is
more efficient than `eigenvals`

, because sometimes symbolic roots can be
expensive to calculate.

```
>>> lamda = symbols('lamda')
>>> p = M.charpoly(lamda)
>>> factor(p.as_expr())
2
(λ - 5) ⋅(λ - 3)⋅(λ + 2)
```

## Possible Issues¶

### Zero Testing¶

If your matrix operations are failing or returning wrong answers, the common reasons would likely be from zero testing. If there is an expression not properly zero-tested, it can possibly bring issues in finding pivots for gaussian elimination, or deciding whether the matrix is inversible, or any high level functions which relies on the prior procedures.

Currently, the SymPy’s default method of zero testing `_iszero`

is only
guaranteed to be accurate in some limited domain of numerics and symbols,
and any complicated expressions beyond its decidability are treated as `None`

,
which behaves similarly to logical `False`

.

The list of methods using zero testing procedures are as follows:

`echelon_form`

, `is_echelon`

, `rank`

, `rref`

, `nullspace`

,
`eigenvects`

, `inverse_ADJ`

, `inverse_GE`

, `inverse_LU`

,
`LUdecomposition`

, `LUdecomposition_Simple`

, `LUsolve`

They have property `iszerofunc`

opened up for user to specify zero testing
method, which can accept any function with single input and boolean output,
while being defaulted with `_iszero`

.

Here is an example of solving an issue caused by undertested zero. While the output for this particular matrix has since been improved, the technique below is still of interest. [1] [2] [3]

```
>>> from sympy import *
>>> q = Symbol("q", positive = True)
>>> m = Matrix([
... [-2*cosh(q/3), exp(-q), 1],
... [ exp(q), -2*cosh(q/3), 1],
... [ 1, 1, -2*cosh(q/3)]])
>>> m.nullspace()
[]
```

You can trace down which expression is being underevaluated, by injecting a custom zero test with warnings enabled.

```
>>> import warnings
>>>
>>> def my_iszero(x):
... result = x.is_zero
...
... # Warnings if evaluated into None
... if result is None:
... warnings.warn("Zero testing of {} evaluated into None".format(x))
... return result
...
>>> m.nullspace(iszerofunc=my_iszero)
__main__:9: UserWarning: Zero testing of 4*cosh(q/3)**2 - 1 evaluated into None
__main__:9: UserWarning: Zero testing of (-exp(q) - 2*cosh(q/3))*(-2*cosh(q/3) - exp(-q)) - (4*cosh(q/3)**2 - 1)**2 evaluated into None
__main__:9: UserWarning: Zero testing of 2*exp(q)*cosh(q/3) - 16*cosh(q/3)**4 + 12*cosh(q/3)**2 + 2*exp(-q)*cosh(q/3) evaluated into None
__main__:9: UserWarning: Zero testing of -(4*cosh(q/3)**2 - 1)*exp(-q) - 2*cosh(q/3) - exp(-q) evaluated into None
[]
```

In this case,
`(-exp(q) - 2*cosh(q/3))*(-2*cosh(q/3) - exp(-q)) - (4*cosh(q/3)**2 - 1)**2`

should yield zero, but the zero testing had failed to catch.
possibly meaning that a stronger zero test should be introduced.
For this specific example, rewriting to exponentials and applying simplify would
make zero test stronger for hyperbolics,
while being harmless to other polynomials or transcendental functions.

```
>>> def my_iszero(x):
... result = x.rewrite(exp).simplify().is_zero
...
... # Warnings if evaluated into None
... if result is None:
... warnings.warn("Zero testing of {} evaluated into None".format(x))
... return result
...
>>> m.nullspace(iszerofunc=my_iszero)
__main__:9: UserWarning: Zero testing of -2*cosh(q/3) - exp(-q) evaluated into None
⎡⎡ ⎛ q ⎛q⎞⎞ -q 2⎛q⎞ ⎤⎤
⎢⎢- ⎜- ℯ - 2⋅cosh⎜─⎟⎟⋅ℯ + 4⋅cosh ⎜─⎟ - 1⎥⎥
⎢⎢ ⎝ ⎝3⎠⎠ ⎝3⎠ ⎥⎥
⎢⎢─────────────────────────────────────────⎥⎥
⎢⎢ ⎛ 2⎛q⎞ ⎞ ⎛q⎞ ⎥⎥
⎢⎢ 2⋅⎜4⋅cosh ⎜─⎟ - 1⎟⋅cosh⎜─⎟ ⎥⎥
⎢⎢ ⎝ ⎝3⎠ ⎠ ⎝3⎠ ⎥⎥
⎢⎢ ⎥⎥
⎢⎢ ⎛ q ⎛q⎞⎞ ⎥⎥
⎢⎢ -⎜- ℯ - 2⋅cosh⎜─⎟⎟ ⎥⎥
⎢⎢ ⎝ ⎝3⎠⎠ ⎥⎥
⎢⎢ ──────────────────── ⎥⎥
⎢⎢ 2⎛q⎞ ⎥⎥
⎢⎢ 4⋅cosh ⎜─⎟ - 1 ⎥⎥
⎢⎢ ⎝3⎠ ⎥⎥
⎢⎢ ⎥⎥
⎣⎣ 1 ⎦⎦
```

You can clearly see `nullspace`

returning proper result, after injecting an
alternative zero test.

Note that this approach is only valid for some limited cases of matrices containing only numerics, hyperbolics, and exponentials. For other matrices, you should use different method opted for their domains.

Possible suggestions would be either taking advantage of rewriting and simplifying, with tradeoff of speed [4] , or using random numeric testing, with tradeoff of accuracy [5] .

If you wonder why there is no generic algorithm for zero testing that can work with any symbolic entities, it’s because of the constant problem stating that zero testing is undecidable [6] , and not only the SymPy, but also other computer algebra systems [7] [8] would face the same fundamental issue.

However, discovery of any zero test failings can provide some good examples to improve SymPy, so if you have encountered one, you can report the issue to SymPy issue tracker [9] to get detailed help from the community.

Footnotes

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

# Advanced Expression Manipulation¶

In this section, we discuss some ways that we can perform advanced manipulation of expressions.

## Understanding Expression Trees¶

Before we can do this, we need to understand how expressions are represented
in SymPy. A mathematical expression is represented as a tree. Let us take
the expression \(x^2 + xy\), i.e., `x**2 + x*y`

. We can see what this
expression looks like internally by using `srepr`

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
```

```
>>> expr = x**2 + x*y
>>> srepr(expr)
"Add(Pow(Symbol('x'), Integer(2)), Mul(Symbol('x'), Symbol('y')))"
```

The easiest way to tear this apart is to look at a diagram of the expression tree:

First, let’s look at the leaves of this tree. Symbols are instances of the class Symbol. While we have been doing

```
>>> x = symbols('x')
```

we could have also done

```
>>> x = Symbol('x')
```

Either way, we get a Symbol with the name “x” [1]. For the number in the
expression, 2, we got `Integer(2)`

. `Integer`

is the SymPy class for
integers. It is similar to the Python built-in type `int`

, except that
`Integer`

plays nicely with other SymPy types.

When we write `x**2`

, this creates a `Pow`

object. `Pow`

is short for
“power”.

```
>>> srepr(x**2)
"Pow(Symbol('x'), Integer(2))"
```

We could have created the same object by calling `Pow(x, 2)`

```
>>> Pow(x, 2)
x**2
```

Note that in the `srepr`

output, we see `Integer(2)`

, the SymPy version of
integers, even though technically, we input `2`

, a Python int. In general,
whenever you combine a SymPy object with a non-SymPy object via some function
or operation, the non-SymPy object will be converted into a SymPy object. The
function that does this is `sympify`

[2].

```
>>> type(2)
<... 'int'>
>>> type(sympify(2))
<class 'sympy.core.numbers.Integer'>
```

We have seen that `x**2`

is represented as `Pow(x, 2)`

. What about
`x*y`

? As we might expect, this is the multiplication of `x`

and `y`

.
The SymPy class for multiplication is `Mul`

.

```
>>> srepr(x*y)
"Mul(Symbol('x'), Symbol('y'))"
```

Thus, we could have created the same object by writing `Mul(x, y)`

.

```
>>> Mul(x, y)
x*y
```

Now we get to our final expression, `x**2 + x*y`

. This is the addition of
our last two objects, `Pow(x, 2)`

, and `Mul(x, y)`

. The SymPy class for
addition is `Add`

, so, as you might expect, to create this object, we use
`Add(Pow(x, 2), Mul(x, y))`

.

```
>>> Add(Pow(x, 2), Mul(x, y))
x**2 + x*y
```

SymPy expression trees can have many branches, and can be quite deep or quite broad. Here is a more complicated example

```
>>> expr = sin(x*y)/2 - x**2 + 1/y
>>> srepr(expr)
"Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Rational(1, 2),
sin(Mul(Symbol('x'), Symbol('y')))), Pow(Symbol('y'), Integer(-1)))"
```

Here is a diagram

This expression reveals some interesting things about SymPy expression trees. Let’s go through them one by one.

Let’s first look at the term `x**2`

. As we expected, we see `Pow(x, 2)`

.
One level up, we see we have `Mul(-1, Pow(x, 2))`

. There is no subtraction
class in SymPy. `x - y`

is represented as `x + -y`

, or, more completely,
`x + -1*y`

, i.e., `Add(x, Mul(-1, y))`

.

```
>>> srepr(x - y)
"Add(Symbol('x'), Mul(Integer(-1), Symbol('y')))"
```

. We might expect to see something like `Div(1, y)`

,
but similar to subtraction, there is no class in SymPy for division. Rather,
division is represented by a power of -1. Hence, we have `Pow(y, -1)`

.
What if we had divided something other than 1 by `y`

, like `x/y`

? Let’s
see.

```
>>> expr = x/y
>>> srepr(expr)
"Mul(Symbol('x'), Pow(Symbol('y'), Integer(-1)))"
```

We see that `x/y`

is represented as `x*y**-1`

, i.e., ```
Mul(x, Pow(y,
-1))
```

.

Finally, let’s look at the `sin(x*y)/2`

term. Following the pattern of the
Mul(sin(x*y), Pow(Integer(2),
-1))
```

. But instead, we have `Mul(Rational(1, 2), sin(x*y))`

. Rational
numbers are always combined into a single term in a multiplication, so that
when we divide by 2, it is represented as multiplying by 1/2.

Finally, one last note. You may have noticed that the order we entered our
expression and the order that it came out from `srepr`

or in the graph were
different. You may have also noticed this phenomenon earlier in the
tutorial. For example

```
>>> 1 + x
x + 1
```

This because in SymPy, the arguments of the commutative operations `Add`

and
`Mul`

are stored in an arbitrary (but consistent!) order, which is
independent of the order inputted (if you’re worried about noncommutative
multiplication, don’t be. In SymPy, you can create noncommutative Symbols
using `Symbol('A', commutative=False)`

, and the order of multiplication for
noncommutative Symbols is kept the same as the input). Furthermore, as we
shall see in the next section, the printing order and the order in which
things are stored internally need not be the same either.

In general, an important thing to keep in mind when working with SymPy expression trees is this: the internal representation of an expression and the way it is printed need not be the same. The same is true for the input form. If some expression manipulation algorithm is not working in the way you expected it to, chances are, the internal representation of the object is different from what you thought it was.

## Recursing through an Expression Tree¶

Now that you know how expression trees work in SymPy, let’s look at how to dig
our way through an expression tree. Every object in SymPy has two very
important attributes, `func`

, and `args`

.

### func¶

`func`

is the head of the object. For example, `(x*y).func`

is `Mul`

.
Usually it is the same as the class of the object (though there are exceptions
to this rule).

Two notes about `func`

. First, the class of an object need not be the same
as the one used to create it. For example

```
>>> expr = Add(x, x)
>>> expr.func
<class 'sympy.core.mul.Mul'>
```

We created `Add(x, x)`

, so we might expect `expr.func`

to be `Add`

, but
instead we got `Mul`

. Why is that? Let’s take a closer look at `expr`

.

```
>>> expr
2*x
```

`Add(x, x)`

, i.e., `x + x`

, was automatically converted into ```
Mul(2,
x)
```

, i.e., `2*x`

, which is a `Mul`

. SymPy classes make heavy use of the
`__new__`

class constructor, which, unlike `__init__`

, allows a different
class to be returned from the constructor.

Second, some classes are special-cased, usually for efficiency reasons [3].

```
>>> Integer(2).func
<class 'sympy.core.numbers.Integer'>
>>> Integer(0).func
<class 'sympy.core.numbers.Zero'>
>>> Integer(-1).func
<class 'sympy.core.numbers.NegativeOne'>
```

For the most part, these issues will not bother us. The special classes
`Zero`

, `One`

, `NegativeOne`

, and so on are subclasses of `Integer`

,
so as long as you use `isinstance`

, it will not be an issue.

### args¶

`args`

are the top-level arguments of the object. `(x*y).args`

would be
`(x, y)`

. Let’s look at some examples

```
>>> expr = 3*y**2*x
>>> expr.func
<class 'sympy.core.mul.Mul'>
>>> expr.args
(3, x, y**2)
```

From this, we can see that `expr == Mul(3, y**2, x)`

. In fact, we can see
that we can completely reconstruct `expr`

from its `func`

and its
`args`

.

```
>>> expr.func(*expr.args)
3*x*y**2
>>> expr == expr.func(*expr.args)
True
```

Note that although we entered `3*y**2*x`

, the `args`

are `(3, x, y**2)`

.
In a `Mul`

, the Rational coefficient will come first in the `args`

, but
other than that, the order of everything else follows no special pattern. To
be sure, though, there is an order.

```
>>> expr = y**2*3*x
>>> expr.args
(3, x, y**2)
```

Mul’s `args`

are sorted, so that the same `Mul`

will have the same
`args`

. But the sorting is based on some criteria designed to make the
sorting unique and efficient that has no mathematical significance.

The `srepr`

form of our `expr`

is `Mul(3, x, Pow(y, 2))`

. What if we
want to get at the `args`

of `Pow(y, 2)`

. Notice that the `y**2`

is in
the third slot of `expr.args`

, i.e., `expr.args[2]`

.

```
>>> expr.args[2]
y**2
```

So to get the `args`

of this, we call `expr.args[2].args`

.

```
>>> expr.args[2].args
(y, 2)
```

Now what if we try to go deeper. What are the args of `y`

. Or `2`

.
Let’s see.

```
>>> y.args
()
>>> Integer(2).args
()
```

They both have empty `args`

. In SymPy, empty `args`

signal that we have
hit a leaf of the expression tree.

So there are two possibilities for a SymPy expression. Either it has empty
`args`

, in which case it is a leaf node in any expression tree, or it has
`args`

, in which case, it is a branch node of any expression tree. When it
has `args`

, it can be completely rebuilt from its `func`

and its `args`

.
This is expressed in the key invariant.

(Recall that in Python if `a`

is a tuple, then `f(*a)`

means to call `f`

with arguments from the elements of `a`

, e.g., `f(*(1, 2, 3))`

is the same
as `f(1, 2, 3)`

.)

This key invariant allows us to write simple algorithms that walk expression trees, change them, and rebuild them into new expressions.

### Walking the Tree¶

With this knowledge, let’s look at how we can recurse through an expression
tree. The nested nature of `args`

is a perfect fit for recursive functions.
The base case will be empty `args`

. Let’s write a simple function that goes
through an expression and prints all the `args`

at each level.

```
>>> def pre(expr):
... print(expr)
... for arg in expr.args:
... pre(arg)
```

See how nice it is that `()`

signals leaves in the expression tree. We
don’t even have to write a base case for our recursion; it is handled
automatically by the for loop.

Let’s test our function.

```
>>> expr = x*y + 1
>>> pre(expr)
x*y + 1
1
x*y
x
y
```

Can you guess why we called our function `pre`

? We just wrote a pre-order
traversal function for our expression tree. See if you can write a
post-order traversal function.

Such traversals are so common in SymPy that the generator functions
`preorder_traversal`

and `postorder_traversal`

are provided to make such
traversals easy. We could have also written our algorithm as

```
>>> for arg in preorder_traversal(expr):
... print(arg)
x*y + 1
1
x*y
x
y
```

## Prevent expression evaluation¶

There are generally two ways to prevent the evaluation, either pass an
`evaluate=False`

parameter while constructing the expression, or create
an evaluation stopper by wrapping the expression with `UnevaluatedExpr`

.

For example:

```
>>> from sympy import Add
>>> from sympy.abc import x, y, z
>>> x + x
2*x
>>> Add(x, x)
2*x
>>> Add(x, x, evaluate=False)
x + x
```

If you don’t remember the class corresponding to the expression you
want to build (operator overloading usually assumes `evaluate=True`

),
just use `sympify`

and pass a string:

```
>>> from sympy import sympify
>>> sympify("x + x", evaluate=False)
x + x
```

Note that `evaluate=False`

won’t prevent future evaluation in later
usages of the expression:

```
>>> expr = Add(x, x, evaluate=False)
>>> expr
x + x
>>> expr + x
3*x
```

That’s why the class `UnevaluatedExpr`

comes handy.
`UnevaluatedExpr`

is a method provided by SymPy which lets the user keep
an expression unevaluated. By *unevaluated* it is meant that the value
inside of it will not interact with the expressions outside of it to give
simplified outputs. For example:

```
>>> from sympy import UnevaluatedExpr
>>> expr = x + UnevaluatedExpr(x)
>>> expr
x + x
>>> x + expr
2*x + x
```

The \(x\) remaining alone is the \(x\) wrapped by `UnevaluatedExpr`

.
To release it:

```
>>> (x + expr).doit()
3*x
```

Other examples:

```
>>> from sympy import *
>>> from sympy.abc import x, y, z
>>> uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)
>>> uexpr
(5/7)*(3/4)
>>> x*UnevaluatedExpr(1/x)
x*1/x
```

A point to be noted is that `UnevaluatedExpr`

cannot prevent the
evaluation of an expression which is given as argument. For example:

```
>>> expr1 = UnevaluatedExpr(x + x)
>>> expr1
2*x
>>> expr2 = sympify('x + x', evaluate=False)
>>> expr2
x + x
```

Remember that `expr2`

will be evaluated if included into another
expression. Combine both of the methods to prevent both inside and outside
evaluations:

```
>>> UnevaluatedExpr(sympify("x + x", evaluate=False)) + y
y + (x + x)
```

`UnevaluatedExpr`

is supported by SymPy printers and can be used to print the
result in different output forms. For example

```
>>> from sympy import latex
>>> uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)
>>> print(latex(uexpr))
\frac{5}{7} \cdot \frac{3}{4}
```

In order to release the expression and get the evaluated LaTeX form,
just use `.doit()`

:

```
>>> print(latex(uexpr.doit()))
\frac{15}{28}
```

Footnotes

## Source: https://docs.sympy.org/latest/tutorials/intro-tutorial/next.html

# What’s Next¶

Congratulations on finishing the SymPy tutorial!

If you are a developer interested in using SymPy in your code, please visit the How-to Guides which discuss key developer tasks.

Intermediate SymPy users and developers might want to visit the Explanations section for common pitfalls and advanced topics.

The SymPy API Reference has a detailed description of the SymPy API.

If you are interested in contributing to SymPy, visit the contribution guides.

## Source: https://docs.sympy.org/latest/tutorials/physics/index.html

# Physics Tutorials¶

The Physics Tutorials aim to introduce SymPy to users who have not previously used its physics features. The functionalities presented here have many more options and capabilities than what is covered in the tutorials. Through insightful examples and exercises, the tutorials demonstrate how to incorporate various physics subpackages of SymPy, including but not limited to multibody dynamics, quantum mechanics, optics, and continuum mechanics, to model and simulate different physical systems and their behaviors.

Feedback on this tutorial, or on SymPy in general is always welcome. Just write to our mailing list.

**Content**

## Source: https://docs.sympy.org/latest/tutorials/physics/biomechanics/index.html

# Biomechanics Tutorials¶

These tutorials provide a comprehensive guide on using SymPy for biomechanical simulations and analysis. We cover various models, including a human arm moving a lever, forces produced by muscles, and tendons using Hill-type muscle models.

In these tutorials, you can expect:

Model description: Detailed explanation of each biomechanical model.

Variables and Kinematics: Definition of necessary variables and kinematics equations essential for modeling.

Modeling: Step-by-step process of constructing the biomechanical models.

Equations of Motion: Derivation and analysis of the equations of motion for the systems.

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/index.html

# Mechanics Tutorials¶

These tutorials are designed to showcase the functionality of the `sympy.physics.mechanics`

module through
detailed examples and step-by-step instructions. We demonstrate how to model various mechanical systems,
derive equations of motion, and solve dynamic problems using Kane’s and Lagrange’s method.
Each example includes clear explanations, mathematical formulations, and code to illustrate key concepts.

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/duffing-example.html

# Duffing Oscillator with a Pendulum¶

In this example we demonstrate the use of functionality provided in
`sympy.physics.mechanics`

for deriving the equations of motion for a system
consisting of a Duffing oscillator with a pendulum. This example is inspired by the
paper [P.Brzeskia2012] section 2.

The system will be modeled using Lagrange equations. \(M\) is mass of the Duffing oscillator, \(m\) is mass of the pendulum, \(l\) is length of the pendulum. \(k_1\) and \(k_2\) are linear and non-linear parts of spring stiffness, and \(c_1\) is a viscous damping coefficient of the Duffing oscillator.

```
>>> import sympy as sm
>>> import sympy.physics.mechanics as me
>>> me.init_vprinting()
```

## Define Variables¶

```
>>> M, m, l, k1, k2, c1, g, h, w, d, r = sm.symbols('M, m, l, k1, k2, c1, g, h, w, d, r')
>>> q1, q2 = me.dynamicsymbols('q1 q2')
>>> q1d = me.dynamicsymbols('q1', 1)
```

\(h\): Height of the Duffing oscillator

\(w\): Width of the Duffing oscillator

\(d\): Depth of the Duffing oscillator

\(r\): Radius of the massive bob of the pendulum

\(q_1\): Generalized coordinate representing the position of the Duffing oscillator

\(q_2\): Generalized coordinate representing the angle of the pendulum

## Define Kinematics¶

Define all the reference frames and points.

```
>>> N = me.ReferenceFrame('N')
>>> B = N.orientnew('B', 'axis', (q2, N.z))
```

The angular velocity of the pendulum in the reference frame is:

```
>>> B.ang_vel_in(N)
q2'(t) n_z
```

Locations and velocities of the Duffing Oscillator block and the pendulum are:

```
>>> O = me.Point('O')
>>> block_point = O.locatenew('block', q1 * N.y)
>>> pendulum_point = block_point.locatenew('pendulum', l * B.y)
```

O is a fixed point in the inertial reference frame.

```
>>> O.set_vel(N, 0)
>>> block_point.set_vel(N, q1d * N.y)
>>> pendulum_point.v2pt_theory(block_point, N, B)
q1'(t) n_y + -l*q2'(t) b_x
```

Define inertia and rigid bodies. Here, we assume a simple pendulum which consists of a bob of mass m hanging from a massless string of length l and fixed at a pivot point (Duffing Oscillator Block).

```
>>> I_block = M / 12 * me.inertia(N, h**2 + d**2, w**2 + d**2, w**2 + h**2)
>>> I_pendulum = 2*m*r**2/5*me.inertia(B, 1, 0, 1)
```

```
>>> block_body = me.RigidBody('block', block_point, N, M, (I_block, block_point))
>>> pendulum_body = me.RigidBody('pendulum', pendulum_point, B, m, (I_pendulum, pendulum_point))
```

## Define Forces¶

We calculate the forces acting on the system. In this example, we set the potential energy to zero in the Lagrangian, and include the conservative forces (gravity and the Duffing spring) in the loads.

```
>>> path = me.LinearPathway(O, block_point)
>>> spring = me.DuffingSpring(k1, k2, path, 0)
>>> damper = me.LinearDamper(c1, path)
```

```
>>> loads = spring.to_loads() + damper.to_loads()
```

```
>>> bodies = [block_body, pendulum_body]
```

```
>>> for body in bodies:
... loads.append(me.Force(body, body.mass * g * N.y))
```

```
>>> loads
/ _____ 3/2\ / _____ 3/2\
| / 2 / 2\ | | / 2 / 2\ |
\k1*\/ q1 + k2*\q1 / /*q1 \- k1*\/ q1 - k2*\q1 / /*q1
[(O, ------------------------------ n_y), (block, -------------------------------- n_y), (O, c1*q1'(t) n_y), (block, -c1*q1'(t) n_y), (block, M*g n_y), (pendulum, g*m n_y)]
_____ _____
/ 2 / 2
\/ q1 \/ q1
```

## Lagrange’s Method¶

With the problem setup, the Lagrangian can be calculated, and the equations of motion formed.

```
>>> L = me.Lagrangian(N, block_body, pendulum_body)
>>> L
2 2 2 / 2 2 2\
M*q1'(t) m*r *q2'(t) m*\l *q2'(t) - 2*l*sin(q2)*q1'(t)*q2'(t) + q1'(t) /
--------- + ------------ + ----------------------------------------------------
2 5 2
```

```
>>> LM = me.LagrangesMethod(L, [q1, q2], bodies=bodies, forcelist=loads, frame=N)
>>> sm.simplify(LM.form_lagranges_equations())
[ / 2 \ / 2\ ]
[-M*g + M*q1''(t) + c1*q1'(t) - g*m - m*\l*sin(q2)*q2''(t) + l*cos(q2)*q2'(t) - q1''(t)/ + \k1 + k2*q1 /*q1]
[ ]
[ / 2 2 \ ]
[ m*\5*g*l*sin(q2) + 5*l *q2''(t) - 5*l*sin(q2)*q1''(t) + 2*r *q2''(t)/ ]
[ --------------------------------------------------------------------- ]
[ 5 ]
```

Equations of motion in [P.Brzeskia2012]:

Equations of motion in this example:

The differences in the equations of motion are attributed to several factors: the gravitational force, a damping torque characterized by the damping coefficient \(c_2\), and a periodically varying excitation \(F_0 \cos(\nu t)\).

## References¶

P. Brzeskia, P. Perlikowskia, S. Yanchukb, T. Kapitaniaka, The dynamics of the pendulum suspended on the forced Duffing oscillator, Journal of Sound and Vibration, 2012, https://doi.org/10.48550/arXiv.1202.5937

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/rollingdisc_example.html

# A rolling disc¶

The disc is assumed to be infinitely thin, in contact with the ground at only 1 point, and it is rolling without slip on the ground. See the image below.

We model the rolling disc in three different ways, to show more of the functionality of this module.

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/rollingdisc_example_kane.html

# A rolling disc, with Kane’s method¶

Here the definition of the rolling disc’s kinematics is formed from the contact point up, removing the need to introduce generalized speeds. Only 3 configuration and three speed variables are need to describe this system, along with the disc’s mass and radius, and the local gravity (note that mass will drop out).

```
>>> from sympy import symbols, sin, cos, tan
>>> from sympy.physics.mechanics import *
>>> q1, q2, q3, u1, u2, u3 = dynamicsymbols('q1 q2 q3 u1 u2 u3')
>>> q1d, q2d, q3d, u1d, u2d, u3d = dynamicsymbols('q1 q2 q3 u1 u2 u3', 1)
>>> r, m, g = symbols('r m g')
>>> mechanics_printing(pretty_print=False)
```

The kinematics are formed by a series of simple rotations. Each simple rotation creates a new frame, and the next rotation is defined by the new frame’s basis vectors. This example uses a 3-1-2 series of rotations, or Z, X, Y series of rotations. Angular velocity for this is defined using the second frame’s basis (the lean frame); it is for this reason that we defined intermediate frames, rather than using a body-three orientation.

```
>>> N = ReferenceFrame('N')
>>> Y = N.orientnew('Y', 'Axis', [q1, N.z])
>>> L = Y.orientnew('L', 'Axis', [q2, Y.x])
>>> R = L.orientnew('R', 'Axis', [q3, L.y])
>>> w_R_N_qd = R.ang_vel_in(N)
>>> R.set_ang_vel(N, u1 * L.x + u2 * L.y + u3 * L.z)
```

This is the translational kinematics. We create a point with no velocity in N; this is the contact point between the disc and ground. Next we form the position vector from the contact point to the disc’s center of mass. Finally we form the velocity and acceleration of the disc.

```
>>> C = Point('C')
>>> C.set_vel(N, 0)
>>> Dmc = C.locatenew('Dmc', r * L.z)
>>> Dmc.v2pt_theory(C, N, R)
r*u2*L.x - r*u1*L.y
```

This is a simple way to form the inertia dyadic. The inertia of the disc does not change within the lean frame as the disc rolls; this will make for simpler equations in the end.

```
>>> I = inertia(L, m / 4 * r**2, m / 2 * r**2, m / 4 * r**2)
>>> mprint(I)
m*r**2/4*(L.x|L.x) + m*r**2/2*(L.y|L.y) + m*r**2/4*(L.z|L.z)
```

Kinematic differential equations; how the generalized coordinate time derivatives relate to generalized speeds.

```
>>> kd = [dot(R.ang_vel_in(N) - w_R_N_qd, uv) for uv in L]
```

Creation of the force list; it is the gravitational force at the center of mass of the disc. Then we create the disc by assigning a Point to the center of mass attribute, a ReferenceFrame to the frame attribute, and mass and inertia. Then we form the body list.

```
>>> ForceList = [(Dmc, - m * g * Y.z)]
>>> BodyD = RigidBody('BodyD', Dmc, R, m, (I, Dmc))
>>> BodyList = [BodyD]
```

Finally we form the equations of motion, using the same steps we did before. Specify inertial frame, supply generalized coordinates and speeds, supply kinematic differential equation dictionary, compute Fr from the force list and Fr* from the body list, compute the mass matrix and forcing terms, then solve for the u dots (time derivatives of the generalized speeds).

```
>>> KM = KanesMethod(N, q_ind=[q1, q2, q3], u_ind=[u1, u2, u3], kd_eqs=kd)
>>> (fr, frstar) = KM.kanes_equations(BodyList, ForceList)
>>> MM = KM.mass_matrix
>>> forcing = KM.forcing
>>> rhs = MM.inv() * forcing
>>> kdd = KM.kindiffdict()
>>> rhs = rhs.subs(kdd)
>>> rhs.simplify()
>>> mprint(rhs)
Matrix([
[(4*g*sin(q2) + 6*r*u2*u3 - r*u3**2*tan(q2))/(5*r)],
[ -2*u1*u3/3],
[ (-2*u2 + u3*tan(q2))*u1]])
```

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/rollingdisc_example_kane_constraints.html

# A rolling disc, with Kane’s method and constraint forces¶

We will now revisit the rolling disc example, except this time we are bringing the non-contributing (constraint) forces into evidence. See [Kane1985] for a more thorough explanation of this. Here, we will turn on the automatic simplification done when doing vector operations. It makes the outputs nicer for small problems, but can cause larger vector operations to hang.

```
>>> from sympy import symbols, sin, cos, tan
>>> from sympy.physics.mechanics import *
>>> mechanics_printing(pretty_print=False)
>>> q1, q2, q3, u1, u2, u3 = dynamicsymbols('q1 q2 q3 u1 u2 u3')
>>> q1d, q2d, q3d, u1d, u2d, u3d = dynamicsymbols('q1 q2 q3 u1 u2 u3', 1)
>>> r, m, g = symbols('r m g')
```

These two lines introduce the extra quantities needed to find the constraint forces.

```
>>> u4, u5, u6, f1, f2, f3 = dynamicsymbols('u4 u5 u6 f1 f2 f3')
```

Most of the main code is the same as before.

```
>>> N = ReferenceFrame('N')
>>> Y = N.orientnew('Y', 'Axis', [q1, N.z])
>>> L = Y.orientnew('L', 'Axis', [q2, Y.x])
>>> R = L.orientnew('R', 'Axis', [q3, L.y])
>>> w_R_N_qd = R.ang_vel_in(N)
>>> R.set_ang_vel(N, u1 * L.x + u2 * L.y + u3 * L.z)
```

The definition of rolling without slip necessitates that the velocity of the contact point is zero; as part of bringing the constraint forces into evidence, we have to introduce speeds at this point, which will by definition always be zero. They are normal to the ground, along the path which the disc is rolling, and along the ground in a perpendicular direction.

```
>>> C = Point('C')
>>> C.set_vel(N, u4 * L.x + u5 * cross(Y.z, L.x) + u6 * Y.z)
>>> Dmc = C.locatenew('Dmc', r * L.z)
>>> vel = Dmc.v2pt_theory(C, N, R)
>>> I = inertia(L, m / 4 * r**2, m / 2 * r**2, m / 4 * r**2)
>>> kd = [dot(R.ang_vel_in(N) - w_R_N_qd, uv) for uv in L]
```

Just as we previously introduced three speeds as part of this process, we also introduce three forces; they are in the same direction as the speeds, and represent the constraint forces in those directions.

```
>>> ForceList = [(Dmc, - m * g * Y.z), (C, f1 * L.x + f2 * cross(Y.z, L.x) + f3 * Y.z)]
>>> BodyD = RigidBody('BodyD', Dmc, R, m, (I, Dmc))
>>> BodyList = [BodyD]
>>> KM = KanesMethod(N, q_ind=[q1, q2, q3], u_ind=[u1, u2, u3], kd_eqs=kd,
... u_auxiliary=[u4, u5, u6])
>>> (fr, frstar) = KM.kanes_equations(BodyList, ForceList)
>>> MM = KM.mass_matrix
>>> forcing = KM.forcing
>>> rhs = MM.inv() * forcing
>>> kdd = KM.kindiffdict()
>>> rhs = rhs.subs(kdd)
>>> rhs.simplify()
>>> mprint(rhs)
Matrix([
[(4*g*sin(q2) + 6*r*u2*u3 - r*u3**2*tan(q2))/(5*r)],
[ -2*u1*u3/3],
[ (-2*u2 + u3*tan(q2))*u1]])
>>> from sympy import trigsimp, signsimp, collect, factor_terms
>>> def simplify_auxiliary_eqs(w):
... return signsimp(trigsimp(collect(collect(factor_terms(w), f2), m*r)))
>>> mprint(KM.auxiliary_eqs.applyfunc(simplify_auxiliary_eqs))
Matrix([
[ -m*r*(u1*u3 + u2') + f1],
[-m*r*u1**2*sin(q2) - m*r*u2*u3/cos(q2) + m*r*cos(q2)*u1' + f2],
[ -g*m + m*r*(u1**2*cos(q2) + sin(q2)*u1') + f3]])
```

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/rollingdisc_example_lagrange.html

# A rolling disc using Lagrange’s Method¶

Here the rolling disc is formed from the contact point up, removing the need to introduce generalized speeds. Only 3 configuration and 3 speed variables are needed to describe this system, along with the disc’s mass and radius, and the local gravity.

```
>>> from sympy import symbols, cos, sin
>>> from sympy.physics.mechanics import *
>>> mechanics_printing(pretty_print=False)
>>> q1, q2, q3 = dynamicsymbols('q1 q2 q3')
>>> q1d, q2d, q3d = dynamicsymbols('q1 q2 q3', 1)
>>> r, m, g = symbols('r m g')
```

The kinematics are formed by a series of simple rotations. Each simple rotation creates a new frame, and the next rotation is defined by the new frame’s basis vectors. This example uses a 3-1-2 series of rotations, or Z, X, Y series of rotations. Angular velocity for this is defined using the second frame’s basis (the lean frame).

```
>>> N = ReferenceFrame('N')
>>> Y = N.orientnew('Y', 'Axis', [q1, N.z])
>>> L = Y.orientnew('L', 'Axis', [q2, Y.x])
>>> R = L.orientnew('R', 'Axis', [q3, L.y])
```

This is the translational kinematics. We create a point with no velocity in N; this is the contact point between the disc and ground. Next we form the position vector from the contact point to the disc’s center of mass. Finally we form the velocity and acceleration of the disc.

```
>>> C = Point('C')
>>> C.set_vel(N, 0)
>>> Dmc = C.locatenew('Dmc', r * L.z)
>>> Dmc.v2pt_theory(C, N, R)
r*(sin(q2)*q1' + q3')*L.x - r*q2'*L.y
```

Forming the inertia dyadic.

```
>>> I = inertia(L, m / 4 * r**2, m / 2 * r**2, m / 4 * r**2)
>>> mprint(I)
m*r**2/4*(L.x|L.x) + m*r**2/2*(L.y|L.y) + m*r**2/4*(L.z|L.z)
>>> BodyD = RigidBody('BodyD', Dmc, R, m, (I, Dmc))
```

We then set the potential energy and determine the Lagrangian of the rolling disc.

```
>>> BodyD.potential_energy = - m * g * r * cos(q2)
>>> Lag = Lagrangian(N, BodyD)
```

Then the equations of motion are generated by initializing the
`LagrangesMethod`

object. Finally we solve for the generalized
accelerations(q double dots) with the `rhs`

method.

```
>>> q = [q1, q2, q3]
>>> l = LagrangesMethod(Lag, q)
>>> le = l.form_lagranges_equations()
>>> le.simplify(); le
Matrix([
[m*r**2*(6*sin(q2)*q3'' + 5*sin(2*q2)*q1'*q2' + 6*cos(q2)*q2'*q3' - 5*cos(2*q2)*q1''/2 + 7*q1''/2)/4],
[ m*r*(4*g*sin(q2) - 5*r*sin(2*q2)*q1'**2/2 - 6*r*cos(q2)*q1'*q3' + 5*r*q2'')/4],
[ 3*m*r**2*(sin(q2)*q1'' + cos(q2)*q1'*q2' + q3'')/2]])
>>> lrhs = l.rhs(); lrhs.simplify(); lrhs
Matrix([
[ q1'],
[ q2'],
[ q3'],
[ -2*(2*tan(q2)*q1' + 3*q3'/cos(q2))*q2'],
[-4*g*sin(q2)/(5*r) + sin(2*q2)*q1'**2/2 + 6*cos(q2)*q1'*q3'/5],
[ (-5*cos(q2)*q1' + 6*tan(q2)*q3' + 4*q1'/cos(q2))*q2']])
```

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/multi_degree_freedom_holonomic_system.html

# Multi Degree of Freedom Holonomic System¶

In this example we demonstrate the use of the functionality provided in
`sympy.physics.mechanics`

for deriving the equations of motion (EOM) of a
holonomic system that includes both particles and rigid bodies with contributing
forces and torques, some of which are specified forces and torques. The system
is shown below:

The system will be modeled using `System`

. First we need to create the
`dynamicsymbols()`

needed to describe the system as shown in the above
diagram. In this case, the generalized coordinates \(q_1\) represent lateral
distance of block from wall, \(q_2\) represents angle of the compound
pendulum from vertical, \(q_3\) represents angle of the simple pendulum
from the compound pendulum. The generalized speeds \(u_1\) represents
lateral speed of block, \(u_2\) represents lateral speed of compound
pendulum and \(u_3\) represents angular speed of C relative to B.

We also create some `symbols()`

to represent the length and mass of the
pendulum, as well as gravity and others.

```
>>> from sympy import zeros, symbols
>>> from sympy.physics.mechanics import *
>>> q1, q2, q3, u1, u2, u3 = dynamicsymbols('q1, q2, q3, u1, u2, u3')
>>> F, T = dynamicsymbols('F, T')
>>> l, k, c, g, kT = symbols('l, k, c, g, kT')
>>> ma, mb, mc, IBzz= symbols('ma, mb, mc, IBzz')
```

With all symbols defined, we can now define the bodies and initialize our
instance of `System`

.

```
>>> wall = RigidBody('N')
>>> block = Particle('A', mass=ma)
>>> compound_pend = RigidBody('B', mass=mb)
>>> compound_pend.central_inertia = inertia(compound_pend.frame, 0, 0, IBzz)
>>> simple_pend = Particle('C', mass=mc)
>>> system = System.from_newtonian(wall)
>>> system.add_bodies(block, compound_pend, simple_pend)
```

```
>>> block_frame = ReferenceFrame('A')
>>> block.masscenter.set_vel(block_frame, 0)
>>> slider = PrismaticJoint('J1', wall, block, coordinates=q1, speeds=u1,
... child_interframe=block_frame)
>>> rev1 = PinJoint('J2', block, compound_pend, coordinates=q2, speeds=u2,
... joint_axis=wall.z, child_point=l*2/3*compound_pend.y,
... parent_interframe=block_frame)
>>> simple_pend_frame = ReferenceFrame('C')
>>> simple_pend.masscenter.set_vel(simple_pend_frame, 0)
>>> rev2 = PinJoint('J3', compound_pend, simple_pend, coordinates=q3,
... speeds=u3, joint_axis=compound_pend.z,
... parent_point=-l/3*compound_pend.y,
... child_point=l*simple_pend_frame.y,
... child_interframe=simple_pend_frame)
>>> system.add_joints(slider, rev1, rev2)
```

Now we can apply loads (forces and torques) to the bodies, gravity acts on all bodies, a linear spring and damper act on block and wall, a rotational linear spring acts on C relative to B specified torque T acts on compound_pend and block, specified force F acts on block.

```
>>> system.apply_uniform_gravity(-g * wall.y)
>>> system.add_loads(Force(block, F * wall.x))
>>> spring_damper_path = LinearPathway(wall.masscenter, block.masscenter)
>>> system.add_actuators(
... LinearSpring(k, spring_damper_path),
... LinearDamper(c, spring_damper_path),
... TorqueActuator(T, wall.z, compound_pend, wall),
... TorqueActuator(kT * q3, wall.z, compound_pend, simple_pend_frame),
... )
```

With the system setup, we can now form the equations of motion with
`KanesMethod`

in the backend.

```
>>> system.form_eoms(explicit_kinematics=True)
Matrix([
[ -c*u1(t) - k*q1(t) + 2*l*mb*u2(t)**2*sin(q2(t))/3 - l*mc*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t)))*Derivative(u3(t), t) - l*mc*(-sin(q2(t))*cos(q3(t)) - sin(q3(t))*cos(q2(t)))*(u2(t) + u3(t))**2 + l*mc*u2(t)**2*sin(q2(t)) - (2*l*mb*cos(q2(t))/3 + mc*(l*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l*cos(q2(t))))*Derivative(u2(t), t) - (ma + mb + mc)*Derivative(u1(t), t) + F(t)],
[-2*g*l*mb*sin(q2(t))/3 - g*l*mc*(sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t))) - g*l*mc*sin(q2(t)) + l**2*mc*(u2(t) + u3(t))**2*sin(q3(t)) - l**2*mc*u2(t)**2*sin(q3(t)) - mc*(l**2*cos(q3(t)) + l**2)*Derivative(u3(t), t) - (2*l*mb*cos(q2(t))/3 + mc*(l*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l*cos(q2(t))))*Derivative(u1(t), t) - (IBzz + 4*l**2*mb/9 + mc*(2*l**2*cos(q3(t)) + 2*l**2))*Derivative(u2(t), t) + T(t)],
[ -g*l*mc*(sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t))) - kT*q3(t) - l**2*mc*u2(t)**2*sin(q3(t)) - l**2*mc*Derivative(u3(t), t) - l*mc*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t)))*Derivative(u1(t), t) - mc*(l**2*cos(q3(t)) + l**2)*Derivative(u2(t), t)]])
>>> system.mass_matrix_full
Matrix([
[1, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 0, ma + mb + mc, 2*l*mb*cos(q2(t))/3 + mc*(l*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l*cos(q2(t))), l*mc*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t)))],
[0, 0, 0, 2*l*mb*cos(q2(t))/3 + mc*(l*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l*cos(q2(t))), IBzz + 4*l**2*mb/9 + mc*(2*l**2*cos(q3(t)) + 2*l**2), mc*(l**2*cos(q3(t)) + l**2)],
[0, 0, 0, l*mc*(-sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))), mc*(l**2*cos(q3(t)) + l**2), l**2*mc]])
>>> system.forcing_full
Matrix([
[ u1(t)],
[ u2(t)],
[ u3(t)],
[ -c*u1(t) - k*q1(t) + 2*l*mb*u2(t)**2*sin(q2(t))/3 - l*mc*(-sin(q2(t))*cos(q3(t)) - sin(q3(t))*cos(q2(t)))*(u2(t) + u3(t))**2 + l*mc*u2(t)**2*sin(q2(t)) + F(t)],
[-2*g*l*mb*sin(q2(t))/3 - g*l*mc*(sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t))) - g*l*mc*sin(q2(t)) + l**2*mc*(u2(t) + u3(t))**2*sin(q3(t)) - l**2*mc*u2(t)**2*sin(q3(t)) + T(t)],
[ -g*l*mc*(sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t))) - kT*q3(t) - l**2*mc*u2(t)**2*sin(q3(t))]])
```

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/lin_pend_nonmin_example.html

# Nonminimal Coordinates Pendulum¶

In this example we demonstrate the use of the functionality provided in
`sympy.physics.mechanics`

for deriving the equations of motion (EOM) for a pendulum
with a nonminimal set of coordinates. As the pendulum is a one degree of
freedom system, it can be described using one coordinate and one speed (the
pendulum angle, and the angular velocity respectively). Choosing instead to
describe the system using the \(x\) and \(y\) coordinates of the mass results in
a need for constraints. The system is shown below:

The system will be modeled using both Kane’s and Lagrange’s methods, and the resulting EOM linearized. While this is a simple problem, it should illustrate the use of the linearization methods in the presence of constraints.

## Kane’s Method¶

First we need to create the `dynamicsymbols`

needed to describe the system as
shown in the above diagram. In this case, the generalized coordinates \(q_1\) and
\(q_2\) represent the mass \(x\) and \(y\) coordinates in the inertial \(N\) frame.
Likewise, the generalized speeds \(u_1\) and \(u_2\) represent the velocities in
these directions. We also create some `symbols`

to represent the length and
mass of the pendulum, as well as gravity and time.

```
>>> from sympy.physics.mechanics import *
>>> from sympy import symbols, atan, Matrix, solve
>>> # Create generalized coordinates and speeds for this non-minimal realization
>>> # q1, q2 = N.x and N.y coordinates of pendulum
>>> # u1, u2 = N.x and N.y velocities of pendulum
>>> q1, q2 = dynamicsymbols('q1:3')
>>> q1d, q2d = dynamicsymbols('q1:3', level=1)
>>> u1, u2 = dynamicsymbols('u1:3')
>>> u1d, u2d = dynamicsymbols('u1:3', level=1)
>>> L, m, g, t = symbols('L, m, g, t')
```

```
>>> # Compose world frame
>>> N = ReferenceFrame('N')
>>> pN = Point('N*')
>>> pN.set_vel(N, 0)
>>> # A.x is along the pendulum
>>> theta1 = atan(q2/q1)
>>> A = N.orientnew('A', 'axis', [theta1, N.z])
```

Locating the pendulum mass is then as easy as specifying its location with in
terms of its x and y coordinates in the world frame. A `Particle`

object is
then created to represent the mass at this location.

```
>>> # Locate the pendulum mass
>>> P = pN.locatenew('P1', q1*N.x + q2*N.y)
>>> pP = Particle('pP', P, m)
```

The kinematic differential equations (KDEs) relate the derivatives of the generalized coordinates to the generalized speeds. In this case the speeds are the derivatives, so these are simple. A dictionary is also created to map \(\dot{q}\) to \(u\):

```
>>> # Calculate the kinematic differential equations
>>> kde = Matrix([q1d - u1,
... q2d - u2])
>>> dq_dict = solve(kde, [q1d, q2d])
```

The velocity of the mass is then the time derivative of the position from the origin \(N^*\):

```
>>> # Set velocity of point P
>>> P.set_vel(N, P.pos_from(pN).dt(N).subs(dq_dict))
```

As this system has more coordinates than degrees of freedom, constraints are
needed. The configuration constraints relate the coordinates to each other. In
this case the constraint is that the distance from the origin to the mass is
always the length \(L\) (the pendulum doesn’t get longer). Likewise, the velocity
constraint is that the mass velocity in the `A.x`

direction is always 0 (no
radial velocity).

```
>>> f_c = Matrix([P.pos_from(pN).magnitude() - L])
>>> f_v = Matrix([P.vel(N).express(A).dot(A.x)])
>>> f_v.simplify()
```

The force on the system is just gravity, at point `P`

.

```
>>> # Input the force resultant at P
>>> R = m*g*N.x
```

With the problem setup, the equations of motion can be generated using the
`KanesMethod`

class. As there are constraints, dependent and independent
coordinates need to be provided to the class. In this case we’ll use \(q_2\) and
\(u_2\) as the independent coordinates and speeds:

```
>>> # Derive the equations of motion using the KanesMethod class.
>>> KM = KanesMethod(N, q_ind=[q2], u_ind=[u2], q_dependent=[q1],
... u_dependent=[u1], configuration_constraints=f_c,
... velocity_constraints=f_v, kd_eqs=kde)
>>> (fr, frstar) = KM.kanes_equations([pP],[(P, R)])
```

For linearization, operating points can be specified on the call, or be
substituted in afterwards. In this case we’ll provide them in the call,
supplied in a list. The `A_and_B=True`

kwarg indicates to solve invert the
\(M\) matrix and solve for just the explicit linearized \(A\) and \(B\) matrices. The
`simplify=True`

kwarg indicates to simplify inside the linearize call, and
return the presimplified matrices. The cost of doing this is small for simple
systems, but for larger systems this can be a costly operation, and should be
avoided.

```
>>> # Set the operating point to be straight down, and non-moving
>>> q_op = {q1: L, q2: 0}
>>> u_op = {u1: 0, u2: 0}
>>> ud_op = {u1d: 0, u2d: 0}
>>> # Perform the linearization
>>> A, B, inp_vec = KM.linearize(op_point=[q_op, u_op, ud_op], A_and_B=True,
... new_method=True, simplify=True)
>>> A
Matrix([
[ 0, 1],
[-g/L, 0]])
>>> B
Matrix(0, 0, [])
```

The resulting \(A\) matrix has dimensions 2 x 2, while the number of total states
is `len(q) + len(u) = 2 + 2 = 4`

. This is because for constrained systems the
resulting `A_and_B`

form has a partitioned state vector only containing
the independent coordinates and speeds. Written out mathematically, the system
linearized about this point would be written as:

## Lagrange’s Method¶

The derivation using Lagrange’s method is very similar to the approach using
Kane’s method described above. As before, we first create the
`dynamicsymbols`

needed to describe the system. In this case, the generalized
coordinates \(q_1\) and \(q_2\) represent the mass \(x\) and \(y\) coordinates in the
inertial \(N\) frame. This results in the time derivatives \(\dot{q_1}\) and
\(\dot{q_2}\) representing the velocities in these directions. We also create some
`symbols`

to represent the length and mass of the pendulum, as well as
gravity and time.

```
>>> from sympy.physics.mechanics import *
>>> from sympy import symbols, atan, Matrix
>>> q1, q2 = dynamicsymbols('q1:3')
>>> q1d, q2d = dynamicsymbols('q1:3', level=1)
>>> L, m, g, t = symbols('L, m, g, t')
```

```
>>> # Compose World Frame
>>> N = ReferenceFrame('N')
>>> pN = Point('N*')
>>> pN.set_vel(N, 0)
>>> # A.x is along the pendulum
>>> theta1 = atan(q2/q1)
>>> A = N.orientnew('A', 'axis', [theta1, N.z])
```

Locating the pendulum mass is then as easy as specifying its location with in
terms of its x and y coordinates in the world frame. A `Particle`

object is
then created to represent the mass at this location.

```
>>> # Create point P, the pendulum mass
>>> P = pN.locatenew('P1', q1*N.x + q2*N.y)
>>> P.set_vel(N, P.pos_from(pN).dt(N))
>>> pP = Particle('pP', P, m)
```

As this system has more coordinates than degrees of freedom, constraints are needed. In this case only a single holonomic constraints is needed: the distance from the origin to the mass is always the length \(L\) (the pendulum doesn’t get longer).

```
>>> # Holonomic Constraint Equations
>>> f_c = Matrix([q1**2 + q2**2 - L**2])
```

The force on the system is just gravity, at point `P`

.

```
>>> # Input the force resultant at P
>>> R = m*g*N.x
```

With the problem setup, the Lagrangian can be calculated, and the equations of
motion formed. Note that the call to `LagrangesMethod`

includes the
Lagrangian, the generalized coordinates, the constraints (specified by
`hol_coneqs`

or `nonhol_coneqs`

), the list of (body, force) pairs, and the
inertial frame. In contrast to the `KanesMethod`

initializer, independent and
dependent coordinates are not partitioned inside the `LagrangesMethod`

object. Such a partition is supplied later.

```
>>> # Calculate the lagrangian, and form the equations of motion
>>> Lag = Lagrangian(N, pP)
>>> LM = LagrangesMethod(Lag, [q1, q2], hol_coneqs=f_c, forcelist=[(P, R)], frame=N)
>>> lag_eqs = LM.form_lagranges_equations()
```

```
>>> # Compose operating point
>>> op_point = {q1: L, q2: 0, q1d: 0, q2d: 0, q1d.diff(t): 0, q2d.diff(t): 0}
```

As there are constraints in the formulation, there will be corresponding
Lagrange Multipliers. These may appear inside the linearized form as well, and
thus should also be included inside the operating point dictionary.
Fortunately, the `LagrangesMethod`

class provides an easy way of solving
for the multipliers at a given operating point using the `solve_multipliers`

method.

```
>>> # Solve for multiplier operating point
>>> lam_op = LM.solve_multipliers(op_point=op_point)
```

With this solution, linearization can be completed. Note that in contrast to
the `KanesMethod`

approach, the `LagrangesMethod.linearize`

method also
requires the partitioning of the generalized coordinates and their time
derivatives into independent and dependent vectors. This is the same as what
was passed into the `KanesMethod`

constructor above:

```
>>> op_point.update(lam_op)
>>> # Perform the Linearization
>>> A, B, inp_vec = LM.linearize([q2], [q2d], [q1], [q1d],
... op_point=op_point, A_and_B=True)
>>> A
Matrix([
[ 0, 1],
[-g/L, 0]])
>>> B
Matrix(0, 0, [])
```

The resulting \(A\) matrix has dimensions 2 x 2, while the number of total states
is `2*len(q) = 4`

. This is because for constrained systems the resulting
`A_and_B`

form has a partitioned state vector only containing the independent
coordinates and their derivatives. Written out mathematically, the system
linearized about this point would be written as:

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/four_bar_linkage_example.html

# A four bar linkage¶

The four bar linkage is a common example used in mechanics, which can be
formulated with only two holonomic constraints. This example will make use of
joints functionality provided in `sympy.physics.mechanics`

. In summary we
will use bodies and joints to define the open loop system. Next, we define the
configuration constraints to close the loop. `System`

will be used to
do the “book-keeping” of the entire system with `KanesMethod`

as the
backend.

First we need to create the `dynamicsymbols()`

needed to describe the
system as shown in the above diagram. In this case, the generalized coordinates
\(q_1\), \(q_2\) and \(q_3\) represent the angles between the links. Likewise, the
generalized speeds \(u_1\), \(u_2\) and \(u_3\) represent the angular velocities
between the links. We also create some `symbols()`

to represent the
lengths and density of the links.

```
>>> from sympy import Matrix, linear_eq_to_matrix, pi, simplify, symbols
>>> from sympy.physics.mechanics import *
>>> mechanics_printing(pretty_print=False)
>>> q1, q2, q3, u1, u2, u3 = dynamicsymbols('q1:4, u1:4')
>>> l1, l2, l3, l4, rho = symbols('l1:5, rho')
```

With all symbols defined, we can now define the bodies and initialize our
instance of `System`

.

```
>>> N = ReferenceFrame('N')
>>> mass_centers = [Point(f'mc{i}') for i in range(1, 5)]
>>> inertias = [Inertia.from_inertia_scalars(P, N, 0, 0, rho*l**3/12)
... for P, l in zip(mass_centers, (l1, l2, l3, l4))]
>>> link1 = RigidBody('Link1', frame=N, mass=rho*l1,
... masscenter=mass_centers[0], inertia=inertias[0])
>>> link2 = RigidBody('Link2', mass=rho*l2, masscenter=mass_centers[1],
... inertia=inertias[1])
>>> link3 = RigidBody('Link3', mass=rho*l3, masscenter=mass_centers[2],
... inertia=inertias[2])
>>> link4 = RigidBody('Link4', mass=rho*l4, masscenter=mass_centers[3],
... inertia=inertias[3])
>>> system = System.from_newtonian(link1)
```

```
>>> joint1 = PinJoint('J1', link1, link2, coordinates=q1, speeds=u1,
... parent_point=l1/2*link1.x,
... child_point=-l2/2*link2.x, joint_axis=link1.z)
>>> joint2 = PinJoint('J2', link2, link3, coordinates=q2, speeds=u2,
... parent_point=l2/2*link2.x,
... child_point=-l3/2*link3.x, joint_axis=link2.z)
>>> joint3 = PinJoint('J3', link3, link4, coordinates=q3, speeds=u3,
... parent_point=l3/2*link3.x,
... child_point=-l4/2*link4.x, joint_axis=link3.z)
>>> system.add_joints(joint1, joint2, joint3)
```

Now we can formulate the holonomic constraint that will close the kinematic loop.

```
>>> start_point = link1.masscenter.locatenew('start_point', -l1/2*link1.x)
>>> end_point = link4.masscenter.locatenew('end_point', l4/2*link4.x)
>>> loop = end_point.pos_from(start_point)
>>> system.add_holonomic_constraints(loop.dot(link1.x), loop.dot(link1.y))
```

Before generating the equations of motion we need to specify which generalized
coordinates and speeds are independent and which are dependent. After which we
can run `validate_system()`

to do some basic consistency checks.

```
>>> system.q_ind = [q1]
>>> system.u_ind = [u1]
>>> system.q_dep = [q2, q3]
>>> system.u_dep = [u2, u3]
>>> system.validate_system()
```

As we have the entire system ready, we can now form the equations of motion
using `KanesMethod`

as the backend.

```
>>> simplify(system.form_eoms())
Matrix([[l2*rho*(-2*l2**2*sin(q3)*u1' + 3*l2*l3*u1**2*sin(q2 + q3)*sin(q2) + 3*l2*l3*sin(q2)*cos(q2 + q3)*u1' - 3*l2*l3*sin(q3)*u1' + 3*l2*l4*u1**2*sin(q2 + q3)*sin(q2) + 3*l2*l4*sin(q2)*cos(q2 + q3)*u1' + 3*l3**2*u1**2*sin(q2)*sin(q3) + 6*l3**2*u1*u2*sin(q2)*sin(q3) + 3*l3**2*u2**2*sin(q2)*sin(q3) + 2*l3**2*sin(q2)*cos(q3)*u1' + 2*l3**2*sin(q2)*cos(q3)*u2' - l3**2*sin(q3)*cos(q2)*u1' - l3**2*sin(q3)*cos(q2)*u2' + 3*l3*l4*u1**2*sin(q2)*sin(q3) + 6*l3*l4*u1*u2*sin(q2)*sin(q3) + 3*l3*l4*u2**2*sin(q2)*sin(q3) + 3*l3*l4*sin(q2)*cos(q3)*u1' + 3*l3*l4*sin(q2)*cos(q3)*u2' + l4**2*sin(q2)*u1' + l4**2*sin(q2)*u2' + l4**2*sin(q2)*u3')/(6*sin(q3))]])
```

## Revealing noncontributing forces¶

To reveal the noncontributing forces at the closing joint, we must introduce auxiliary speeds in the x and y-direction at the endpoint.

```
>>> uaux1, uaux2 = dynamicsymbols('uaux1:3')
>>> end_point_aux = end_point.locatenew('end_point_aux', 0)
>>> end_point_aux.set_vel(N, end_point.vel(N) + uaux1*N.x + uaux2*N.y)
```

To ensure that speeds are included in the velocity constraints, we must manually overwrite the velocity constraints because those are by default specified as the time derivatives of the holonomic constraints.

```
>>> system.velocity_constraints = [
... end_point_aux.vel(N).dot(N.x), end_point_aux.vel(N).dot(N.y)]
```

When adding the noncontributing forces we need them to depend only on the auxiliary velocity and not the velocity that is eliminated by the constraints. This can be achieved by applying an equal and opposite force to the non-auxiliary endpoint.

```
>>> faux1, faux2 = dynamicsymbols('faux1:3')
>>> noncontributing_forces = [
... Force(end_point_aux, faux1*N.x + faux2*N.y),
... Force(end_point, -(faux1*N.x + faux2*N.y)),
... ]
```

Alternatively, we can specify a new point that already subtracts the velocity eliminated by the constraints.

```
>>> end_point_forces = end_point.locatenew('end_point_forces', 0)
>>> end_point_forces.set_vel(N, uaux1*N.x + uaux2*N.y)
>>> noncontributing_forces = [Force(end_point_forces, faux1*N.x + faux2*N.y)]
```

```
>>> system.add_loads(*noncontributing_forces)
>>> system.u_aux = [uaux1, uaux2]
```

To include gravity we can use `apply_uniform_gravity()`

before
validating the system and forming the equations of motion.

```
>>> g = symbols('g')
>>> system.apply_uniform_gravity(-g*N.y)
>>> system.validate_system()
>>> eoms = system.form_eoms()
```

With the equations of motion formed we can solve the auxiliary equations for the noncontributing forces and compute their values for a simple configuration.

```
>>> auxiliary_eqs = system.eom_method.auxiliary_eqs
>>> forces_eqs = Matrix.LUsolve(
... *linear_eq_to_matrix(auxiliary_eqs, [faux1, faux2]))
>>> subs = {
... l1: 2, l2: 1, l3: 2, l4: 1,
... rho: 5, g: 9.81,
... q1: pi/2, q2: pi/2, q3: pi/2,
... u1: 0, u2: 0, u3: 0, u1.diff(): 0, u2.diff(): 0, u3.diff(): 0,
... }
>>> forces_eqs.xreplace(subs)
Matrix([
[ 0],
[-98.1]])
```

## Source: https://docs.sympy.org/latest/tutorials/physics/mechanics/bicycle_example.html

# Linearized Carvallo-Whipple Bicycle Model¶

The bicycle is an interesting system in that it can be modeled with multiple
rigid bodies, non-holonomic constraints, and a holonomic constraint. The
linearized equations of motion of the Carvallo-Whipple bicycle model are
presented and benchmarked in [Meijaard2007]. This example will construct the
same linear equations of motion using `sympy.physics.mechanics`

.

```
>>> import sympy as sm
>>> import sympy.physics.mechanics as me
>>> me.mechanics_printing(pretty_print=False)
```

## Declaration of Coordinates & Speeds¶

The simple definition of \(\mathbf{u} = \dot{\mathbf{q}}\) is used in this model. The generalized speeds are:

yaw frame angular rate \(u_1\),

roll frame angular rate \(u_2\),

rear wheel frame angular rate (spinning motion) \(u_3\),

frame angular rate (pitching motion) \(u_4\),

steering frame angular rate \(u_5\), and

front wheel angular rate (spinning motion) \(u_6\).

Wheel positions are ignorable coordinates, so they are not introduced.

```
>>> q1, q2, q3, q4, q5 = me.dynamicsymbols('q1 q2 q3 q4 q5')
>>> q1d, q2d, q4d, q5d = me.dynamicsymbols('q1 q2 q4 q5', 1)
>>> u1, u2, u3, u4, u5, u6 = me.dynamicsymbols('u1 u2 u3 u4 u5 u6')
>>> u1d, u2d, u3d, u4d, u5d, u6d = me.dynamicsymbols('u1 u2 u3 u4 u5 u6', 1)
```

## Declaration of System’s Parameters¶

The constant parameters of the model are:

```
>>> WFrad, WRrad, htangle, forkoffset = sm.symbols('WFrad WRrad htangle forkoffset')
>>> forklength, framelength, forkcg1 = sm.symbols('forklength framelength forkcg1')
>>> forkcg3, framecg1, framecg3, Iwr11 = sm.symbols('forkcg3 framecg1 framecg3 Iwr11')
>>> Iwr22, Iwf11, Iwf22, Iframe11 = sm.symbols('Iwr22 Iwf11 Iwf22 Iframe11')
>>> Iframe22, Iframe33, Iframe31, Ifork11 = sm.symbols('Iframe22 Iframe33 Iframe31 Ifork11')
>>> Ifork22, Ifork33, Ifork31, g = sm.symbols('Ifork22 Ifork33 Ifork31 g')
>>> mframe, mfork, mwf, mwr = sm.symbols('mframe mfork mwf mwr')
```

## Kinematics of the Bicycle¶

### Set up reference frames for the system¶

`N`

- inertial`Y`

- yaw`R`

- roll`WR`

- rear wheel, rotation angle is ignorable coordinate so not oriented`Frame`

- bicycle frame`TempFrame`

- statically rotated frame for easier reference inertia definition`Fork`

- bicycle fork`TempFork`

- statically rotated frame for easier reference inertia definition`WF`

- front wheel, again posses an ignorable coordinate

```
>>> N = me.ReferenceFrame('N')
>>> Y = N.orientnew('Y', 'Axis', [q1, N.z])
>>> R = Y.orientnew('R', 'Axis', [q2, Y.x])
>>> Frame = R.orientnew('Frame', 'Axis', [q4 + htangle, R.y])
>>> WR = me.ReferenceFrame('WR')
>>> TempFrame = Frame.orientnew('TempFrame', 'Axis', [-htangle, Frame.y])
>>> Fork = Frame.orientnew('Fork', 'Axis', [q5, Frame.x])
>>> TempFork = Fork.orientnew('TempFork', 'Axis', [-htangle, Fork.y])
>>> WF = me.ReferenceFrame('WF')
```

### Define relevant points for the system¶

`WR_cont`

- rear wheel contact
`WR_mc`

- rear wheel’s center of mass
`Steer`

- frame/fork connection
`Frame_mc`

- frame’s center of mass
`Fork_mc`

- fork’s center of mass
`WF_mc`

- front wheel’s center of mass
`WF_cont`

- front wheel contact point

```
>>> WR_cont = me.Point('WR_cont')
>>> WR_mc = WR_cont.locatenew('WR_mc', WRrad*R.z)
>>> Steer = WR_mc.locatenew('Steer', framelength*Frame.z)
>>> Frame_mc = WR_mc.locatenew('Frame_mc', -framecg1*Frame.x + framecg3*Frame.z)
>>> Fork_mc = Steer.locatenew('Fork_mc', -forkcg1*Fork.x + forkcg3*Fork.z)
>>> WF_mc = Steer.locatenew('WF_mc', forklength*Fork.x + forkoffset*Fork.z)
>>> WF_cont = WF_mc.locatenew('WF_cont', WFrad*(me.dot(Fork.y, Y.z)*Fork.y - Y.z).normalize())
```

### Set the angular velocity of each frame¶

Angular accelerations end up being calculated automatically by differentiating the angular velocities when first needed.

`u1`

is yaw rate`u2`

is roll rate`u3`

is rear wheel rate`u4`

is frame pitch rate`u5`

is fork steer rate`u6`

is front wheel rate

```
>>> Y.set_ang_vel(N, u1 * Y.z)
>>> R.set_ang_vel(Y, u2 * R.x)
>>> WR.set_ang_vel(Frame, u3 * Frame.y)
>>> Frame.set_ang_vel(R, u4 * Frame.y)
>>> Fork.set_ang_vel(Frame, u5 * Fork.x)
>>> WF.set_ang_vel(Fork, u6 * Fork.y)
```

Form the velocities of the points, using the 2-point theorem. Accelerations again are calculated automatically when first needed.

```
>>> WR_cont.set_vel(N, 0)
>>> WR_mc.v2pt_theory(WR_cont, N, WR)
WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y
>>> Steer.v2pt_theory(WR_mc, N, Frame)
WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y + framelength*(u1*sin(q2) + u4)*Frame.x - framelength*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4))*Frame.y
>>> Frame_mc.v2pt_theory(WR_mc, N, Frame)
WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y + framecg3*(u1*sin(q2) + u4)*Frame.x + (-framecg1*(u1*cos(htangle + q4)*cos(q2) + u2*sin(htangle + q4)) - framecg3*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4)))*Frame.y + framecg1*(u1*sin(q2) + u4)*Frame.z
>>> Fork_mc.v2pt_theory(Steer, N, Fork)
WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y + framelength*(u1*sin(q2) + u4)*Frame.x - framelength*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4))*Frame.y + forkcg3*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5))*Fork.x + (-forkcg1*((-sin(q2)*sin(q5) + cos(htangle + q4)*cos(q2)*cos(q5))*u1 + u2*sin(htangle + q4)*cos(q5) - u4*sin(q5)) - forkcg3*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4) + u5))*Fork.y + forkcg1*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5))*Fork.z
>>> WF_mc.v2pt_theory(Steer, N, Fork)
WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y + framelength*(u1*sin(q2) + u4)*Frame.x - framelength*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4))*Frame.y + forkoffset*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5))*Fork.x + (forklength*((-sin(q2)*sin(q5) + cos(htangle + q4)*cos(q2)*cos(q5))*u1 + u2*sin(htangle + q4)*cos(q5) - u4*sin(q5)) - forkoffset*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4) + u5))*Fork.y - forklength*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5))*Fork.z
>>> WF_cont.v2pt_theory(WF_mc, N, WF)
- WFrad*((-sin(q2)*sin(q5)*cos(htangle + q4) + cos(q2)*cos(q5))*u6 + u4*cos(q2) + u5*sin(htangle + q4)*sin(q2))/sqrt((-sin(q2)*cos(q5) - sin(q5)*cos(htangle + q4)*cos(q2))*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2)) + 1)*Y.x + WFrad*(u2 + u5*cos(htangle + q4) + u6*sin(htangle + q4)*sin(q5))/sqrt((-sin(q2)*cos(q5) - sin(q5)*cos(htangle + q4)*cos(q2))*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2)) + 1)*Y.y + WRrad*(u1*sin(q2) + u3 + u4)*R.x - WRrad*u2*R.y + framelength*(u1*sin(q2) + u4)*Frame.x - framelength*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4))*Frame.y + (-WFrad*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*((-sin(q2)*sin(q5) + cos(htangle + q4)*cos(q2)*cos(q5))*u1 + u2*sin(htangle + q4)*cos(q5) - u4*sin(q5))/sqrt((-sin(q2)*cos(q5) - sin(q5)*cos(htangle + q4)*cos(q2))*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2)) + 1) + forkoffset*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5)))*Fork.x + (forklength*((-sin(q2)*sin(q5) + cos(htangle + q4)*cos(q2)*cos(q5))*u1 + u2*sin(htangle + q4)*cos(q5) - u4*sin(q5)) - forkoffset*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4) + u5))*Fork.y + (WFrad*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*(-u1*sin(htangle + q4)*cos(q2) + u2*cos(htangle + q4) + u5)/sqrt((-sin(q2)*cos(q5) - sin(q5)*cos(htangle + q4)*cos(q2))*(sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2)) + 1) - forklength*((sin(q2)*cos(q5) + sin(q5)*cos(htangle + q4)*cos(q2))*u1 + u2*sin(htangle + q4)*sin(q5) + u4*cos(q5)))*Fork.z
```

The kinematic differential equations are as follows. Each entry in this list is equal to zero.

```
>>> kd = [q1d - u1, q2d - u2, q4d - u4, q5d - u5]
```

### Setup the constraints¶

The nonholonomic constraints are the velocity of the front wheel contact point dotted into the X, Y, and Z directions; the yaw frame is used as it is “closer” to the front wheel (one fewer direction cosine matrix connecting them). These constraints force the velocity of the front wheel contact point to be zero in the inertial frame; the X and Y direction constraints enforce a “no-slip” condition, and the Z direction constraint forces the front wheel contact point to not move away from the ground frame, essentially replicating the holonomic constraint which does not allow the frame pitch to change in an invalid fashion.

```
>>> conlist_speed = [me.dot(WF_cont.vel(N), Y.x),
... me.dot(WF_cont.vel(N), Y.y),
... me.dot(WF_cont.vel(N), Y.z)]
```

The holonomic constraint is that the position from the rear wheel contact point to the front wheel contact point when dotted into the normal-to-ground plane direction must be zero; effectively that the front and rear wheel contact points are always touching the ground plane. This is actually not part of the dynamical differential equations, but is necessary for the linearization process.

```
>>> conlist_coord = [me.dot(WF_cont.pos_from(WR_cont), Y.z)]
```

## Inertia and Rigid Bodies¶

Sets the inertias of each body. Uses the inertia frame to construct the inertia dyadics. Wheel inertias are only defined by principal moments of inertia, and are in fact constant in the frame and fork reference frames; it is for this reason that the orientations of the wheels does not need to be defined. The frame and fork inertias are defined in the ‘Temp’ frames which are fixed to the appropriate body frames; this is to allow easier input of the reference values of the benchmark paper. Note that due to slightly different orientations, the products of inertia need to have their signs flipped; this is done later when entering the numerical value.

```
>>> Frame_I = (me.inertia(TempFrame, Iframe11, Iframe22, Iframe33, 0, 0,
... Iframe31), Frame_mc)
>>> Fork_I = (me.inertia(TempFork, Ifork11, Ifork22, Ifork33, 0, 0, Ifork31), Fork_mc)
>>> WR_I = (me.inertia(Frame, Iwr11, Iwr22, Iwr11), WR_mc)
>>> WF_I = (me.inertia(Fork, Iwf11, Iwf22, Iwf11), WF_mc)
```

Declaration of the `RigidBody`

containers.

```
>>> BodyFrame = me.RigidBody('BodyFrame', Frame_mc, Frame, mframe, Frame_I)
>>> BodyFork = me.RigidBody('BodyFork', Fork_mc, Fork, mfork, Fork_I)
>>> BodyWR = me.RigidBody('BodyWR', WR_mc, WR, mwr, WR_I)
>>> BodyWF = me.RigidBody('BodyWF', WF_mc, WF, mwf, WF_I)
>>> bodies = [BodyFrame, BodyFork, BodyWR, BodyWF]
```

## Gravitational Loads¶

The force list; each body has the appropriate gravitational force applied at its center of mass.

```
>>> forces = [(Frame_mc, -mframe * g * Y.z),
... (Fork_mc, -mfork * g * Y.z),
... (WF_mc, -mwf * g * Y.z),
... (WR_mc, -mwr * g * Y.z)]
...
```

## Nonlinear Equations of Motion¶

The `N`

frame is the inertial frame, coordinates are supplied in the order of
independent, dependent coordinates. The kinematic differential equations are
also entered here. Here the independent speeds are specified, followed by the
dependent speeds, along with the non-holonomic constraints. The dependent
coordinate is also provided, with the holonomic constraint. Again, this is only
comes into play in the linearization process, but is necessary for the
linearization to correctly work.

```
>>> kane = me.KanesMethod(
... N,
... q_ind=[q1, q2, q5],
... q_dependent=[q4],
... configuration_constraints=conlist_coord,
... u_ind=[u2, u3, u5],
... u_dependent=[u1, u4, u6],
... velocity_constraints=conlist_speed,
... kd_eqs=kd,
... constraint_solver='CRAMER')
>>> fr, frstar = kane.kanes_equations(bodies, loads=forces)
```

## Linearized Equations of Motion¶

This is the start of entering in the numerical values from the benchmark paper to validate the eigenvalues of the linearized equations from this model to the reference eigenvalues. Look at the aforementioned paper for more information. Some of these are intermediate values, used to transform values from the paper into the coordinate systems used in this model.

```
>>> PaperRadRear = 0.3
>>> PaperRadFront = 0.35
>>> HTA = sm.evalf.N(sm.pi/2 - sm.pi/10)
>>> TrailPaper = 0.08
>>> rake = sm.evalf.N(-(TrailPaper*sm.sin(HTA) - (PaperRadFront*sm.cos(HTA))))
>>> PaperWb = 1.02
>>> PaperFrameCgX = 0.3
>>> PaperFrameCgZ = 0.9
>>> PaperForkCgX = 0.9
>>> PaperForkCgZ = 0.7
>>> FrameLength = sm.evalf.N(PaperWb*sm.sin(HTA) - (rake -
... (PaperRadFront - PaperRadRear)*sm.cos(HTA)))
>>> FrameCGNorm = sm.evalf.N((PaperFrameCgZ - PaperRadRear -
... (PaperFrameCgX/sm.sin(HTA))*sm.cos(HTA))*sm.sin(HTA))
>>> FrameCGPar = sm.evalf.N((PaperFrameCgX / sm.sin(HTA) +
... (PaperFrameCgZ - PaperRadRear -
... PaperFrameCgX / sm.sin(HTA)*sm.cos(HTA))*sm.cos(HTA)))
>>> tempa = sm.evalf.N((PaperForkCgZ - PaperRadFront))
>>> tempb = sm.evalf.N((PaperWb-PaperForkCgX))
>>> tempc = sm.evalf.N(sm.sqrt(tempa**2 + tempb**2))
>>> PaperForkL = sm.evalf.N((PaperWb*sm.cos(HTA) -
... (PaperRadFront - PaperRadRear)*sm.sin(HTA)))
>>> ForkCGNorm = sm.evalf.N(rake + (tempc*sm.sin(sm.pi/2 -
... HTA - sm.acos(tempa/tempc))))
>>> ForkCGPar = sm.evalf.N(tempc*sm.cos((sm.pi/2 - HTA) -
... sm.acos(tempa/tempc)) - PaperForkL)
```

Here is the final assembly of the numerical values. The symbol ‘v’ is the
forward speed of the bicycle (a concept which only makes sense in the upright,
static equilibrium case?). These are in a dictionary which will later be
substituted in. Again the sign on the *product* of inertia values is flipped
here, due to different orientations of coordinate systems.

```
>>> v = sm.Symbol('v')
>>> val_dict = {
... WFrad: PaperRadFront,
... WRrad: PaperRadRear,
... htangle: HTA,
... forkoffset: rake,
... forklength: PaperForkL,
... framelength: FrameLength,
... forkcg1: ForkCGPar,
... forkcg3: ForkCGNorm,
... framecg1: FrameCGNorm,
... framecg3: FrameCGPar,
... Iwr11: 0.0603,
... Iwr22: 0.12,
... Iwf11: 0.1405,
... Iwf22: 0.28,
... Ifork11: 0.05892,
... Ifork22: 0.06,
... Ifork33: 0.00708,
... Ifork31: 0.00756,
... Iframe11: 9.2,
... Iframe22: 11,
... Iframe33: 2.8,
... Iframe31: -2.4,
... mfork: 4,
... mframe: 85,
... mwf: 3,
... mwr: 2,
... g: 9.81,
... }
...
```

Linearize the equations of motion about the equilibrium point:

```
>>> eq_point = {
... u1d: 0,
... u2d: 0,
... u3d: 0,
... u4d: 0,
... u5d: 0,
... u6d: 0,
... q1: 0,
... q2: 0,
... q4: 0,
... q5: 0,
... u1: 0,
... u2: 0,
... u3: v/PaperRadRear,
... u4: 0,
... u5: 0,
... u6: v/PaperRadFront,
... }
...
>>> Amat, _, _ = kane.linearize(A_and_B=True, op_point=eq_point, linear_solver='CRAMER')
>>> Amat = me.msubs(Amat, val_dict)
```

### Calculate the Eigenvalues¶

Finally, we construct an “A” matrix for the form \(\dot{\mathbf{x}} = \mathbf{A} \mathbf{x}\) (\(\mathbf{x}\) being the state vector, although in this case, the sizes are a little off). The following line extracts only the minimum entries required for eigenvalue analysis, which correspond to rows and columns for lean, steer, lean rate, and steer rate.

```
>>> A = Amat.extract([1, 2, 3, 5], [1, 2, 3, 5])
>>> A
Matrix([
[ 0, 0, 1, 0],
[ 0, 0, 0, 1],
[9.48977444677355, -0.891197738059089*v**2 - 0.571523173729245, -0.105522449805691*v, -0.330515398992311*v],
[11.7194768719633, 30.9087533932407 - 1.97171508499972*v**2, 3.67680523332152*v, -3.08486552743311*v]])
>>> print('v = 1')
v = 1
>>> print(A.subs(v, 1).eigenvals())
{-3.13423125066578 - 1.05503732448615e-65*I: 1, 3.52696170990069 - 0.807740275199311*I: 1, 3.52696170990069 + 0.807740275199311*I: 1, -7.11008014637441: 1}
>>> print('v = 2')
v = 2
>>> print(A.subs(v, 2).eigenvals())
{2.68234517512745 - 1.68066296590676*I: 1, 2.68234517512745 + 1.68066296590676*I: 1, -3.07158645641514: 1, -8.67387984831737: 1}
>>> print('v = 3')
v = 3
>>> print(A.subs(v, 3).eigenvals())
{1.70675605663973 - 2.31582447384324*I: 1, 1.70675605663973 + 2.31582447384324*I: 1, -2.63366137253665: 1, -10.3510146724592: 1}
>>> print('v = 4')
v = 4
>>> print(A.subs(v, 4).eigenvals())
{0.413253315211239 - 3.07910818603205*I: 1, 0.413253315211239 + 3.07910818603205*I: 1, -1.42944427361326 + 1.65070329233125e-64*I: 1, -12.1586142657644: 1}
>>> print('v = 5')
v = 5
>>> print(A.subs(v, 5).eigenvals())
{-0.775341882195845 - 4.46486771378823*I: 1, -0.322866429004087 + 3.32140410564766e-64*I: 1, -0.775341882195845 + 4.46486771378823*I: 1, -14.0783896927982: 1}
```

The eigenvalues shown above match those in Table 2 on pg. 1971 of [Meijaard2007]. This concludes the bicycle example.

## References¶

Meijaard, J. P., Papadopoulos, J. M., Ruina, A., & Schwab, A. L. (2007). Linearized dynamics equations for the balance and steer of a bicycle: A benchmark and review. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 463(2084), 1955–1982. https://doi.org/10.1098/rspa.2007.1857

## Source: https://docs.sympy.org/latest/tutorials/physics/continuum_mechanics/beam_problems.html

# Solving Beam Bending Problems using Singularity Functions¶

To make this document easier to read, enable pretty printing:

```
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> init_printing(use_unicode=True)
```

## Beam¶

A planar beam is a structural element that is capable of withstanding load through resistance to internal shear and bending. Beams are characterized by their length, constraints, cross-sectional second moment of area, and elastic modulus. In SymPy, 2D beam objects are constructed by specifying the following properties:

Length

Elastic Modulus

Second Moment of Area

Variable : A symbol representing the location along the beam’s length. By default, this is set to

`Symbol(x)`

.- Boundary Conditions
bc_slope : Boundary conditions for slope.

bc_deflection : Boundary conditions for deflection.

Load Distribution

Once the above are specified, the following methods are used to compute useful information about the loaded beam:

`solve_for_reaction_loads()`

`shear_force()`

`bending_moment()`

`slope()`

## Examples¶

Below are examples of a variety two dimensional beam bending problems.

### Example 1¶

A cantilever beam 9 meters in length has a distributed constant load of 8 kN/m applied downward from the fixed end over a 5 meter distance. A counterclockwise moment of 50 kN-m is applied 5 meters from the fixed end. Lastly, a downward point load of 12 kN is applied at the free end of the beam.

```
y
^
|
\\\\|
\\\\| 8 kN/m
\\\\|_________________
\\\\|| | | | | | | | | 12 kN
\\\\|V V V V V V V V V |
\\\\|________________|_______________V
\\\\| | |
\\\\o - - - - - - - -↺ 50 kN-m - - - | - - -> x
\\\\|________________|_______________|
\\\\| :
\\\\|----------------|---------------|
5.0 m 4.0 m
```

Note

The user is free to choose their own sign convention. In this case the downward forces and counterclockwise bending moment being positive.

The beam must be initialized with the length, modulus of elasticity, and the second moment of area. These quantities can be symbols or numbers.

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> E, I = symbols('E, I')
>>> b = Beam(9, E, I)
```

The three loads are applied to the beam using the `apply_load()`

method. This
method supports point forces, point moments, and polynomial distributed loads
of any order, i.e. \(c, cx, cx^2, cx^3, \ldots\).

The 12 kN point load is in the negative direction, at the location of 9 meters, and the polynomial order is specified as -1:

```
>>> b.apply_load(12, 9, -1)
```

The `load`

attribute can then be used to access the loading function in
singularity function form:

```
>>> b.load
-1
12⋅<x - 9>
```

Similarly, the positive moment can be applied with a polynomial order -2:

```
>>> b.apply_load(50, 5, -2)
```

The distributed load is of order 0 and spans x=0 to x=5:

```
>>> b.apply_load(8, 0, 0, end=5)
```

The fixed end imposes two boundary conditions: 1) no vertical deflection and 2) no rotation. These are specified by appending tuples of x values and the corresponding deflection or slope values:

```
>>> b.bc_deflection.append((0, 0))
>>> b.bc_slope.append((0, 0))
```

These boundary conditions introduce an unknown reaction force and moment which need to be applied to the beam to maintain static equilibrium:

```
>>> R, M = symbols('R, M')
>>> b.apply_load(R, 0, -1)
>>> b.apply_load(M, 0, -2)
>>> b.load
-2 -1 0 -2 0 -1
M⋅<x> + R⋅<x> + 8⋅<x> + 50⋅<x - 5> - 8⋅<x - 5> + 12⋅<x - 9>
```

These two variables can be solved for in terms of the applied loads and the final loading can be displayed:

```
>>> b.solve_for_reaction_loads(R, M)
>>> b.reaction_loads
{M: 158, R: -52}
>>> b.load
-2 -1 0 -2 0 -1
158⋅<x> - 52⋅<x> + 8⋅<x> + 50⋅<x - 5> - 8⋅<x - 5> + 12⋅<x - 9>
```

At this point, the beam is fully defined and the internal shear and bending moments are calculated:

```
>>> b.shear_force()
-1 0 1 -1 1 0
- 158⋅<x> + 52⋅<x> - 8⋅<x> - 50⋅<x - 5> + 8⋅<x - 5> - 12⋅<x - 9>
```

```
>>> b.bending_moment()
0 1 2 0 2 1
- 158⋅<x> + 52⋅<x> - 4⋅<x> - 50⋅<x - 5> + 4⋅<x - 5> - 12⋅<x - 9>
```

These can be visualized by calling the respective plot methods:

```
>>> b.plot_shear_force()
>>> b.plot_bending_moment()
```

The beam will deform under load and the slope and deflection can be determined with:

```
>>> b.slope()
⎛ 3 3 ⎞
⎜ 1 2 4⋅<x> 1 4⋅<x - 5> 2⎟
-⎜- 158⋅<x> + 26⋅<x> - ────── - 50⋅<x - 5> + ────────── - 6⋅<x - 9> ⎟
⎝ 3 3 ⎠
─────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 3 4 4 ⎞
⎜ 2 26⋅<x> <x> 2 <x - 5> 3⎟
-⎜- 79⋅<x> + ─────── - ──── - 25⋅<x - 5> + ──────── - 2⋅<x - 9> ⎟
⎝ 3 3 3 ⎠
────────────────────────────────────────────────────────────────────
E⋅I
```

The slope and deflection of the beam can be plotted so long as numbers are provided for the modulus and second moment:

```
>>> b.plot_slope(subs={E: 20E9, I: 3.25E-6})
>>> b.plot_deflection(subs={E: 20E9, I: 3.25E-6})
```

All of the plots can be shown in one figure with:

```
>>> b.plot_loading_results(subs={E: 20E9, I: 3.25E-6})
```

### Example 2¶

There is a beam of length 30 meters. A moment of magnitude 120 Nm is applied in the counter-clockwise direction at the end of the beam. A point load of magnitude 8 N is applied from the top of the beam at the starting point. There are two simple supports below the beam. One at the end and another one at a distance of 10 meters from the start. The deflection is restricted at both the supports.

```
|| 8 N ↺ 120 Nm
\/______________________________________________|
|_______________________________________________|
/\ /\
|------------|---------------------------------|
10 m 20 m
```

Note

Using the sign convention of downward forces and counterclockwise moment being positive.

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I = symbols('E, I')
>>> R1, R2 = symbols('R1, R2')
>>> b = Beam(30, E, I)
>>> b.apply_load(8, 0, -1)
>>> b.apply_load(R1, 10, -1)
>>> b.apply_load(R2, 30, -1)
>>> b.apply_load(120, 30, -2)
>>> b.bc_deflection.append((10, 0))
>>> b.bc_deflection.append((30, 0))
>>> b.solve_for_reaction_loads(R1, R2)
>>> b.reaction_loads
{R₁: -18, R₂: 10}
>>> b.load
-1 -1 -2 -1
8⋅<x> - 18⋅<x - 10> + 120⋅<x - 30> + 10⋅<x - 30>
>>> b.shear_force()
0 0 -1 0
- 8⋅<x> + 18⋅<x - 10> - 120⋅<x - 30> - 10⋅<x - 30>
>>> b.bending_moment()
1 1 0 1
- 8⋅<x> + 18⋅<x - 10> - 120⋅<x - 30> - 10⋅<x - 30>
>>> b.slope()
2 2 1 2 1600
4⋅<x> - 9⋅<x - 10> + 120⋅<x - 30> + 5⋅<x - 30> - ────
3
─────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
3 3
1600⋅x 4⋅<x> 3 2 5⋅<x - 30>
- ────── + ────── - 3⋅<x - 10> + 60⋅<x - 30> + ─────────── + 4000
3 3 3
───────────────────────────────────────────────────────────────────
E⋅I
```

### Example 3¶

A beam of length 6 meters is having a roller support at the start and a hinged support at the end. A counterclockwise moment of 1.5 kN-m is applied at the mid of the beam. A constant distributed load of 3 kN/m and a ramp load of 1 kN/m/m is applied from the mid till the end of the beam.

```
ramp load = 1 KN/m/m
constant load = 3 KN/m
|------------------------|
↺ 1.5 KN-m
______________________|________________________
|_______________________________________________|
o | /\
|----------------------|-----------------------|
3.0 m 3.0 m
```

Note

Using the sign convention of downward forces and counterclockwise moment being positive.

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols, plot, S
>>> E, I = symbols('E, I')
>>> R1, R2 = symbols('R1, R2')
>>> b = Beam(6, E, I)
>>> b.apply_load(R1, 0, -1)
>>> b.apply_load(-S(3)/2, 3, -2)
>>> b.apply_load(3, 3, 0)
>>> b.apply_load(1, 3, 1)
>>> b.apply_load(R2, 6, -1)
>>> b.bc_deflection.append((0, 0))
>>> b.bc_deflection.append((6, 0))
>>> b.solve_for_reaction_loads(R1, R2)
>>> b.reaction_loads
{R₁: -11/4, R₂: -43/4}
```

```
>>> b.load
-1 -2 -1
11⋅<x> 3⋅<x - 3> 0 1 43⋅<x - 6>
- ──────── - ─────────── + 3⋅<x - 3> + <x - 3> - ────────────
4 2 4
```

```
>>> plot(b.load)
```

```
>>> b.shear_force()
0 -1 2 0
11⋅<x> 3⋅<x - 3> 1 <x - 3> 43⋅<x - 6>
─────── + ─────────── - 3⋅<x - 3> - ──────── + ───────────
4 2 2 4
```

```
>>> b.bending_moment()
1 0 2 3 1
11⋅<x> 3⋅<x - 3> 3⋅<x - 3> <x - 3> 43⋅<x - 6>
─────── + ────────── - ────────── - ──────── + ───────────
4 2 2 6 4
```

```
>>> b.slope()
2 1 3 4 2
11⋅<x> 3⋅<x - 3> <x - 3> <x - 3> 43⋅<x - 6> 78
- ─────── - ────────── + ──────── + ──────── - ─────────── + ──
8 2 2 24 8 5
───────────────────────────────────────────────────────────────
E⋅I
```

```
>>> b.deflection()
3 2 4 5 3
78⋅x 11⋅<x> 3⋅<x - 3> <x - 3> <x - 3> 43⋅<x - 6>
──── - ─────── - ────────── + ──────── + ──────── - ───────────
5 24 4 8 120 24
───────────────────────────────────────────────────────────────
E⋅I
```

### Example 4¶

An overhanging beam of length 8 meters is pinned at 1 meter from starting point and supported by a roller 1 meter before the other end. It is subjected to a distributed constant load of 10 KN/m from the starting point till 2 meters away from it. Two point loads of 20KN and 8KN are applied at 5 meters and 7.5 meters away from the starting point respectively.

```
---> x
|
v y
10 KN/m
_____________ 20 KN 8 KN
| | | | | | | | |
V V V V V V V V V
_______________________________________________
|_______________________________________________|
/\ O
|-----|------|-----------------|----------|--|--|
1m 1m 3m 2m .5m .5m
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E,I,M,V = symbols('E I M V')
>>> b = Beam(8, E, I)
>>> E,I,R1,R2 = symbols('E I R1 R2')
>>> b.apply_load(R1, 1, -1)
>>> b.apply_load(R2, 7, -1)
>>> b.apply_load(10, 0, 0, end=2)
>>> b.apply_load(20, 5, -1)
>>> b.apply_load(8, 7.5, -1)
>>> b.solve_for_reaction_loads(R1, R2)
>>> b.reaction_loads
{R₁: -26, R₂: -22}
>>> b.load
0 -1 0 -1 -1 -1
10⋅<x> - 26⋅<x - 1> - 10⋅<x - 2> + 20⋅<x - 5> - 22⋅<x - 7> + 8⋅<x - 7.5>
>>> b.shear_force()
1 0 1 0 0 0
- 10⋅<x> + 26⋅<x - 1> + 10⋅<x - 2> - 20⋅<x - 5> + 22⋅<x - 7> - 8⋅<x - 7.5>
>>> b.bending_moment()
2 1 2 1 1 1
- 5⋅<x> + 26⋅<x - 1> + 5⋅<x - 2> - 20⋅<x - 5> + 22⋅<x - 7> - 8⋅<x - 7.5>
>>> b.bc_deflection = [(1, 0), (7, 0)]
>>> b.slope()
3 3
5⋅<x> 2 5⋅<x - 2> 2 2 2 679
────── - 13⋅<x - 1> - ────────── + 10⋅<x - 5> - 11⋅<x - 7> + 4⋅<x - 7.5> + ───
3 3 24
──────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
4 3 4 3 3 3
679⋅x 5⋅<x> 13⋅<x - 1> 5⋅<x - 2> 10⋅<x - 5> 11⋅<x - 7> 4⋅<x - 7.5> 689
───── + ────── - ─────────── - ────────── + ─────────── - ─────────── + ──────────── - ───
24 12 3 12 3 3 3 24
──────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

### Example 5¶

A cantilever beam of length 6 meters is under downward distributed constant load with magnitude of 4.0 KN/m from starting point till 2 meters away from it. A ramp load of 1 kN/m/m applied from the mid till the end of the beam. A point load of 12KN is also applied in same direction 4 meters away from start.

```
---> x .
| . |
v y 12 KN . | |
| . | | |
V . | | | |
\\\\| 4 KN/m . | | | | |
\\\\|___________ . 1 KN/m/m| |
\\\\|| | | | | | . V V V V V V V
\\\\|V V V V V V |---------------|
\\\\|________________________________
\\\\|________________________________|
\\\\| : : :
\\\\|----------|-----|----|----------|
2.0 m 1m 1m 2.0 m
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E,I,M,V = symbols('E I M V')
>>> b = Beam(6, E, I)
>>> b.apply_load(V, 0, -1)
>>> b.apply_load(M, 0, -2)
>>> b.apply_load(4, 0, 0, end=2)
>>> b.apply_load(12, 4, -1)
>>> b.apply_load(1, 3, 1, end=6)
>>> b.solve_for_reaction_loads(V, M)
>>> b.reaction_loads
{M: 157/2, V: -49/2}
>>> b.load
-2 -1
157⋅<x> 49⋅<x> 0 0 1 -1 0 1
───────── - ──────── + 4⋅<x> - 4⋅<x - 2> + <x - 3> + 12⋅<x - 4> - 3⋅<x - 6> - <x - 6>
2 2
>>> b.shear_force()
-1 0 2 2
157⋅<x> 49⋅<x> 1 1 <x - 3> 0 1 <x - 6>
- ───────── + ─────── - 4⋅<x> + 4⋅<x - 2> - ──────── - 12⋅<x - 4> + 3⋅<x - 6> + ────────
2 2 2 2
>>> b.bending_moment()
0 1 3 2 3
157⋅<x> 49⋅<x> 2 2 <x - 3> 1 3⋅<x - 6> <x - 6>
- ──────── + ─────── - 2⋅<x> + 2⋅<x - 2> - ──────── - 12⋅<x - 4> + ────────── + ────────
2 2 6 2 6
>>> b.bc_deflection = [(0, 0)]
>>> b.bc_slope = [(0, 0)]
>>> b.slope()
⎛ 1 2 3 3 4 3 4⎞
⎜ 157⋅<x> 49⋅<x> 2⋅<x> 2⋅<x - 2> <x - 3> 2 <x - 6> <x - 6> ⎟
-⎜- ──────── + ─────── - ────── + ────────── - ──────── - 6⋅<x - 4> + ──────── + ────────⎟
⎝ 2 4 3 3 24 2 24 ⎠
────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 2 3 4 4 5 4 5⎞
⎜ 157⋅<x> 49⋅<x> <x> <x - 2> <x - 3> 3 <x - 6> <x - 6> ⎟
-⎜- ──────── + ─────── - ──── + ──────── - ──────── - 2⋅<x - 4> + ──────── + ────────⎟
⎝ 4 12 6 6 120 8 120 ⎠
────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

### Example 6¶

An overhanging beam of length 11 meters is subjected to a distributed constant load of 2 KN/m from 2 meters away from the starting point till 6 meters away from it. It is pinned at the starting point and is resting over a roller 8 meters away from that end. Also a counterclockwise moment of 5 KN-m is applied at the overhanging end.

```
2 KN/m ---> x
_________________ |
| | | | | | | | | v y
V V V V V V V V V ↺ 5 KN-m
____________________________________________________|
O____________________________________________________|
/ \ /\
|--------|----------------|----------|---------------|
2m 4m 2m 3m
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> R1, R2 = symbols('R1, R2')
>>> E, I = symbols('E, I')
>>> b = Beam(11, E, I)
>>> b.apply_load(R1, 0, -1)
>>> b.apply_load(2, 2, 0, end=6)
>>> b.apply_load(R2, 8, -1)
>>> b.apply_load(5, 11, -2)
>>> b.solve_for_reaction_loads(R1, R2)
>>> b.reaction_loads
{R₁: -37/8, R₂: -27/8}
>>> b.load
-1 -1
37⋅<x> 0 0 27⋅<x - 8> -2
- ──────── + 2⋅<x - 2> - 2⋅<x - 6> - ──────────── + 5⋅<x - 11>
8 8
>>> b.shear_force()
0 0
37⋅<x> 1 1 27⋅<x - 8> -1
─────── - 2⋅<x - 2> + 2⋅<x - 6> + ─────────── - 5⋅<x - 11>
8 8
>>> b.bending_moment()
1 1
37⋅<x> 2 2 27⋅<x - 8> 0
─────── - <x - 2> + <x - 6> + ─────────── - 5⋅<x - 11>
8 8
>>> b.bc_deflection = [(0, 0), (8, 0)]
>>> b.slope()
2 3 3 2
37⋅<x> <x - 2> <x - 6> 27⋅<x - 8> 1
- ─────── + ──────── - ──────── - ─────────── + 5⋅<x - 11> + 36
16 3 3 16
────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
3 4 4 3 2
37⋅<x> <x - 2> <x - 6> 9⋅<x - 8> 5⋅<x - 11>
36⋅x - ─────── + ──────── - ──────── - ────────── + ───────────
48 12 12 16 2
───────────────────────────────────────────────────────────────
E⋅I
```

### Example 7¶

There is a beam of length `l`

, fixed at both ends. A concentrated point load
of magnitude `F`

is applied in downward direction at mid-point of the
beam.

```
^ y
|
---> x
\\\\| F |\\\\
\\\\| | |\\\\
\\\\| V |\\\\
\\\\|_____________________________________|\\\\
\\\\|_____________________________________|\\\\
\\\\| : |\\\\
\\\\| : |\\\\
\\\\|------------------|------------------|\\\\
l/2 l/2
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I, F = symbols('E I F')
>>> l = symbols('l', positive=True)
>>> b = Beam(l, E, I)
>>> R1,R2 = symbols('R1 R2')
>>> M1, M2 = symbols('M1, M2')
>>> b.apply_load(R1, 0, -1)
>>> b.apply_load(M1, 0, -2)
>>> b.apply_load(R2, l, -1)
>>> b.apply_load(M2, l, -2)
>>> b.apply_load(-F, l/2, -1)
>>> b.bc_deflection = [(0, 0),(l, 0)]
>>> b.bc_slope = [(0, 0),(l, 0)]
>>> b.solve_for_reaction_loads(R1, R2, M1, M2)
>>> b.reaction_loads
⎧ -F⋅l F⋅l F F⎫
⎨M₁: ─────, M₂: ───, R₁: ─, R₂: ─⎬
⎩ 8 8 2 2⎭
>>> b.load
-2 -2 -1 -1 -1
F⋅l⋅<x> F⋅l⋅<-l + x> F⋅<x> l F⋅<-l + x>
- ───────── + ────────────── + ─────── - F⋅<- ─ + x> + ────────────
8 8 2 2 2
>>> b.shear_force()
-1 -1 0 0 0
F⋅l⋅<x> F⋅l⋅<-l + x> F⋅<x> l F⋅<-l + x>
───────── - ────────────── - ────── + F⋅<- ─ + x> - ───────────
8 8 2 2 2
>>> b.bending_moment()
0 0 1 1 1
F⋅l⋅<x> F⋅l⋅<-l + x> F⋅<x> l F⋅<-l + x>
──────── - ───────────── - ────── + F⋅<- ─ + x> - ───────────
8 8 2 2 2
>>> b.slope()
⎛ 2 ⎞
⎜ l ⎟
⎜ 1 1 2 F⋅<- ─ + x> 2⎟
⎜F⋅l⋅<x> F⋅l⋅<-l + x> F⋅<x> 2 F⋅<-l + x> ⎟
-⎜──────── - ───────────── - ────── + ──────────── - ───────────⎟
⎝ 8 8 4 2 4 ⎠
──────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 3 ⎞
⎜ l ⎟
⎜ 2 2 3 F⋅<- ─ + x> 3⎟
⎜F⋅l⋅<x> F⋅l⋅<-l + x> F⋅<x> 2 F⋅<-l + x> ⎟
-⎜──────── - ───────────── - ────── + ──────────── - ───────────⎟
⎝ 16 16 12 6 12 ⎠
──────────────────────────────────────────────────────────────────
E⋅I
```

### Example 8¶

There is a beam of length `4*l`

, having a hinge connector at the middle. It
is having a fixed support at the start and also has two rollers at a distance
of `l`

and `4*l`

from the starting point. A concentrated point load `P`

is also
applied at a distance of `3*l`

from the starting point.

```
---> x
\\\\| P |
\\\\| | v y
\\\\| V
\\\\|_____________________ _______________________
\\\\|_____________________O_______________________|
\\\\| /\ : /\
\\\\| oooo : oooo
\\\\|----------|-----------|----------|-----------|
l l l l
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I = symbols('E I')
>>> l = symbols('l', positive=True)
>>> R1, M1, R2, R3, P = symbols('R1 M1 R2 R3 P')
>>> b1 = Beam(2*l, E, I)
>>> b2 = Beam(2*l, E, I)
>>> b = b1.join(b2, "hinge")
>>> b.apply_load(M1, 0, -2)
>>> b.apply_load(R1, 0, -1)
>>> b.apply_load(R2, l, -1)
>>> b.apply_load(R3, 4*l, -1)
>>> b.apply_load(P, 3*l, -1)
>>> b.bc_slope = [(0, 0)]
>>> b.bc_deflection = [(0, 0), (l, 0), (4*l, 0)]
>>> b.solve_for_reaction_loads(M1, R1, R2, R3)
>>> b.reaction_loads
⎧ -P⋅l 3⋅P -5⋅P -P ⎫
⎨M₁: ─────, R₁: ───, R₂: ─────, R₃: ───⎬
⎩ 4 4 4 2 ⎭
>>> b.load
2 -3 -2 -1 -1 -1
13⋅P⋅l ⋅<-2⋅l + x> P⋅l⋅<x> 3⋅P⋅<x> 5⋅P⋅<-l + x> -1 P⋅<-4⋅l + x>
- ──────────────────── - ───────── + ───────── - ────────────── + P⋅<-3⋅l + x> - ──────────────
48 4 4 4 2
>>> b.shear_force()
2 -2 -1 0 0 0
13⋅P⋅l ⋅<-2⋅l + x> P⋅l⋅<x> 3⋅P⋅<x> 5⋅P⋅<-l + x> 0 P⋅<-4⋅l + x>
──────────────────── + ───────── - ──────── + ───────────── - P⋅<-3⋅l + x> + ─────────────
48 4 4 4 2
>>> b.bending_moment()
2 -1 0 1 1 1
13⋅P⋅l ⋅<-2⋅l + x> P⋅l⋅<x> 3⋅P⋅<x> 5⋅P⋅<-l + x> 1 P⋅<-4⋅l + x>
──────────────────── + ──────── - ──────── + ───────────── - P⋅<-3⋅l + x> + ─────────────
48 4 4 4 2
>>> b.slope()
⎛ 2 0 1 2 2 2 2⎞
⎜13⋅P⋅l ⋅<-2⋅l + x> P⋅l⋅<x> 3⋅P⋅<x> 5⋅P⋅<-l + x> P⋅<-3⋅l + x> P⋅<-4⋅l + x> ⎟
-⎜─────────────────── + ──────── - ──────── + ───────────── - ───────────── + ─────────────⎟
⎝ 48 4 8 8 2 4 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 2 1 2 3 3 3 3⎞
⎜13⋅P⋅l ⋅<-2⋅l + x> P⋅l⋅<x> P⋅<x> 5⋅P⋅<-l + x> P⋅<-3⋅l + x> P⋅<-4⋅l + x> ⎟
-⎜─────────────────── + ──────── - ────── + ───────────── - ───────────── + ─────────────⎟
⎝ 48 8 8 24 6 12 ⎠
───────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

### Example 9¶

There is a cantilever beam of length 4 meters. For first 2 meters
its moment of inertia is `1.5*I`

and `I`

for the rest.
A pointload of magnitude 20 N is applied from the top at its free end.

```
---> x
\\\\| |
\\\\| 20 N v y
\\\\|________________ |
\\\\| |_______________V
\\\\| 1.5*I _______I_______|
\\\\|________________|
\\\\| :
\\\\|----------------|---------------|
2.0 m 2.0 m
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I = symbols('E, I')
>>> R1, R2 = symbols('R1, R2')
>>> b1 = Beam(2, E, 1.5*I)
>>> b2 = Beam(2, E, I)
>>> b = b1.join(b2, "fixed")
>>> b.apply_load(20, 4, -1)
>>> b.apply_load(R1, 0, -1)
>>> b.apply_load(R2, 0, -2)
>>> b.bc_slope = [(0, 0)]
>>> b.bc_deflection = [(0, 0)]
>>> b.solve_for_reaction_loads(R1, R2)
>>> b.load
-2 -1 -1
80⋅<x> - 20⋅<x> + 20⋅<x - 4>
>>> b.shear_force()
-1 0 0
- 80⋅<x> + 20⋅<x> - 20⋅<x - 4>
>>> b.bending_moment()
0 1 1
- 80⋅<x> + 20⋅<x> - 20⋅<x - 4>
>>> b.slope()
⎛ 1 2 2 ⎞
⎜ - 80⋅<x> + 10⋅<x> - 10⋅<x - 4> 120 ⎟
⎜ ───────────────────────────────── + ─── ⎟ ⎛ 1 2 2⎞ 0 ⎛ 1 2 2⎞ 0
⎜ I I 80.0⎟ 0 0.666666666666667⋅⎝- 80⋅<x> + 10⋅<x> - 10⋅<x - 4> ⎠⋅<x> 0.666666666666667⋅⎝- 80⋅<x> + 10⋅<x> - 10⋅<x - 4> ⎠⋅<x - 2>
⎜- ─────────────────────────────────────── + ────⎟⋅<x - 2> - ────────────────────────────────────────────────────────── + ──────────────────────────────────────────────────────────────
⎝ E E⋅I ⎠ E⋅I E⋅I
```

### Example 10¶

A combined beam, with constant flexural rigidity `E*I`

, is formed by joining
a Beam of length `2*l`

to the right of another Beam of length `l`

. The whole beam
is fixed at both of its ends. A point load of magnitude `P`

is also applied
from the top at a distance of `2*l`

from starting point.

```
---> x
|
\\\\| P v y |\\\\
\\\\| | |\\\\
\\\\| V |\\\\
\\\\|____________ ________________________|\\\\
\\\\|____________O________________________|\\\\
\\\\| : : |\\\\
\\\\| : : |\\\\
\\\\|------------|------------|-----------|\\\\
l l l
```

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I = symbols('E, I')
>>> l = symbols('l', positive=True)
>>> b1 = Beam(l ,E,I)
>>> b2 = Beam(2*l ,E,I)
>>> b = b1.join(b2,"hinge")
>>> M1, A1, M2, A2, P = symbols('M1 A1 M2 A2 P')
>>> b.apply_load(A1, 0, -1)
>>> b.apply_load(M1, 0 ,-2)
>>> b.apply_load(P, 2*l, -1)
>>> b.apply_load(A2, 3*l, -1)
>>> b.apply_load(M2, 3*l, -2)
>>> b.bc_slope=[(0, 0), (3*l, 0)]
>>> b.bc_deflection=[(0, 0), (3*l, 0)]
>>> b.solve_for_reaction_loads(M1, A1, M2, A2)
>>> b.reaction_loads
⎧ -5⋅P -13⋅P 5⋅P⋅l -4⋅P⋅l ⎫
⎨A₁: ─────, A₂: ──────, M₁: ─────, M₂: ───────⎬
⎩ 18 18 18 9 ⎭
>>> b.load
2 -3 -2 -2 -1 -1
P⋅l ⋅<-l + x> 5⋅P⋅l⋅<x> 4⋅P⋅l⋅<-3⋅l + x> 5⋅P⋅<x> -1 13⋅P⋅<-3⋅l + x>
- ─────────────── + ─────────── - ────────────────── - ───────── + P⋅<-2⋅l + x> - ─────────────────
12 18 9 18 18
>>> b.shear_force()
2 -2 -1 -1 0 0
P⋅l ⋅<-l + x> 5⋅P⋅l⋅<x> 4⋅P⋅l⋅<-3⋅l + x> 5⋅P⋅<x> 0 13⋅P⋅<-3⋅l + x>
─────────────── - ─────────── + ────────────────── + ──────── - P⋅<-2⋅l + x> + ────────────────
12 18 9 18 18
>>> b.bending_moment()
2 -1 0 0 1 1
P⋅l ⋅<-l + x> 5⋅P⋅l⋅<x> 4⋅P⋅l⋅<-3⋅l + x> 5⋅P⋅<x> 1 13⋅P⋅<-3⋅l + x>
─────────────── - ────────── + ───────────────── + ──────── - P⋅<-2⋅l + x> + ────────────────
12 18 9 18 18
>>> b.slope()
⎛ 2 0 1 1 2 2 2⎞
⎜P⋅l ⋅<-l + x> 5⋅P⋅l⋅<x> 4⋅P⋅l⋅<-3⋅l + x> 5⋅P⋅<x> P⋅<-2⋅l + x> 13⋅P⋅<-3⋅l + x> ⎟
-⎜────────────── - ────────── + ───────────────── + ──────── - ───────────── + ────────────────⎟
⎝ 12 18 9 36 2 36 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 2 1 2 2 3 3 3⎞
⎜P⋅l ⋅<-l + x> 5⋅P⋅l⋅<x> 2⋅P⋅l⋅<-3⋅l + x> 5⋅P⋅<x> P⋅<-2⋅l + x> 13⋅P⋅<-3⋅l + x> ⎟
-⎜────────────── - ────────── + ───────────────── + ──────── - ───────────── + ────────────────⎟
⎝ 12 36 9 108 6 108 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

### Example 11¶

Any type of load defined by a polynomial can be applied to the beam. This allows approximation of arbitrary load distributions. The following example shows six truncated polynomial loads across the surface of a beam.

```
>>> n = 6
>>> b = Beam(10*n, E, I)
>>> for i in range(n):
... b.apply_load(1 / (5**i), 10*i + 5, i, end=10*i + 10)
>>> plot(b.load, (x, 0, 10*n))
```

### Example 12¶

The same Beam form Example 10 but using `apply_rotation_hinge()`

and `apply_support()`

methods.

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols
>>> E, I = symbols('E, I')
>>> l = symbols('l', positive=True)
>>> b = Beam(3*l, E, I)
>>> r0,m0 = b.apply_support(0, type='fixed')
>>> r3l,m3l = b.apply_support(3*l, type='fixed')
>>> F = symbols('F')
>>> p1 = b.apply_rotation_hinge(l)
>>> b.apply_load(F, 2*l, -1)
>>> b.solve_for_reaction_loads(r0,m0,r3l,m3l)
>>> b.reaction_loads
⎧ 5⋅F⋅l -4⋅F⋅l -5⋅F -13⋅F ⎫
⎨M₀: ─────, M_3*l: ───────, R₀: ─────, R_3*l: ──────⎬
⎩ 18 9 18 18 ⎭
>>> b.load
2 -3 -2 -2 -1 -1
F⋅l ⋅<-l + x> 5⋅F⋅l⋅<x> 4⋅F⋅l⋅<-3⋅l + x> 5⋅F⋅<x> -1 13⋅F⋅<-3⋅l + x>
- ─────────────── + ─────────── - ────────────────── - ───────── + F⋅<-2⋅l + x> - ─────────────────
12 18 9 18 18
>>> b.shear_force()
2 -2 -1 -1 0 0
F⋅l ⋅<-l + x> 5⋅F⋅l⋅<x> 4⋅F⋅l⋅<-3⋅l + x> 5⋅F⋅<x> 0 13⋅F⋅<-3⋅l + x>
─────────────── - ─────────── + ────────────────── + ──────── - F⋅<-2⋅l + x> + ────────────────
12 18 9 18 18
>>> b.bending_moment()
2 -1 0 0 1 1
F⋅l ⋅<-l + x> 5⋅F⋅l⋅<x> 4⋅F⋅l⋅<-3⋅l + x> 5⋅F⋅<x> 1 13⋅F⋅<-3⋅l + x>
─────────────── - ────────── + ───────────────── + ──────── - F⋅<-2⋅l + x> + ────────────────
12 18 9 18 18
>>> b.slope()
⎛ 2 0 1 1 2 2 2⎞
⎜F⋅l ⋅<-l + x> 5⋅F⋅l⋅<x> 4⋅F⋅l⋅<-3⋅l + x> 5⋅F⋅<x> F⋅<-2⋅l + x> 13⋅F⋅<-3⋅l + x> ⎟
-⎜────────────── - ────────── + ───────────────── + ──────── - ───────────── + ────────────────⎟
⎝ 12 18 9 36 2 36 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 2 1 2 2 3 3 3⎞
⎜F⋅l ⋅<-l + x> 5⋅F⋅l⋅<x> 2⋅F⋅l⋅<-3⋅l + x> 5⋅F⋅<x> F⋅<-2⋅l + x> 13⋅F⋅<-3⋅l + x> ⎟
-⎜────────────── - ────────── + ───────────────── + ──────── - ───────────── + ────────────────⎟
⎝ 12 36 9 108 6 108 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

### Example 13¶

There is a beam of length `3*l`

fixed at both ends. A load is applied at `l/3`

and a distributed load `q1`

is applied between `2*l`

and `3*l`

. The beam has a sliding hinge located at `l*5/2`

using the `apply_sliding_hinge()`

method.

Note

It is possible to use `l*5/2`

as input however it good practise to use `Rational(5, 2)`

instead. This helps the solver to understand
the input as a fraction and will output exact solutions instead of floating point numbers.

```
>>> from sympy.physics.continuum_mechanics.beam import Beam
>>> from sympy import symbols, Rational
>>> E, I = symbols('E, I')
>>> l = symbols('l', positive=True)
>>> b = Beam(3*l, E, I)
>>> r0, m0 = b.apply_support(0, type='fixed')
>>> r3l, m3l = b.apply_support(3*l, type='fixed')
>>> s1 = b.apply_sliding_hinge(l*Rational(5, 2))
>>> P1, q1 = symbols('P1 q1')
>>> b.apply_load(P1, l*Rational(1, 3), -1)
>>> b.apply_load(q1, 2*l, 0, 3*l)
>>> b.solve_for_reaction_loads(r0, r3l, m0, m3l)
>>> b.reaction_loads
⎧ 2 2 ⎫
⎪ 17⋅P₁⋅l 25⋅l ⋅q₁ P₁⋅l 11⋅l ⋅q₁ l⋅q₁ -l⋅q₁ ⎪
⎨M₀: ─────── + ────────, M_3*l: ──── + ────────, R₀: -P₁ - ────, R_3*l: ──────⎬
⎪ 54 36 54 36 2 2 ⎪
⎩ ⎭
>>> b.load
-4
⎛ 3 4 ⎞ 5⋅l
-1 -1 ⎛ 2 ⎞ ⎛ 2 ⎞ ⎝- 25⋅P₁⋅l - 297⋅l ⋅q₁⎠⋅<- ─── + x>
l l⋅q₁⋅<-3⋅l + x> 0 0 ⎛ l⋅q₁⎞ -1 ⎜P₁⋅l 11⋅l ⋅q₁⎟ -2 ⎜17⋅P₁⋅l 25⋅l ⋅q₁⎟ -2 2
P₁⋅<- ─ + x> - ───────────────── + q₁⋅<-2⋅l + x> - q₁⋅<-3⋅l + x> + ⎜-P₁ - ────⎟⋅<x> + ⎜──── + ────────⎟⋅<-3⋅l + x> + ⎜─────── + ────────⎟⋅<x> + ──────────────────────────────────────
3 2 ⎝ 2 ⎠ ⎝ 54 36 ⎠ ⎝ 54 36 ⎠ 324
>>> b.shear_force()
0 0 ⎛ 2 ⎞ ⎛ 2 ⎞ ⎛ 3 4 ⎞ -3
l l⋅q₁⋅<-3⋅l + x> 1 1 ⎛ l⋅q₁⎞ 0 ⎜P₁⋅l 11⋅l ⋅q₁⎟ -1 ⎜17⋅P₁⋅l 25⋅l ⋅q₁⎟ -1 ⎜ 25⋅P₁⋅l 11⋅l ⋅q₁⎟ 5⋅l
- P₁⋅<- ─ + x> + ──────────────── - q₁⋅<-2⋅l + x> + q₁⋅<-3⋅l + x> - ⎜-P₁ - ────⎟⋅<x> - ⎜──── + ────────⎟⋅<-3⋅l + x> - ⎜─────── + ────────⎟⋅<x> - ⎜- ──────── - ────────⎟⋅<- ─── + x>
3 2 ⎝ 2 ⎠ ⎝ 54 36 ⎠ ⎝ 54 36 ⎠ ⎝ 324 12 ⎠ 2
>>> b.bending_moment()
1 1 2 2 ⎛ 2 ⎞ ⎛ 2 ⎞ ⎛ 3 4 ⎞ -2
l l⋅q₁⋅<-3⋅l + x> q₁⋅<-2⋅l + x> q₁⋅<-3⋅l + x> ⎛ l⋅q₁⎞ 1 ⎜ 17⋅P₁⋅l 25⋅l ⋅q₁⎟ 0 ⎜ P₁⋅l 11⋅l ⋅q₁⎟ 0 ⎜25⋅P₁⋅l 11⋅l ⋅q₁⎟ 5⋅l
- P₁⋅<- ─ + x> + ──────────────── - ────────────── + ────────────── + ⎜P₁ + ────⎟⋅<x> + ⎜- ─────── - ────────⎟⋅<x> + ⎜- ──── - ────────⎟⋅<-3⋅l + x> + ⎜──────── + ────────⎟⋅<- ─── + x>
3 2 2 2 ⎝ 2 ⎠ ⎝ 54 36 ⎠ ⎝ 54 36 ⎠ ⎝ 324 12 ⎠ 2
>>> b.slope()
⎛ -1 2 -1 ⎞
⎜ 3 5⋅l l 4 5⋅l ⎟
⎜25⋅P₁⋅l ⋅<- ─── + x> 1 1 2 P₁⋅<- ─ + x> 11⋅l ⋅q₁⋅<- ─── + x> 2 1 2 1 2 2 3 3⎟
⎜ 2 17⋅P₁⋅l⋅<x> P₁⋅l⋅<-3⋅l + x> P₁⋅<x> 3 2 25⋅l ⋅q₁⋅<x> 11⋅l ⋅q₁⋅<-3⋅l + x> l⋅q₁⋅<x> l⋅q₁⋅<-3⋅l + x> q₁⋅<-2⋅l + x> q₁⋅<-3⋅l + x> ⎟
-⎜────────────────────── - ──────────── - ──────────────── + ─────── - ───────────── + ────────────────────── - ───────────── - ──────────────────── + ───────── + ──────────────── - ────────────── + ──────────────⎟
⎝ 324 54 54 2 2 12 36 36 4 4 6 6 ⎠
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
>>> b.deflection()
⎛ 0 3 0 ⎞
⎜ 3 5⋅l l 4 5⋅l ⎟
⎜25⋅P₁⋅l ⋅<- ─── + x> 2 2 3 P₁⋅<- ─ + x> 11⋅l ⋅q₁⋅<- ─── + x> 2 2 2 2 3 3 4 4⎟
⎜ 2 17⋅P₁⋅l⋅<x> P₁⋅l⋅<-3⋅l + x> P₁⋅<x> 3 2 25⋅l ⋅q₁⋅<x> 11⋅l ⋅q₁⋅<-3⋅l + x> l⋅q₁⋅<x> l⋅q₁⋅<-3⋅l + x> q₁⋅<-2⋅l + x> q₁⋅<-3⋅l + x> ⎟
-⎜───────────────────── - ──────────── - ──────────────── + ─────── - ───────────── + ───────────────────── - ───────────── - ──────────────────── + ───────── + ──────────────── - ────────────── + ──────────────⎟
⎝ 324 108 108 6 6 12 72 72 12 12 24 24 ⎠
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
E⋅I
```

## Source: https://docs.sympy.org/latest/tutorials/physics/control/index.html

# Control Tutorials¶

The control module in SymPy provides essential tools for symbolic control system analysis. The TransferFunction class allows for creating transfer functions and analyzing their properties, such as stability is_stable(), poles, and zeros. Series, Parallel, and Feedback classes enable constructing and simplifying system interconnections. The TransferFunctionMatrix handles multi-input, multi-output (MIMO) systems, while MIMOSeries, MIMOParallel, and MIMOFeedback extend these functionalities for complex systems.

Additionally, the module includes the StateSpace class, which allows for modeling control systems using state variables, inputs, and outputs in matrix form. This representation is particularly useful for time-domain analysis and handling complex MIMO systems.

This tutorial contains a brief guide on how to solve Control Problems using \(TransferFunction\) and \(StateSpace\).

## Source: https://docs.sympy.org/latest/tutorials/physics/control/control_problems.html

# Control Package Examples¶

Given below, are some comprehensive textbook examples to demonstrate the possible use cases of the Control Module.

## Example 1¶

A pole zero plot of an unknown **Transfer Function** is given above.

Determine the exact Transfer Function if the continuous time

**DC Gain**of the system is**20**.Is the TransferFunction

**stable**or**unstable**in nature.Obtain the

**unit impulse response**of the system.Find the initial value of the

**time-domain response**of system without using the time domain equation.

Solution

>>> # Imports >>> from sympy import symbols, I, limit, pprint, solve, oo >>> from sympy.physics.control import TransferFunctionSubpart 1

>>> s, k = symbols('s k') >>> gain = k # Let unknown gain be k >>> a = [-3] # Zero at -3 in S plane >>> b = [-1, -2-I, -2+I] # Poles at -1, (-2, j) and (-2, -j) in S plane >>> tf = TransferFunction.from_zpk(a, b, gain, s) >>> pprint(tf) k*(s + 3) ------------------------------- (s + 1)*(s + 2 - I)*(s + 2 + I) >>> gain = tf.dc_gain() >>> print(gain) 3*k*(2 - I)*(2 + I)/25 >>> K = solve(gain - 20, k)[0] # Solve for k >>> tf = tf.subs({k: K}) # Reconstruct the TransferFunction using .subs() >>> pprint(tf.expand()) 100*s ----- + 100 3 ------------------- 3 2 s + 5*s + 9*s + 5Subpart 2

>>> tf.is_stable() # Expect True, since poles lie in the left half of S plane TrueSubpart 3

>>> from sympy import inverse_laplace_transform >>> t = symbols('t', positive = True) >>> # Convert from S to T domain for impulse response >>> tf = tf.to_expr() >>> Impulse_Response = inverse_laplace_transform(tf, s, t) >>> pprint(Impulse_Response) -t -2*t 100*e 100*e *cos(t) ------- - ---------------- 3 3Subpart 4

>>> # Apply the Initial Value Theorem on Equation of S domain >>> # limit(y(t), t, 0) = limit(s*Y(S), s, oo) >>> limit(s*tf, s, oo) 0

## Example 2¶

Find the Transfer Function of the following Spring-Mass dampering system :

Solution

```
>>> # Imports
>>> from sympy import Function, laplace_transform, laplace_initial_conds, laplace_correspondence, diff, Symbol, solve
>>> from sympy.abc import s, t
>>> from sympy.physics.control import TransferFunction
>>> y = Function('y')
>>> Y = Function('Y')
>>> u = Function('u')
>>> U = Function('U')
>>> k = Symbol('k') # Spring Constant
>>> c = Symbol('c') # Damper
>>> m = Symbol('m') # Mass of block
```

The **DIFFERENTIAL EQUATION** of the system will be as follows:

\[\begin{split}\frac{{d^2y(t)}}{{dt^2}} + c\frac{{dy(t)}}{{dt}} + ky(t) = w^2u(t) \\\\ with \ initial \ conditions \\ y(0) = t,\quad\frac{{dy}}{{dt}}\bigg|_{t=0} = 0\\\end{split}\]>>> f = m*diff(y(t), t, t) + c*diff(y(t), t) + k*y(t) - u(t) >>> F = laplace_transform(f, t, s, noconds=True) >>> F = laplace_correspondence(F, {u: U, y: Y}) >>> F = laplace_initial_conds(F, t, {y: [0, 0]}) >>> t = (solve(F, Y(s))[0])/U(s) # To construct Transfer Function from Y(s) and U(s) >>> tf = TransferFunction.from_rational_expression(t, s) >>> pprint(tf) 1 -------------- 2 c*s + k + m*s

## Example 3¶

A signal matrix in the time-domain, also known as the *impulse response matrix* **g(t)** is given below.

\[\begin{split}g(t) = \begin{bmatrix} (1-t)e^{-t} & e^{-2t} \\ -e^{-t}+5e^{-2t} & \left(-3\sqrt{3}\sin\left(\frac{\sqrt{3}t}{2}\right)+\cos\left(\frac{\sqrt{3}t}{2}\right)\right)e^{-\frac{t}{2}} \end{bmatrix}\end{split}\]

With Respect to this matrix, find

The system matrix (Transfer Function Matrix) in the Laplace domain (

**g(t)**→**G(s)**).The number of input and output signals in the system.

**Poles**and**Zeros**of the system elements (individual Transfer Functions in Transfer Function Matrix) in the Laplace domain*(Note: The actual poles and zeros of a MIMO system are NOT the poles and zeros of the individual elements of the transfer function matrix)*. Also, visualise the poles and zeros of the individual transfer function corresponding to the**1st input**and**1st output**of the**G(s)**matrix.Plot the

**unit step response**of the individual Transfer Function corresponding to the**1st input**and**1st output**of the**G(s)**matrix.Analyse the Bode magnitude and phase plot of the Transfer Function corresponding to

**1st input**and**2nd output**of the**G(s)**matrix.

Solution

>>> # Imports >>> from sympy import Matrix, laplace_transform, inverse_laplace_transform, exp, cos, sqrt, sin, pprint >>> from sympy.abc import s, t >>> from sympy.physics.control import *Subpart 1

>>> g = Matrix([[exp(-t)*(1 - t), exp(-2*t)], [5*exp((-2*t))-exp((-t)), (cos((sqrt(3)*t)/2) - 3*sqrt(3)*sin((sqrt(3)*t)/2))*exp(-t/2)]]) >>> G = g.applyfunc(lambda a: laplace_transform(a, t, s)[0]) >>> pprint(G) [ 1 1 1 ] [----- - -------- ----- ] [s + 1 2 s + 2 ] [ (s + 1) ] [ ] [ 5 1 s + 1/2 9 ] [ ----- - ----- -------------- - ------------------] [ s + 2 s + 1 2 3 / 2 3\] [ (s + 1/2) + - 2*|(s + 1/2) + -|] [ 4 \ 4/]Subpart 2

>>> G = TransferFunctionMatrix.from_Matrix(G, s) >>> type(G) <class 'sympy.physics.control.lti.TransferFunctionMatrix'> >>> type(G[0]) <class 'sympy.physics.control.lti.TransferFunction'> >>> print(f'Inputs = {G.num_inputs}, Outputs = {G.num_outputs}') Inputs = 2, Outputs = 2Subpart 3

>>> G.elem_poles() [[[-1, -1, -1], [-2]], [[-2, -1], [-1/2 - sqrt(3)*I/2, -1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]]] >>> G.elem_zeros() [[[-1, 0], []], [[-3/4], [4, -1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]]] >>> pole_zero_plot(G[0, 0])Subpart 4

>>> tf1 = G[0, 0] >>> pprint(tf1) 2 -s + (s + 1) - 1 ----------------- 3 (s + 1) >>> step_response_plot(tf1)Subpart 5

>>> tf2 = G[0, 1] >>> bode_magnitude_plot(tf2)>>> bode_phase_plot(tf2)

## Example 4¶

A system is designed by arranging

**P(s)**and**C(s)**in a series configuration*(Values of P(s) and C(s) are provided below)*. Compute the equivalent system matrix, when the order of blocks is reversed*(i.e. C(s) then P(s))*.\[\begin{split}P(s) = \begin{bmatrix} \frac{1}{s} & \frac{2}{s+2} \\ 0 & 3 \end{bmatrix}\end{split}\]\[\begin{split}C(s) = \begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}\end{split}\]Also, find the

**equivalent closed-loop system***(or the ratio v/u from the block diagram given below)*for the system (negative-feedback loop) having**C(s)**as the**controller**and**P(s)**as**plant***(Refer to the block diagram given below)*.

Solution

>>> # Imports >>> from sympy import Matrix, pprint >>> from sympy.abc import s, t >>> from sympy.physics.control import *Subpart 1

>>> P_mat = Matrix([[1/s, 2/(2+s)], [0, 3]]) >>> C_mat = Matrix([[1, 1], [2, 2]]) >>> P = TransferFunctionMatrix.from_Matrix(P_mat, var=s) >>> C = TransferFunctionMatrix.from_Matrix(C_mat, var=s) >>> # Series equivalent, considering (Input)→[P]→[C]→(Output). Note that order of matrix multiplication is opposite to the order in which the elements are arranged. >>> pprint(C*P) [1 1] [1 2 ] [- -] [- -----] [1 1] [s s + 2] [ ] *[ ] [2 2] [0 3 ] [- -] [- - ] [1 1]{t} [1 1 ]{t} >>> # Series equivalent, considering (Input)→[C]→[P]→(Output). >>> pprint(P*C) [1 2 ] [1 1] [- -----] [- -] [s s + 2] [1 1] [ ] *[ ] [0 3 ] [2 2] [- - ] [- -] [1 1 ]{t} [1 1]{t} >>> pprint((C*P).doit()) [1 3*s + 8 ] [- ------- ] [s s + 2 ] [ ] [2 6*s + 16] [- --------] [s s + 2 ]{t} >>> pprint((P*C).doit()) [ 5*s + 2 5*s + 2 ] [--------- ---------] [s*(s + 2) s*(s + 2)] [ ] [ 6 6 ] [ - - ] [ 1 1 ]{t}Subpart 2

>>> tfm_feedback = MIMOFeedback(P, C, sign=-1) >>> pprint(tfm_feedback.doit()) # ((I + P*C)**-1)*P [ 7*s + 14 -s - 6 ] [--------------- ---------------] [ 2 2 ] [7*s + 19*s + 2 7*s + 19*s + 2] [ ] [ 2 ] [ -6*s - 12 3*s + 9*s + 6 ] [--------------- ---------------] [ 2 2 ] [7*s + 19*s + 2 7*s + 19*s + 2]{t}

## Example 5¶

Given,

\[ \begin{align}\begin{aligned}\begin{split}G1 &= \frac{1}{10 + s}\\\\\end{split}\\\begin{split}G2 &= \frac{1}{1 + s}\\\\\end{split}\\\begin{split}G3 &= \frac{1 + s^2}{4 + 4s + s^2}\\\\\end{split}\\\begin{split}G4 &= \frac{1 + s}{6 + s}\\\\\end{split}\\\begin{split}H1 &= \frac{1 + s}{2 + s}\\\\\end{split}\\\begin{split}H2 &= \frac{2 \cdot (6 + s)}{1 + s}\\\\\end{split}\\\begin{split}H3 &= 1\\\end{split}\end{aligned}\end{align} \]

Where \(s\) is the variable of the transfer function (in Laplace Domain).

Find

The equivalent Transfer Function representing the system given above.

Pole-Zero plot of the system.

Solution

>>> from sympy.abc import s >>> from sympy.physics.control import * >>> G1 = TransferFunction(1, 10 + s, s) >>> G2 = TransferFunction(1, 1 + s, s) >>> G3 = TransferFunction(1 + s**2, 4 + 4*s + s**2, s) >>> G4 = TransferFunction(1 + s, 6 + s, s) >>> H1 = TransferFunction(1 + s, 2 + s, s) >>> H2 = TransferFunction(2*(6 + s), 1 + s, s) >>> H3 = TransferFunction(1, 1, s) >>> sys1 = Series(G3, G4) >>> sys2 = Feedback(sys1, H1, 1).doit() >>> sys3 = Series(G2, sys2) >>> sys4 = Feedback(sys3, H2).doit() >>> sys5 = Series(G1, sys4) >>> sys6 = Feedback(sys5, H3) >>> sys6 # Final unevaluated Feedback object Feedback(Series(TransferFunction(1, s + 10, s), TransferFunction((s + 1)**3*(s + 2)*(s + 6)**2*(s**2 + 1)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4)**2, (s + 1)*(s + 6)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*((s + 1)**2*(s + 6)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4) + (s + 1)*(s + 2)*(s + 6)*(2*s + 12)*(s**2 + 1)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4), s)), TransferFunction(1, 1, s), -1) >>> sys6.doit() # Reducing to TransferFunction form without simplification TransferFunction((s + 1)**4*(s + 2)*(s + 6)**3*(s + 10)*(s**2 + 1)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))**2*((s + 1)**2*(s + 6)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4) + (s + 1)*(s + 2)*(s + 6)*(2*s + 12)*(s**2 + 1)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4)**3, (s + 1)*(s + 6)*(s + 10)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*((s + 1)**2*(s + 6)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4) + (s + 1)*(s + 2)*(s + 6)*(2*s + 12)*(s**2 + 1)*(s**2 + 4*s + 4))*((s + 1)**3*(s + 2)*(s + 6)**2*(s**2 + 1)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4)**2 + (s + 1)*(s + 6)*(s + 10)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*((s + 1)**2*(s + 6)*(-(s + 1)**2*(s**2 + 1) + (s + 2)*(s + 6)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4) + (s + 1)*(s + 2)*(s + 6)*(2*s + 12)*(s**2 + 1)*(s**2 + 4*s + 4))*(s**2 + 4*s + 4))*(s**2 + 4*s + 4), s) >>> sys6 = sys6.doit(cancel=True, expand=True) # Simplified TransferFunction form >>> sys6 TransferFunction(s**4 + 3*s**3 + 3*s**2 + 3*s + 2, 12*s**5 + 193*s**4 + 873*s**3 + 1644*s**2 + 1484*s + 712, s) >>> pole_zero_plot(sys6)

## Source: https://docs.sympy.org/latest/tutorials/physics/control/electrical_problems.html

# Electrical Problems using StateSpace¶

The state-space approach is a powerful method used to model and analyze systems in control theory. Instead of focusing solely on the input-output relationships like the transfer function approach, the state-space approach represents systems as a set of first-order differential equations.

The state-space representation of a system can be written as:

\[\begin{split}\dot{x}(t) = A x(t) + B u(t) \\ y(t) = C x(t) + D u(t)\end{split}\]

Where \(x(t)\) is the state vector, \(u(t)\) is the input vector, \(y(t)\) is the output vector, \(A\), \(B\), \(C\), and \(D\) are matrices that define the system dynamics.

Below are some examples to demonstrate the use of StateSpace to solve Electrical problems.

## Example 1¶

In a series RLC circuit, we have a resistor \(R\), an inductor \(L\), and a capacitor \(C\) connected in series with an input voltage \(v_{in}(t)\). The state variables are the current through the inductor \(i(t)\) and the voltage across the capacitor \(v_C(t)\).

Applying **Kirchhoff’s Voltage Law** (KVL) around the loop in the above diagram gives:

\[v_{in}(t) = R \cdot i(t) + L \frac{di(t)}{dt} + V_C(t)\]

Where: \(v_{in}(t)\) is the input voltage, \(i(t)\) is the current through the inductor and \(v_C(t)\) is the voltage across the capacitor.

This equation relates the input voltage to the elements of the RLC circuit.

**Capacitor Voltage Equation**

The voltage across the capacitor can be related to the current by:

\[V_C(t) = \frac{1}{C} \int i(t) \, dt\]

Taking the time derivative of both sides, we obtain the rate of change of the capacitor voltage:

\[\dot{v}_C(t) = \frac{d v_C(t)}{dt} = \frac{i(t)}{C}\]

This equation shows that the rate of change of the capacitor voltage is proportional to the current through the circuit.

From the KVL equation, solving for the derivative of the current gives:

\[\frac{di(t)}{dt} = -\frac{R}{L} i(t) - \frac{1}{L} v_C(t) + \frac{1}{L} v_{in}(t)\]

This is the first-order differential equation that describes the rate of change of the current in terms of the circuit’s components and input voltage.

The state-space representation expresses the system in terms of state variables, which are typically the variables that describe the energy stored in the circuit elements (such as current and voltage).

We define the state vector \(X(t)\) as:

\[\begin{split}X(t) = \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} = \begin{bmatrix} i(t) \\ v_C(t) \end{bmatrix}\end{split}\]

Here \(x_1(t) = i(t)\) is the current through the inductor and \(x_2(t) = v_C(t)\) is the voltage across the capacitor.

The input vector \(U(t)\) is the input voltage:

\[U(t) = v_{in}(t)\]

The system of differential equations in terms of the state variables becomes:

The derivative of the current:

\[\dot{x}_1(t) = -\frac{R}{L} x_1(t) - \frac{1}{L} x_2(t) + \frac{1}{L} v_{in}(t)\]The derivative of the capacitor voltage:

\[\dot{x}_2(t) = \frac{x_1(t)}{C}\]

The matrices for the series RLC circuit are:

\[\begin{split}A = \begin{bmatrix} -\frac{R}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix}, B = \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix}, C = \begin{bmatrix} 0 & 1 \end{bmatrix}, D = \begin{bmatrix} 0 \end{bmatrix}\end{split}\]

Thus, the state-space representation of the series RLC circuit is:

\[ \begin{align}\begin{aligned}\begin{split}\dot{X}(t) = \begin{bmatrix} -\frac{R}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} V_{in}(t)\end{split}\\\begin{split}Y(t) = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} 0 \end{bmatrix} V_{in}(t)\end{split}\end{aligned}\end{align} \]

The state-space representation provides a compact way of modeling the series RLC circuit by using matrices to describe the system’s dynamics. The matrices \(A\), \(B\), \(C\), and \(D\) capture the relationships between the circuit’s state variables, input, and output. This representation is particularly useful for analyzing the system’s behavior in the time domain and for designing control systems.

Solution

>>> from sympy import Matrix, symbols, pprint >>> from sympy.physics.control import * >>> R, L, C = symbols('R L C') >>> A = Matrix([[-R/L, -1/L], [1/C, 0]]) >>> B = Matrix([[1/L], [0]]) >>> C = Matrix([[0, 1]]) >>> D = Matrix([[0]]) >>> ss = StateSpace(A, B, C, D) >>> ss StateSpace(Matrix([ [-R/L, -1/L], [ 1/C, 0]]), Matrix([ [1/L], [ 0]]), Matrix([[0, 1]]), Matrix([[0]]))We can convert the StateSpace to TransferFunction by rewrite method.

>>> tf = ss.rewrite(TransferFunction)[0][0] >>> tf TransferFunction(1, C*L*s**2 + C*R*s + 1, s)

## Example 2¶

Obtain the state model for a system represented by an electrical system as shown in figure

The system is modeled with two state variables, \(x_1(t)\) and \(x_2(t)\), which are related to the physical voltages at the nodes \(v_1(t)\) and \(v_2(t)\) respectively.

Let the two state variables be defined as:

\[ \begin{align}\begin{aligned}v_1(t) = x_1(t)\\v_2(t) = x_2(t)\end{aligned}\end{align} \]

The governing equations are derived by applying Kirchhoff’s Current Law (KCL) at the nodes \(v_1(t)\) and \(v_2(t)\).

Applying KCL at node \(v_1(t)\):

\[\frac{v_1(t) - u(t)}{R} + C \frac{d v_1(t)}{dt} + \frac{v_1(t) - v_2(t)}{R} = 0\]

Substituting the state variables:

\[\frac{x_1(t) - u(t)}{R} + C \frac{dx_1(t)}{dt} + \frac{x_1(t) - x_2(t)}{R} = 0\]

Simplifying:

\[C \dot{x_1}(t) = -\frac{2x_1(t)}{R} + \frac{x_2(t)}{R} + \frac{u(t)}{R}\]

Thus, the state equation for \(x_1(t)\) becomes:

\[\dot{x_1}(t) = -\frac{2x_1(t)}{RC} + \frac{x_2(t)}{RC} + \frac{u(t)}{RC}\]

Applying KCL at node \(v_2(t)\):

\[C \frac{d v_2(t)}{dt} + \frac{v_2(t) - v_1(t)}{R} = 0\]

Substituting the state variables:

\[C \frac{d x_2(t)}{dt} + \frac{x_2(t) - x_1(t)}{R} = 0\]

Simplifying:

\[C \dot{x_2}(t) = \frac{x_1(t)}{R} - \frac{x_2(t)}{R}\]

Thus, the state equation for \(x_2(t)\) becomes:

\[\dot{x_2}(t) = \frac{x_1(t)}{RC} - \frac{x_2(t)}{RC}\]

The state-space representation is given by the following matrix equation:

\[\begin{split}\begin{bmatrix} \dot{x_1}(t) \\ \dot{x_2}(t) \end{bmatrix} = \begin{bmatrix} -\frac{2}{RC} & \frac{1}{RC} \\ \frac{1}{RC} & -\frac{1}{RC} \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{RC} \\ 0 \end{bmatrix} u(t)\end{split}\]

The output of the circuit is defined as:

\[y(t) = v_2(t) = x_2(t)\]

Thus, the output equation can be written as:

\[\begin{split}y(t) = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix}\end{split}\]

Solution

```
>>> from sympy import symbols, Matrix
>>> from sympy.physics.control import *
>>> R, C = symbols('R C')
>>> A = Matrix([[-2/(R*C), 1/(R*C)], [1/(R*C), -1/(R*C)]])
>>> B = Matrix([[1/(R*C)], [0]])
>>> C = Matrix([[0, 1]])
>>> ss = StateSpace(A, B, C)
>>> ss
StateSpace(Matrix([
[-2/(C*R), 1/(C*R)],
[ 1/(C*R), -1/(C*R)]]), Matrix([
[1/(C*R)],
[ 0]]), Matrix([[0, 1]]), Matrix([[0]]))
```

## Source: https://docs.sympy.org/latest/tutorials/physics/control/mechanics_problems.html

# Mechanics Problems using StateSpace¶

Below are some Mechanics problems that can be solved using StateSpace.

## Example 1¶

A spring-mass-damping system can be modeled using a mass (m), a spring with a constant (k), and a damper with a damping coefficient (b). The spring force is proportional to the displacement of the mass, and the damping force is proportional to the velocity of the mass. Find the frequency response of the system. The free-body diagram for this system is shown below:

The equation of motion for the mass-spring-damper system is given by:

where:

\(x\) is the displacement of the mass,

\(\dot{x}\) is the velocity of the mass,

\(\ddot{x}\) is the acceleration of the mass,

\(F(t)\) is the external force applied to the system.

To determine the state-space representation of the mass-spring-damper system, we reduce the second-order differential equation to a set of two first-order differential equations. We choose the position and velocity as our state variables:

The state equations become:

The state-space can be represented by:

The state equation can be written as

Using SymPy’s Control Systems Toolbox (CST), we can define the state-space representation and convert it to the transfer function.

### Solution¶

The following code demonstrates how to define the state-space representation of the spring-mass-damper system and convert it to a transfer function using SymPy:

>>> from sympy import symbols, Matrix >>> from sympy.physics.control import *Define the variables

>>> m, k, b = symbols('m k b')Define the state-space matrices

>>> A = Matrix([[0, 1], [-k/m, -b/m]]) >>> B = Matrix([[0], [1/m]]) >>> C = Matrix([[1, 0]]) >>> D = Matrix([[0]])Create the StateSpace model

>>> ss = StateSpace(A, B, C, D) >>> ss StateSpace(Matrix([ [ 0, 1], [-k/m, -b/m]]), Matrix([ [ 0], [1/m]]), Matrix([[1, 0]]), Matrix([[0]]))Converting StateSpace to TransferFunction by rewrite method.

>>> tf = ss.rewrite(TransferFunction)[0][0] >>> tf TransferFunction(1, b*s + k + m*s**2, s)

### References¶

## Example 2¶

This problem explains how to model a rotaional system to state-space model. The system has input torque \(τ_a\) and damping effects \(B_{r1}\) and \(B_{r2}\). The system consists of two flywheels connected by a spring, with the angular positions denoted by \(θ_1\) and \(θ_2\).

The energy variables for the rotating system are potential energy stored in springs \(1/2 K_r \theta^ 2\) and kinetic energy stored in inertial elements \(1/2 J \omega ^ 2\).

The **State Variables:** can be written as:

The goal is to find a set of first-order differential equations that describe the system in terms of these state variables.

First, we write the equations of motion for the two flywheels, including the effects of damping.

For the first flywheel (\(J_1\)):

\[J_1 \ddot{\theta}_1 + B_{r1} \dot{\theta}_1 + K_r\theta_1 - B_{r1} \dot{\theta}_2 = - \tau_a\]For the second flywheel (\(J_2\)):

\[J_2 \ddot{\theta}_2 + (B_{r2} + B_{r1}) \dot{\theta}_2 - B_{r1} \dot{\theta}_1 = 0\]Now we want the equations for the derivates of state variables.

\[\dot{x}_1 = \dot{\theta}_1 = x_2\]\[ \begin{align}\begin{aligned}\dot{x}_2 = \ddot{\theta_1} = \frac{1}{J_1} \left(-\tau_a - B_{r1} \dot{\theta_1} - K_r \theta_1 + B_{r1}\dot{\theta_2} \right)\\\dot{x}_2 = \frac{1}{J_1} \left(-\tau_a - B_{r1} x_2 - K_r x_1 + B_{r1} x_3 \right)\end{aligned}\end{align} \]\[ \begin{align}\begin{aligned}\dot{x}_3 = \ddot{\theta}_2 = \frac{1}{J_2} \left(- (B_{r2} + B_{r1}) \dot{\theta_2} + B_{r1} \dot{\theta_1} \right)\\\dot{x}_3 = \frac{1}{J_2} \left( - (B_{r2} + B_{r1}) x_3 + B_{r1} x_2 \right)\end{aligned}\end{align} \]

The state-space model of the system can be expressed in the standard form:

Where:

**x**is the state vector:\[\begin{split}x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} \theta_1 \\ \dot{\theta}_1 \\ \theta_2 \end{bmatrix}\end{split}\]**u**is the input torque (\(τ_a\)).**y**is the output angular position (\(θ_1\)).

The matrices **A**, **B**, **C**, and **D** are defined as follows:

The

A matrixrepresents the relationship between the state variables. It is defined as:\[\begin{split}A = \begin{bmatrix} 0 & 1 & 0 \\ -\frac{K_r}{J_1} & -\frac{B_{r1}}{J_1} & \frac{B_{r1}}{J_1} \\ 0 & \frac{B_{r1}}{J_2} x_2 & -\frac{B_{r2} + B_{r1}}{J_2} \end{bmatrix}\end{split}\]The

B matrixrepresents the influence of the input torque on the system. It is defined as:\[\begin{split}B = \begin{bmatrix} 0 \\ \frac{-1}{J_1} \\ 0 \end{bmatrix}\end{split}\]The

C matrixdefines the relationship between the output (y) and the state variables (x). Since we are only interested in the angular position θ₁, theC matrixis:\[C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}\]The

D matrixis the direct transmission matrix. Since there is no direct transmission frothe input to the output,Dis zero:\[D = 0\]

### Solution¶

```
>>> from sympy import symbols, Matrix
>>> from sympy.physics.control import StateSpace
>>> K_r, J1, J2, B_r1, B_r2, x2 = symbols('K_r J1 J2 B_r1 B_r2 x2')
>>> A = Matrix([[0, 1, 0], [-K_r/J1, -B_r1/J1, B_r1/J1], [0, B_r1/J2 * x2, - (B_r2 + B_r1)/J2]])
>>> B = Matrix([[0], [-1/J1], [0]])
>>> C = Matrix([[1, 0, 0]])
>>> ss = StateSpace(A, B, C)
>>> ss
StateSpace(Matrix([
[ 0, 1, 0],
[-K_r/J1, -B_r1/J1, B_r1/J1],
[ 0, B_r1*x2/J2, (-B_r1 - B_r2)/J2]]), Matrix([
[ 0],
[-1/J1],
[ 0]]), Matrix([[1, 0, 0]]), Matrix([[0]]))
```
