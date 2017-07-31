## Javascript Warmup

* [Learn Javascript in Y Minutes][inxmin]
* [Javascript Garden][garden]

In this exercise, to rapidly get acclimated to Javascript, we will be porting over some Javascript code.  Convert the following Python code to Javascript, on the same example input it should give the same output.

### Python

```python
example = ['cat','dog','rats','mouse','hello', 'star', 'man', 'sun', 'god', 'heelo', 'beach','tsar']

# output every word that has an anagram elsewhere in the input list
def anagrams(input_list):
    output = []

    for word1 in input_list:
        for word2 in input_list:
            if sorted(word1) == sorted(word2) and word1 != word2:
              output.append(word1)
              break;

    return output

anagrams(example)
#=> ['dog', 'rats', 'star', 'god', 'tsar']
```

## Javascript Tutorials

* [JS for Cats (beginner)][jscats]
* [Code School interactive][codeschool]
* [Eloquent Javascript (more advanced)][eloquent]
* [Superhero.js (set of resources)][supjs]
* [understanding `this`][this]

[jscats]: http://jsforcats.com/
[eloquent]: http://eloquentjavascript.net/
[supjs]: http://superherojs.com/
[codeschool]: https://www.codeschool.com/paths/javascript
[inxmin]: http://learnxinyminutes.com/docs/javascript/
[garden]: https://bonsaiden.github.io/JavaScript-Garden/
[this]: http://tomhicks.github.io/code/2014/08/11/some-of-this.html
