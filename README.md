<!-- PROJECT LOGO -->
<br />

<p align="center">
    <img src="images/plog_icon.png" alt="Logo" width="100" height="100">
  <h3 align="center">Python-Log</h3>





<p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>



</p>



<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

> Python에서 제공하는 ``logging`` 모듈에서 자주 사용하는 class 및 method를 활용하여 log를 훨씬 더 쉽게 접근할 수 있게 만들었다.
>
> 해당 project에서는 다음에 대한 기능을 제공한다
>
> 1. Stream Log (console에 log 찍기)
> 2. File Log (파일에 log 찍기)
>    * Rotation (주기를 설정하여 log 파일 관리한다)
> 3. Level Handling (Level에 따른 log 관리)
>
> 그리고 다음 앞으로 제공될 기능이다
>
> 1. Coloring
> 2. Traceback
> 3. Filter
> 4. Catch

### Built With

> 현재 까지는 ubuntu 20.04 LTS 환경에서 `Python 3.8.10.`번전에서 돌아간다.
>
> ``logging`` 0.5.1.2 모듈

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

> ``logging`` 모듈만 import 할 수 있으면 된다

### Installation

1. Clone the repo

   ```
   git clone https://github.com/J-Kyu/Python-Log
   ```

<!-- USAGE EXAMPLES -->

## Usage

> 기본적으로 root logger의 level 수준은 warning이다. 그렇기 때문에 logging.basicConfig를 설정하지 않으면 기본 format에 warning이상의 log는 terminal에 출려이 된다.
>
> 이것을 방지하기 위해(add stream handler를 설정하는 경우에만 terminal에 나에게 하기 위해) logging.basicConfig를 의도적으로 설정하여 stream handler를 등록하게 만든다. 이후 해당 handler를 삭제함으로서 기본으로 제공되는 stream handler를 없앨 수 있다.
>
> 또한, NullHandler를 추가하지 않으면 Logger에서 handler가 아무것도 없는 것으로 판단하여 default handler로 log를 출력한다. 
>
> 결과적으로, logging.basicConfig를 생성하고 NullHandler를 추가한다음, removeHandler를 통해 streamHandler를 삭제하면 nullHandler가 처음 시작하기 적절한 로그가 될 수 있다.  이것을 기준으로 여러 handler를 추가하고 삭제하며 logger를 관리하자.
>
> 

## addStreamHandler

> 기본적으로 root logger의 level 수준은 warning이다. 그리고 config
>
> Config Default Stream Handler

* Logger에 기본적인 stream handler에 대하여 설정한다.

  

## addFileHandler

> Add Handler

|          |      |
| -------- | ---- |
| format   |      |
| datefmt  |      |
| filename |      |
| rotation |      |
|          |      |
|          |      |
|          |      |

### Rotation



### Filter

> Filter는 record의 정보를 토대로 함수를 정의하여 추가할 수 있다. 함수는 record에 대하여 boolean으로 값을 반환하는 함수여야 하며, 이것을 통해 log를 filtering할 수 있다.
>
> :warning: 단, filter에 몇가지 문제점이 존재한다. filter를 통해 log로 전달되는 record(LogRecord)에 접근이 가능하지만, 실제로 호출되는 logger.info()..등등의 함수는 PythonLog를 통하여 logging.info()가 호출이 된다. 즉, lineno혹은 filename과 같이 추가적인 정보를 가져오는 경우 올바르지 않는 값이 전달된다. 고로 아직은 msg에 대한 내용만 filtering 할 수 있다.





```python
from source import logger

logger.add(fileName = "test_size.log",rotation = '200 MB') # log will be recorded until log file is up to 200 MB
logger.add(fileName = "test_atTime.log",rotation = '17:50') # every day 17:50, log will be rolled over
logger.add(fileName = "test_interval.log",rotation = '1 hour') # every 1 hour, log will be rolled over

logger.info("This is info")
logger.debug("THIS is DEBUG")
logger.warning("THIS is warning")
logger.error("THIS is error")
logger.critical("This is critical")
```





<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/J-Kyu/Python-Log/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Your Name - [J-Kyu](https://github.com/J-Kyu)

Project Link: [https://github.com/J-Kyu/Python-Log](https://github.com/J-Kyu/Python-Log)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [filter](https://docs.python.org/ko/3/library/logging.html#logrecord-objects)

