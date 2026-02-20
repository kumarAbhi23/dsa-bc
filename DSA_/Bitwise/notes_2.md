Almost 👍 — but the correct idea is:

> **Bitwise OR (`|`) is used to *set* a bit to 1,**

Let’s make it clear.

---

## 🔹 What does OR (`|`) do?

Bitwise OR compares each bit:

| A | B | A | B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 1     |

So **if either bit is 1 → result is 1**.
But **if mask is 0 then result will not change **

---

## 🔹 Using OR to *set* a bit

To turn ON a specific bit, we OR the number with a mask.

```python
n = 10      # 1010
mask = 1<<1  # 0010  (bit position 1)

n = n | mask
print(n)   # 1010 | 0010 = 1010 (no change, already 1)
```

Another example:

```python
n = 8       # 1000
mask = 1<<1 # 0010

n = n | mask
print(n)    # 1010 (10)
```

Here:

* We **set bit-1 to 1**
* We did **not add 2**, we just forced that bit ON.

---

## 🔹 Difference: OR vs Add

| Operation | Example | Result             |    |                      |
| --------- | ------- | ------------------ | -- | -------------------- |
| `n + 2`   | `8 + 2` | `10` (normal math) |    |                      |
| `n        | 2`      | `8                 | 2` | `10` (bit forced ON) |

But:

```python
n = 10  # 1010
n + 2 = 12  # 1100
n | 2 = 10  # 1010 (no change!)
```

So OR **does not mean add** — it means **set bits**.

---

## 🔹 Summary

| Operator | Use                        |                |
| -------- | -------------------------- | -------------- |
| `        | ` OR                       | Set a bit to 1 |
| `&` AND  | Check a bit                |                |
| `^` XOR  | Toggle a bit               |                |
| `~` NOT  | Flip bits                  |                |
| `<<`     | Shift left (multiply by 2) |                |
| `>>`     | Shift right (divide by 2)  |                |

---

If you want, I can make you a **bitmask cheat sheet in one page** 👨‍💻🔥
