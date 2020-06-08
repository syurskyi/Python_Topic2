class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        if n < 1:
            return
        self.nodes = {}
        self.count = n
        for i in range(n):
            self.nodes[i + 1] = i + 1

    def find(self, a):
        if self.nodes[a] == a:
            return a
        self.nodes[a] = self.find(self.nodes[a])
        return self.nodes[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.nodes[root_a] = root_b
            self.count -= 1

    """
    @return: An integer
    """
    def query(self):
        return self.count
