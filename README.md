# cousera-ml

Python port of the Coursera-Stanford Machine Learning Matlab code

**UPDATE**: This project is not being maintained, I found [this one](https://github.com/tansaku/py-coursera) which I recommend you use too.

## How to use:
Just download or clone the repository, name your solution like the corresponding **.m** file but change the extension to **.py** and finally run:
```
python submit.py
```

## Code design and organization

Same structure of the Matlab code `ex1`, `ex2`, etc folders with corresponding **.py** files instead of **.m** files. There should also be a test file per folder, ex: `ex1/test_ex1.py`.

## Requirements

* numpy
* pytest (optional for testing)

## Development Roadmap

* Implement quicklogin
* More testing
* Add templates for remaining exercises

## Testing

Set your email as an environment variable with `export COURSERA_EMAIL='your@email.com'` and then run `py.test`

## Contributing

1. Find a bug or feature you'd like to work on.
2. If you don't have one, create a free account on `github <http://www.github.com>`.
3. Set up your local development environment with git (`Instructions <http://help.github.com/set-up-git-redirect>`).
4. Fork the `coursera-ml repository <http://www.github.com./elyase/coursera-ml>` (`Instructions <http://help.github.com/fork-a-repo/>`).
5. Create a new working branch for your changes.
6. If possible make sure your patch includes a corresponding test.
7. Commit your changes and submit a pull request (`Instructions <http://help.github.com/send-pull-requests/>`).

## License

The MIT License (MIT)

Copyright (c) 2013, Yaser Martinez Palenzuela

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

