# ECE4010J Midterm Example Pack

> 根据 `cheating_sheet.md` 范围整理。题目是按公开教材/课程常见题型重新改写，重点是考试可套模板，不是复制题库。

## 文件目录

| 文件 | 内容 |
|---|---|
| `01_pmf_pdf_cdf_lotus.md` | PMF/PDF/CDF, expectation, variance, LOTUS |
| `02_distribution_recognition_discrete.md` | 离散分布识别：Bernoulli/Binomial/Geometric/NegBin/Hypergeometric/Poisson |
| `03_continuous_distributions.md` | 连续分布：Uniform/Exponential/Gamma/Normal/Weibull |
| `04_binomial_approximations.md` | Poisson approximation / Normal approximation / continuity correction |
| `05_poisson_process.md` | Poisson process, exponential waiting, gamma waiting, thinning/superposition |
| `06_transformations_1d_max_min.md` | 一维变量变换，CDF method，max/min order statistics |
| `07_jacobian_convolution.md` | 二维 Jacobian transformation，sum/convolution |
| `08_joint_marginal_conditional.md` | Joint PMF/PDF，marginal，conditional，independence |
| `09_conditional_expectation_total_laws.md` | Conditional expectation，全期望，全方差，random sum |
| `10_covariance_independence.md` | Covariance/correlation，uncorrelated vs independent |
| `11_reliability_hazard_weibull.md` | Reliability function，hazard，Weibull，series/parallel system |
| `12_mgf.md` | MGF 求矩、识别分布、独立和 |

## 建议打印顺序

1. `01` 到 `04`：基础分布和近似，最高频。
2. `06` 到 `08`：变量变换和 joint 大题，最容易丢 support。
3. `11`：reliability/hazard，公式相对固定。
4. `12`：MGF，适合做最后一页速查。

## 总原则

```text
Define RV -> identify distribution -> write support -> use correct sum/integral -> check boundary/support.
```

## 主要参考链接

- cheating_sheet: https://github.com/ghhufue/401_review/blob/main/cheating_sheet.md
- OpenStax discrete distributions: https://openstax.org/books/introductory-business-statistics/pages/4-formula-review
- OpenStax Poisson examples: https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution
- OpenStax normal approximation: https://openstax.org/books/statistics/pages/7-3-using-the-central-limit-theorem
- Penn State STAT 414 continuous RV: https://online.stat.psu.edu/stat414/Lesson14
- Penn State STAT 414 exponential/gamma: https://online.stat.psu.edu/stat414/Lesson15
- Penn State STAT 414 MGF: https://online.stat.psu.edu/stat414/Lesson09
- Penn State STAT 414 approximations: https://online.stat.psu.edu/stat414/Lesson28
- LibreTexts transformations: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/03%3A_Distributions/3.07%3A_Transformations_of_Random_Variables
- LibreTexts joint continuous: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.2%3A_Joint_Distributions_of_Continuous_Random_Variables
- LibreTexts joint discrete: https://stats.libretexts.org/Courses/Saint_Mary%27s_College_Notre_Dame/MATH_345__-_Probability_%28Kuter%29/5%3A_Probability_Distributions_for_Combinations_of_Random_Variables/5.1%3A_Joint_Distributions_of_Discrete_Random_Variables
- reliability docs equations: https://reliability.readthedocs.io/en/stable/Equations%20of%20supported%20distributions.html
