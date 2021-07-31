from subset import Subset
import copy

def main():
    backends = []
    for i in xrange(12):
        backends.append(i)

    result = {}
    subset_size = 3
    for client_id in xrange(10):
        result[client_id] = Subset(backends=copy.copy(backends), client_id=client_id, subset_size=subset_size)

    for client_id, backend in result.iteritems():
        print("{}: {}".format(client_id, backend))

if __name__ == "__main__":
    main()
