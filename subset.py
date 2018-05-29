"""
A Subset Selection Algorithm: Deterministic Subsetting

The following algorithm is mentioned at the Site Reliability Engineering book.

Source: https://landing.google.com/sre/book/chapters/load-balancing-datacenter.html
"""

import random

def Subset(backends, client_id, subset_size):
    """We divide client tasks into "rounds," where round i consists of
    subset_count consecutive client tasks, starting at task subset_count x i,
    and subset_count is the number of subsets (i.e., the number of backend tasks
    divided by the desired subset size). Within each round, each backend is
    assigned to exactly one client (except possibly the last round,
    which may not contain enough clients, so some backends may not be assigned).
    """
    subset_count = len(backends) / subset_size

    # Group clients into rounds; each round uses the same shuffled list:
    round = client_id / subset_count
    random.seed(round)
    random.shuffle(backends)

    # The subset id corresponding to the current client:
    subset_id = client_id % subset_count

    start = subset_id * subset_size
    return backends[start:start + subset_size]
