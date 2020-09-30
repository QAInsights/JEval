# 🚀 JEval
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![saythanks](https://img.shields.io/badge/say-thanks-1EAEDB.svg)](https://saythanks.io/to/catch.nkn%40gmail.com)
[![](https://img.shields.io/badge/license-MIT-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-QAInsights-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-YouTube%20Channel-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://www.youtube.com/user/QAInsights?sub_confirmation=1)
[![](https://img.shields.io/badge/donate-paypal-1EAEDB)](https://www.paypal.com/paypalme/NAVEENKUMARN)

<pre>
***************************************************************
*                _   ______                   _               *
*               | | |  ____|                 | |              *
*               | | | |__    __   __   __ _  | |              *
*           _   | | |  __|   \ \ / /  / _` | | |              *
*          | |__| | | |____   \ V /  | (_| | | |              *
*           \____/  |______|   \_/    \__,_| |_|              *
*                                                             *
*            (c) NaveenKumar Namachivayam 2020                *
*                       QAInsights.com                        *
*                                                             *
***************************************************************
</pre>

JEval helps you to evaluate your JMeter test plan and provides recommendation before you start your performance testing.

# 🛠 Prerequisites

* Clone this repository.
* Install the latest version of Python
* Install the dependencies  
`pip install -r requirements.txt`

**Important Notes**  
* *JEval doesn't make any modifications to your JMeter test plan. But it is advisable to make a backup of your JMeter test plan.*  
* *JEval utility doesn't collect any sort of data*

# ✨ Usage

* cd into the repository
* Issue the below command  
`python app.py -f <JMeter-File-Path>`  
E.g.  
`python app.py -f .\jmx\Sample.jmx`

## 💪 Output

![JEval Output](./assets/JEval-Output.jpg)

# ✍ Log file

To view the log, open the `tmp.log` file.

# ✔ Features

* JEval detects the JMeter version and validates the test plan.

* JEval detects following JMeter elements
  - AuthManager
  - CookieManager
  - HeaderManager
  - CacheManager
  - CSVDataSet  
  - TransactionController  
  - ConfigTestElement
  - ConstantTimer
  - UniformRandomTimer
  - GaussianRandomTimer
  - Arguments
  - ProxyControl
  - RegexExtractor
  - TestAction
  - BeanShellSampler
  - JSR223Sampler
  - IfController
  - LoopController
  - ResultCollector
  - ResponseAssertion
  - XPath2Assertion
  - JSONPathAssertion
  - DebugSampler

If you want to add custom elements, you can add it in the `config.yaml` file. 

# 🛑 Limitations

* Doesn't detect JMeter plugins yet.

# 💰 Donate
☕ <a target="_blank" href="https://www.buymeacoffee.com/qainsights">Buy me a tea</a>

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://QAInsights.com"><img src="https://avatars2.githubusercontent.com/u/2826376?v=4" width="100px;" alt=""/><br /><sub><b>NaveenKumar</b></sub></a><br /><a href="https://github.com/QAInsights/JEval/commits?author=QAInsights" title="Code">💻</a></td>
    <td align="center"><a href="https://goo.gl/rTd92i"><img src="https://avatars3.githubusercontent.com/u/6709533?v=4" width="100px;" alt=""/><br /><sub><b>Anthony Gauthier</b></sub></a><br /><a href="https://github.com/QAInsights/JEval/commits?author=delirius325" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!