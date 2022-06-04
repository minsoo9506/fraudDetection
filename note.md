## Tox

- reference: https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/

-> 여기서 4문단 읽을 차례!!!!!!!!!!!!!!!!!!!

### tox를 사용하는 이유

- tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.
- tox is a generic virtualenv management and test command line tool
- acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.
- tox makes it easy to:
  - Test against different versions of Python (which would have alerted Kyle that the library hadn’t been tested against his install version).
  - Test against different dependency versions
  - Capture and run setup steps/ad hoc commands (which Kyle could have made a mistake on / not known about)
  - Isolate environment variables - By design, tox does not pass any evars from the system. Instead you are asked to explicitly declare them (which would have alerted Kyle to any environment variable requirements).
  - Do all the above across Windows / macOS / Linux (which would have saved Kyle if the issue had been due to the OS)

### how tox works

- tox as a kind of combination of virtualenvwrapper and Makefile

1. tox generates a series virtual environments
2. Installs dependencies for each environment (which are defined in config)
3. Runs setup commands (which are also defined in config) for each environment
4. Returns the results from each environment to the user.

- As per the tox docs, At the moment tox supports three configuration locations prioritized in the following order:

1. pyproject.toml
2. tox.ini -> flask, django, numpy 에서 사용하는 format
3. setup.cfg

### 사용

- `tox`
  - `envlist`에 있는 모든 섹션을 실행
- `tox -e 섹션`
  - 해당 섹션을 실행
