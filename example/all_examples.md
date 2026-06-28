# ECE4010J Probability Example Pack

This is a plain-text version for the repository. It follows the scope of cheating_sheet.md and focuses on exam-style recognition, setup, and final-answer templates.

## 01. PMF, density, CDF, expectation, variance, LOTUS

Example 01.1: discrete normalization. X has p(x) = c(x + 1) for x = 0, 1, 2, 3. Sum of weights is 10, so c = 1/10. Probabilities are 0.1, 0.2, 0.3, 0.4. F(2) = 0.6. E[X] = 2. E[X squared] = 5. Var(X) = 1.

Example 01.2: continuous normalization. f(x) = c times x squared on 0 to 2. Integral gives 8c/3 = 1, so c = 3/8. CDF inside the interval is x cubed over 8. Probability from 1 to 2 is 7/8.

Example 01.3: CDF to density and median. If F(x) = x squared on 0 to 1, then density is 2x. Median m satisfies F(m) = 0.5, so m = square root of 0.5. CDF equal to 0.5 gives median, not necessarily mean.

Example 01.4: LOTUS. X takes 1, 2, 4 with probabilities 0.2, 0.5, 0.3. To find E[X squared + 3X], do not find a new distribution. Values are 4, 10, 28, so answer is 4 times 0.2 plus 10 times 0.5 plus 28 times 0.3 = 14.2.

## 02. Discrete distribution recognition

Example 02.1: Bernoulli. One yes-or-no test detects a fault with probability 0.03. X is Bernoulli with p = 0.03. Mean is 0.03 and variance is 0.03 times 0.97.

Example 02.2: Binomial. 20 independent chips each pass with probability 0.9. Number passing is Binomial with n = 20 and p = 0.9. P(X = 18) = C(20,18) times 0.9 power 18 times 0.1 power 2. Mean is 18 and variance is 1.8.

Example 02.3: Hypergeometric. 50 parts include 8 bad parts. Draw 5 without replacement. Probability of exactly 2 bad parts is C(8,2) C(42,3) divided by C(50,5).

Example 02.4: Geometric. Startup succeeds with probability 0.2. First success on trial 4 has probability 0.8 cubed times 0.2. Probability first success occurs after trial 5 is 0.8 power 5.

Example 02.5: Negative binomial. Probability that the third success occurs on trial 10 is C(9,2) times p cubed times (1-p) power 7.

Example 02.6: Poisson. Website receives average 4 requests per minute. Probability of exactly 6 next minute is exp(-4) times 4 power 6 divided by 6 factorial.

Example 02.7: Binomial versus Poisson. Fixed 100 requests with failure probability 0.01 gives Binomial(100, 0.01). Count of requests in one minute with average 80 gives Poisson(80).

Example 02.8: Binomial versus Hypergeometric. Drawing 4 from 20 balls with 5 red balls is Binomial if with replacement, Hypergeometric if without replacement.

## 03. Continuous distributions

Example 03.1: Uniform. X uniform on 0 to 10. P(3 to 8) is length ratio 5/10 = 0.5. Mean is 5. Variance is 100/12.

Example 03.2: Uniform conditional probability. P(X greater than 7 given X greater than 4) = length 7 to 10 divided by length 4 to 10 = 3/6 = 1/2.

Example 03.3: Exponential waiting. Failure rate is 0.5 per hour. Waiting time T is exponential rate 0.5. P(T greater than 3) = exp(-1.5).

Example 03.4: Memoryless. For exponential T, P(T greater than 7 given T greater than 4) = P(T greater than 3).

Example 03.5: Gamma waiting. Poisson process rate 2 per hour. Time to third event is Gamma with shape 3 and rate 2.

Example 03.6: Normal. X normal mean 75 standard deviation 10. P(X greater than 90) uses Z = 1.5, so probability is about 0.0668.

Example 03.7: Rate versus scale. Exponential with rate 4 has mean 1/4. Exponential with scale 4 has mean 4.

Example 03.8: Weibull survival. Scale 200, shape 2, survival at 100 is exp(-(100/200) squared) = exp(-0.25).

## 04. Binomial approximations

Example 04.1: Poisson approximation. Binomial n = 1000, p = 0.002 has lambda = 2. Approximate P(X = 3) by exp(-2) times 2 cubed divided by 3 factorial.

Example 04.2: Normal approximation. Binomial n = 100, p = 0.6 has mean 60 and variance 24. P(X at least 70) becomes normal probability above 69.5 after continuity correction.

Example 04.3: Continuity correction. P(45 at most X at most 55) becomes normal interval 44.5 to 55.5.

Example 04.4: When not to use normal. Binomial(20, 0.02) has np = 0.4, too small. Use exact binomial or Poisson approximation.

## 05. Poisson process

Example 05.1: Count in interval. Calls arrive at rate 3 per hour. In 2 hours, lambda is 6. P(exactly 5) = exp(-6) times 6 power 5 divided by 5 factorial.

Example 05.2: At least one event. Rate 4 per hour, 30 minutes gives lambda 2. P(no event) = exp(-2), P(at least one) = 1 - exp(-2).

Example 05.3: Waiting to first event. Rate 4 per hour. P(first event after 0.5 hour) = exp(-2).

Example 05.4: Waiting to third event. Third event before 1 hour means at least 3 events in first hour. Use 1 minus Poisson probabilities for 0, 1, and 2.

Example 05.5: Thinning. Poisson arrivals rate 10 per hour. Type A probability 0.3. Type A process rate is 3 per hour.

Example 05.6: Superposition. Independent rates 2 and 5 combine to rate 7.

## 06. One-dimensional transformations, max and min

Example 06.1: Monotone transformation. X uniform on 0 to 1, Y = X squared. CDF of Y is square root of y on 0 to 1. Density is 1 divided by 2 square root y.

Example 06.2: Non-monotone transformation. X uniform on -1 to 1, Y = X squared. CDF of Y is square root of y because interval from negative square root y to positive square root y has length 2 square root y over total length 2.

Example 06.3: Linear scaling. X exponential rate 2, Y = 3X. Density of Y is (2/3) exp(-2y/3), y nonnegative.

Example 06.4: Maximum. If Xi are iid with CDF F and M is max, then CDF of M is F(m) power n.

Example 06.5: Minimum. If L is min, survival of L is survival of X power n, so CDF is 1 minus that.

## 07. Jacobian transformation and convolution

Example 07.1: U = X + Y and V = X - Y. Inverse is x = (u+v)/2 and y = (u-v)/2. Absolute Jacobian of inverse is 1/2. New joint density is old joint density at inverse point times 1/2, with transformed support.

Example 07.2: U = X/Y and V = Y. Inverse is x = uv and y = v. Absolute Jacobian is absolute value of v.

Example 07.3: Sum convolution. For independent X and Y, density of Z = X+Y is integral of f_X(x) f_Y(z-x) over valid x values.

Example 07.4: Sum of two uniform(0,1). Density of Z is z from 0 to 1 and 2-z from 1 to 2.

Example 07.5: Sum of two iid exponential rate lambda variables is Gamma with shape 2 and rate lambda.

## 08. Joint, marginal, conditional, independence

Example 08.1: Joint table. If p(0,0)=0.2, p(0,1)=0.1, p(1,0)=0.3, p(1,1)=0.4, then P(X=1)=0.7, P(Y=1)=0.5, P(X=1 given Y=1)=0.8. Not independent because 0.4 is not 0.7 times 0.5.

Example 08.2: Joint density f(x,y)=2 on 0 < y < x < 1. Marginal of X is 2x because y ranges from 0 to x.

Example 08.3: Same region. Conditional density of Y given X=x is 1/x on 0 to x, so Y given X=x is uniform on 0 to x.

Example 08.4: Same region. E[Y given X=x] = x/2.

Example 08.5: Independence check. f(x,y)=6xy on unit square. Marginals are 3x and 3y, product is 9xy, not 6xy, so not independent.

Example 08.6: Unit square area probability. P(X+Y less than 1) is lower-left triangle area 1/2.

## 09. Conditional expectation and total laws

Example 09.1: Conditional expectation from table. If P(Y=1)=0.5 and conditional probabilities of X=0 and X=2 given Y=1 are 0.2 and 0.8, then E[X given Y=1] = 1.6.

Example 09.2: Total expectation. Line A probability 0.7 has mean defects 2. Line B probability 0.3 has mean defects 5. Overall mean is 2.9.

Example 09.3: Total variance. Var(X)=E[Var(X|L)] + Var(E[X|L]). If conditional variances are 1 and 4, first part is 1.9. Conditional means are 2 and 5 with overall mean 2.9, second part is 1.89. Total is 3.79.

Example 09.4: Random sum. N is Poisson mean 10. Each order amount has mean 20. Total expected amount is 20 times E[N] = 200.

Example 09.5: Exponential residual life. For exponential rate lambda, expected remaining life after already surviving s is 1/lambda. Expected total lifetime given survival to s is s + 1/lambda.

## 10. Covariance, correlation, independence

Example 10.1: From table. E[X]=0.7, E[Y]=0.5, E[XY]=0.4. Covariance is 0.4 - 0.7 times 0.5 = 0.05.

Example 10.2: Independent variables. If E[X]=3 and E[Y]=4, then E[XY]=12 and covariance is 0.

Example 10.3: Zero covariance but not independent. X uniform on -1 to 1 and Y = X squared. Covariance is 0 by symmetry, but Y is determined by X, so not independent.

Example 10.4: Linear combination variance. Var(3X - 2Y) = 9 Var(X) + 4 Var(Y) - 12 Cov(X,Y). With Var(X)=4, Var(Y)=9, Cov=2, result is 48.

Example 10.5: Correlation. Var(X)=4, Var(Y)=9, Cov=3. Standard deviations are 2 and 3, so correlation is 1/2.

Example 10.6: Joint normal. For jointly normal variables, zero correlation implies independence. For general variables, it does not.

## 11. Reliability, hazard, Weibull

Example 11.1: Reliability. If F(t)=1-exp(-0.01t), then R(t)=exp(-0.01t), so R(100)=exp(-1).

Example 11.2: Exponential hazard. T exponential rate 0.02 has density 0.02 exp(-0.02t), reliability exp(-0.02t), and hazard 0.02.

Example 11.3: Series system. Independent exponential rates 0.01 and 0.02 in series give system reliability exp(-0.03t). At t=100, this is exp(-3).

Example 11.4: Parallel system. Reliability is 1 - (1-R1)(1-R2). At t=100, use 1 - (1-exp(-1))(1-exp(-2)).

Example 11.5: Weibull hazard. Shape beta less than 1 means decreasing hazard. Beta equal to 1 means constant hazard. Beta greater than 1 means increasing hazard.

Example 11.6: Annual to daily failure probability. If yearly failure probability is 10 percent, yearly survival is 0.90. Daily p satisfies (1-p)^365 = 0.90. Therefore p = 1 - 0.90^(1/365), about 0.0002886.

Example 11.7: Competing risks. Exponential rates 0.01 and 0.02. Minimum is exponential rate 0.03. Probability A fails first is 0.01/(0.01+0.02)=1/3.

Example 11.8: Mean from survival. If R(t)=exp(-0.5t), mean lifetime is integral of survival, which equals 2.

## 12. MGF

Example 12.1: From PMF. If X takes 0,1,2 with probabilities 0.2,0.5,0.3, M(t)=0.2 + 0.5 exp(t) + 0.3 exp(2t).

Example 12.2: Mean and variance from MGF. M prime at 0 gives mean. M second derivative at 0 gives E[X squared]. Variance is M second derivative at 0 minus mean squared.

Example 12.3: Identify binomial. M(t)=(3/4 + (1/4)exp(t))^20 is Binomial with n=20 and p=1/4.

Example 12.4: Independent Poisson sum. Poisson(3) plus independent Poisson(5) is Poisson(8).

Example 12.5: Normal linear combination. X normal mean 1 variance 4, Y normal mean 2 variance 9, independent. Z=2X-3Y is normal with mean -4 and variance 97.

Example 12.6: Exponential sum. Sum of k iid exponential rate lambda variables is Gamma with shape k and rate lambda.

Example 12.7: MGF coefficients. If M(t)=0.1 exp(t)+0.2 exp(2t)+0.3 exp(3t)+0.4 exp(4t), then probabilities at 1,2,3,4 are 0.1,0.2,0.3,0.4.

Example 12.8: If MGF does not exist, still use direct definitions of expectation and variance.

## Final exam checklist

1. Fixed n independent trials: Binomial.
2. Without replacement: Hypergeometric.
3. First success: Geometric.
4. r-th success: Negative binomial.
5. Count in fixed interval: Poisson.
6. Waiting to first Poisson event: Exponential.
7. Waiting to k-th Poisson event: Gamma.
8. Continuous probability: use CDF difference or integrate density.
9. Transformation: write inverse and support.
10. Joint distribution: marginalize first, then condition.
11. Reliability: R(t)=1-F(t), hazard=density/reliability.
12. MGF: derivatives give moments; independent sums multiply MGFs.
