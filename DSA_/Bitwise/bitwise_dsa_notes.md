 **`bitwise_dsa_notes.md`**.

---

# 🧠 Bitwise Operators – DSA Quick Revision Notes

Bitwise operations work at the **binary level** and are extremely useful in **DSA, competitive programming, system design, and optimizations**. This file contains definitions, examples, common tricks, pitfalls, and practice problems with short hints — everything you need for a fast revision.

---

## Table of Contents

1. [Check Last Bit (Odd / Even)](#1-check-last-bit-odd--even)
2. [Right Shift `>>` and Left Shift `<<`](#2-right-shift--and-left-shift-)
3. [Set / Clear / Toggle / Check Bits (Bitmasking)](#3-set--clear--toggle--check-bits-bitmasking)
4. [Common Bit Tricks & Micro-optimizations](#4-common-bit-tricks--micro-optimizations)
5. [XOR Patterns & Single-number Problems](#5-xor-patterns--single-number-problems)
6. [Swap Without Temp (XOR swap) — Example](#6-swap-without-temp-xor-swap----example)
7. [State Compression & Bitmask DP — Example](#7-state-compression--bitmask-dp----example)
8. [Language Differences / Signedness / Pitfalls](#8-language-differences--signedness--pitfalls)
9. [Complexity & Why use bit ops?](#9-complexity--why-use-bit-ops)
10. [Quick Interview Tips & Common Questions](#10-quick-interview-tips--common-questions)
11. [Practice Problems (with hints / brief solutions)](#11-practice-problems-with-hints--brief-solutions)

---

## 1. Check Last Bit (Odd / Even)

```python
bit = n & 1  # get last bit
```

* `1` → odd, `0` → even
* Remove last bit (shift right):

```python
n >>= 1  # n = n >> 1
```

**Example**

```python
n = 13      # binary 1101
print(n & 1)  # 1 (odd)
n >>= 1
print(n)      # 6  (binary 110)
```

Used for: parity checks, iterating bits, processing binary digits.

---

## 2. Right Shift `>>` and Left Shift `<<`

### Right shift

```text
n >> x   # drop x least significant bits
```

* `n >> x` ≈ `floor(n / 2^x)` for non-negative integers.

**Example**

```python
n = 10       # 1010
print(n >> 1)  # 5
print(n >> 2)  # 2
```

### Left shift

```text
n << x   # add x zero bits on the right
```

* `n << x` = `n * 2^x`.

**Example**

```python
n = 3       # 11
print(n << 1)  # 6  (110)
print(n << 3)  # 24 (11000)
```

**Use**: fast multiply/divide by powers of two, building binary numbers.

---

## 3. Set / Clear / Toggle / Check Bits (Bitmasking)

```python
mask = 1 << k   # mask with kth bit = 1 (0-indexed LSB)
```

* **Set kth bit**: `n | mask`
* **Clear kth bit**: `n & ~mask`
* **Toggle kth bit**: `n ^ mask`
* **Check kth bit**: `(n & mask) != 0`

**Examples**

```python
n = 0b1010      # 10
k = 1
mask = 1 << k   # 0b0010

# Set
print(bin(n | mask))   # 0b1010 (already set)

# Clear
print(bin(n & ~mask))  # 0b1000

# Toggle
print(bin(n ^ mask))   # 0b1000

# Check
print((n & mask) != 0) # True
```

**Practical uses**: permission flags, representing multiple boolean options in an int, subset generation.

---

## 4. Common Bit Tricks & Micro-optimizations

* **Remove last set bit**: `n & (n - 1)`

  * Example: `12 (1100) & 11 (1011) = 8 (1000)`
* **Check power of two**: `n > 0 and (n & (n - 1)) == 0`
* **Get lowest set bit**: `n & -n` (two's complement)
* **Count set bits (Brian Kernighan)**:

```python
count = 0
while n:
    n &= (n - 1)
    count += 1
```

* **Turn off rightmost set bit**: `n & (n - 1)`
* **Turn on rightmost zero bit**: `n | (n + 1)` (useful in some algorithms)
* **Build number from bits**:

```python
x = 0
for bit in bits:      # bit is 0 or 1
    x = (x << 1) | bit
```

**Example - count bits**

```python
def popcount(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt
```

---

## 5. XOR Patterns & Single-number Problems

Properties:

* `a ^ a = 0`
* `a ^ 0 = a`
* XOR is commutative and associative.

**Single unique element (all appear twice except one)**

```python
ans = 0
for x in nums:
    ans ^= x
# ans now holds the unique number
```

**Two unique elements (others appear twice)** — approach:

1. XOR all numbers -> `xor_all = a ^ b` (a,b are unique)
2. Find any set bit in `xor_all` (e.g. `d = xor_all & -xor_all`)
3. Partition numbers by that bit and XOR each partition to get a and b.

**Missing number (0..n)**:

* XOR approach or sum/formula approach.

**Example - two uniques**

```python
xor_all = 0
for x in nums: xor_all ^= x
mask = xor_all & -xor_all
a = b = 0
for x in nums:
    if x & mask: a ^= x
    else: b ^= x
# a and b are the two unique numbers
```

---

## 6. Swap Without Temp (XOR swap) — Example

```python
a = 5  # 0101
b = 9  # 1001

a = a ^ b
b = a ^ b
a = a ^ b
```

**After:**

* `a == 9`, `b == 5`

**Note**: In modern languages and CPUs, `temp` swap is usually faster and clearer; XOR swap is a neat trick but rarely practical.

---

## 7. State Compression & Bitmask DP — Example

**Problem**: Count number of valid subsets for `n <= 20` with some constraints.

Represent the chosen subset as a bitmask `mask` (0..2^n-1). Iterate subsets:

```python
for mask in range(1 << n):
    # check or compute properties using bit operations
```

**Example — subset generation**

```python
n = 3
for mask in range(1 << n):
    subset = []
    for i in range(n):
        if mask & (1 << i):
            subset.append(i)
    print(mask, subset)
```

**DP with bitmask (TSP sketch)**:
Let `dp[mask][i]` = best cost to visit nodes in `mask` and end at `i`. Transition uses `(mask ^ (1<<i))` etc.

---

## 8. Language Differences / Signedness / Pitfalls

* **Right shift of negative numbers**:

  * In Python, `>>` on negative numbers does arithmetic shift (keeps sign).
  * In C/C++ behavior for negative right shift is implementation-defined historically; usually arithmetic shift (fills sign bit).
  * In Java, `>>` is arithmetic (sign-propagating), `>>>` is logical (zero-fill).
* **Integer bitwidth matters** in C/C++/Java (32-bit, 64-bit). Python ints are arbitrary precision.
* **Use parentheses** to avoid precedence bugs (e.g., `n & (1 << k)`).
* **Beware overflow** when using `1 << k` for large `k` in fixed-width languages.

---

## 9. Complexity & Why use bit ops?

* Bit operations run in constant time on machine words — extremely fast.
* They save memory by packing many booleans into one integer.
* Many DP and combinatorial algorithms become feasible via state compression.
* Complexity of loops using bit tricks is still measured in usual terms (e.g., iterating `1<<n` masks is O(2^n)).

---

## 10. Quick Interview Tips & Common Questions

* Always clarify bit-indexing (0-indexed LSB vs MSB).
* When using `1<<k`, ensure `k` is within word-size.
* For problems saying “all numbers appear twice except two”, think XOR partition trick.
* For counting bits, mention Brian Kernighan's method (faster than checking every bit).
* Mention signed vs unsigned semantics when asked about shifting negatives.
* If asked to optimize, show bitmask DP or using `n & (n-1)` to speed up bit counts.

---

## 11. Practice Problems (with hints / brief solutions)

1. **Single Number** (LeetCode 136)

   * *Given array where every element appears twice except one, find that single one.*
   * **Hint**: XOR all elements.
   * **Solution**: `ans ^= x` loop.

2. **Single Number II** (LeetCode 137)

   * *Every element appears thrice except one.*
   * **Hint**: use bit counts for every bit position (mod 3).

3. **Find two unique numbers**

   * *Array where exactly two numbers appear once, others twice.*
   * **Hint**: XOR total, find distinguishing bit, partition, XOR each partition.

4. **Count set bits from 1..n**

   * **Hint**: use patterns per bit position (or DP using highest power of two).

5. **Subsets generation**

   * *Generate all subsets of array.*
   * **Hint**: iterate `mask` from `0` to `(1<<n)-1` and collect elements where `(mask & (1<<i))`.

6. **DP with bitmask — TSP small `n`**

   * *n <= 20 classical TSP*
   * **Hint**: `dp[mask][i]` transitions from `dp[mask ^ (1<<i)][j]`.

7. **Next permutation using bit operations?** (challenge)

   * *Not typical — but use bit patterns if numbers are small / limited domain.*

---

## Extra Examples: Full Code Snippets

### Example: Count set bits (fast)

```python
def popcount(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt

print(popcount(29))  # 29 = 11101 -> 4
```

### Example: Two unique numbers

```python
def two_single_numbers(nums):
    xor_all = 0
    for x in nums: xor_all ^= x
    mask = xor_all & -xor_all
    a = b = 0
    for x in nums:
        if x & mask:
            a ^= x
        else:
            b ^= x
    return a, b
```

### Example: Generate subsets

```python
def subsets(arr):
    n = len(arr)
    res = []
    for mask in range(1 << n):
        s = []
        for i in range(n):
            if mask & (1 << i):
                s.append(arr[i])
        res.append(s)
    return res
```

---

## Summary — Core Takeaways

* `n & 1` — last bit, odd/even.
* `n >> x` — divide by `2^x` (floor for non-negative).
* `n << x` — multiply by `2^x`.
* `1 << k` — build masks; use for flags and state compression.
* `n & (n-1)` — remove lowest set bit; helpful for popcount and power-of-two checks.
* XOR is a powerful tool for parity and cancellation problems.
* Bitmask DP makes exponential problems tractable for small `n` by encoding states compactly.

---

If you want, I can:

* produce a printable PDF version, or
* generate a condensed one-page cheat-sheet image, or
* add solution walkthroughs for the practice problems (step-by-step).
