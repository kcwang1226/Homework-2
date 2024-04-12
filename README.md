# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

Profitable Path: 
```
tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB
```

The amountIn, amountOut value for Each Swap:
```
tokenB -> tokenA: (amount in: 5, amount out: 5.655321988655323)
tokenA -> tokenC: (amount in: 5.655321988655323, amount out: 2.372138936383089)
tokenC -> tokenE: (amount in: 2.372138936383089, amount out: 1.530137136963617)
tokenE -> tokenD: (amount in: 1.530137136963617, amount out: 3.4507414486197083)
tokenD -> tokenC: (amount in: 3.4507414486197083, amount out: 6.684525579572587)
tokenC -> tokenB: (amount in: 6.684525579572587, amount out: 22.497221806974142)
```

My final Reward:
```
22.497221806974142 tokenB
```

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage in AMMs refers to the difference between the expected price of a trade and the price at which the trade is executed. This occurs due to changes in a token's supply and demand on the liquidity pool between the time a transaction is sent and when it is executed.

Uniswap V2 addresses slippage through the use of a constant product formula (x * y = k), where x and y are the reserve amounts of two tokens in the liquidity pool, and k is a constant. When a trade is executed, the amounts of the tokens change, but the product of their amounts must remain the same. This mechanism naturally limits the amount by which the actual execution price can deviate from the expected price, as larger orders move the price more significantly.

For example, if you swap TokenA for TokenB in a pool with reserves x of TokenA and y of TokenB, the output amount dy of TokenB for an input amount dx of TokenA is determined by the formula:
$dy=\frac{y*dx}{x+dx}$

This formula ensures that the product (x * y = k) remains constant, thus providing predictability and limiting slippage.
## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

In Uniswap V2, upon the initial minting of liquidity, a minimum liquidity amount (usually 1000 liquidity tokens) is permanently locked in the pool. This is done to prevent someone from manipulating the pool with extremely small amounts of liquidity, which could lead to disproportionate control over the price as calculated by the constant product formula. By locking away this small amount, it ensures there's always some base level of liquidity, thus protecting against potential manipulation or rounding errors at very low liquidity levels.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

For subsequent liquidity deposits (after the initial setup), Uniswap V2 uses a specific formula to determine how much liquidity tokens a depositor should receive. This formula ensures that the share of liquidity tokens received is proportional to the amount of liquidity the depositor adds relative to the current pool size.

The formula to calculate liquidity 
L added by a new deposit of tokens dx and dy is: L=min(dx*total_liquidity/x,dy*total_liquidity/y)

This design maintains the ratio of reserves in the pool, ensuring that the value is distributed fairly according to each provider's contribution and prevents dilution of existing liquidity providers' shares.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack in the context of AMMs like Uniswap involves a malicious trader placing a trade right before and right after a victim's trade. The attacker sees the victim's transaction in the public pool (mempool), and if the victim's transaction is large enough to move the market, the attacker places one transaction immediately before the victim's trade to drive the price up (or down), and another right after to sell at the new higher price (or buy back cheaper).

Impact on the Victim: This results in the victim receiving a worse price than expected, as the first attack transaction shifted the market unfavorably. The victim suffers from increased slippage and potentially substantial financial loss, while the attacker profits from this manipulation.

## Bonus
The most profitable path among all possible swap path
```
tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB
```
Profit:
```
22.497221806974142 tokenB
```
Corresponding Python script: Is in Arbitrage.py
