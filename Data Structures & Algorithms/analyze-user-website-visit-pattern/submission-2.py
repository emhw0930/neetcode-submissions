class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        events = sorted(zip(timestamp, username, website))   # bug 4

        visits = defaultdict(list)
        for _, user, site in events:
            visits[user].append(site)

        count = defaultdict(int)
        for sites in visits.values():
            for p in set(combinations(sites, 3)):   # bug 1 + bug 2
                count[p] += 1

        return list(max(sorted(count), key=count.get))   # bug 3