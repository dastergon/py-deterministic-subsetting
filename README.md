# A Subset Selection Algorithm: Deterministic Subsetting

Source: https://landing.google.com/sre/book/chapters/load-balancing-datacenter.html

**Subsetting**: limiting the pool of potential backend tasks with which a client task interacts.

What the algorithm does according to the [Site Reliability Engineering](https://landing.google.com/sre/book/chapters/load-balancing-datacenter.html) book:
```
We divide client tasks into "rounds," where round i consists of subset_count consecutive client tasks, starting at task subset_count × i, and subset_count is the number of subsets (i.e., the number of backend tasks divided by the desired subset size). Within each round, each backend is assigned to exactly one client (except possibly the last round, which may not contain enough clients, so some backends may not be assigned).
```

### How to use
```python
from subset import Subset

def main():
    backends = []
    for i in xrange(12):
        backends.append(i)

    result = {}
    subset_size = 3
    for client_id in xrange(10):
        result[client_id] = Subset(backends=backends, client_id=client_id, subset_size=subset_size)

    for client_id, backend in result.iteritems():
        print("{}: {}".format(client_id, backend))

if __name__ == "__main__":
    main()

```
