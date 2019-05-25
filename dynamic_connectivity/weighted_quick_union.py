

class WeightedQuickUnion(object):
    """ Structure that maintains list for connected components.
        Each index of the id_list represents one object and value on this index
        points to another object from the same group. If the value on the index points to itself
        it means that this object is the root of the group.
        Each group is therefore represented as a tree.
        Another list, size_list, keeps track of heights of the trees to ensure the trees are stacked
        in such a way that the max height of tree is limited to log N
    """

    def __init__(self, N: int):
        """
        initialization that assigns each object so its own connected component
        complexity O(N)

        :param N: number of objects that we can connect
        """
        self.id_list = list(range(N))
        self.size_list = [1] * N

    def root(self, p: int) -> int:
        """
        finds root of a given object and compresses the path by half.
        The compression is done by making each object point to its grandparent while searching for the root
        complexity O(log N) ...log N is max distance between the object and its root

        :param p: an object for which we want to find a root
        :return: root of the group the object p belongs to
        """
        while p != self.id_list[p]:
            self.id_list[p] = self.id_list[self.id_list[p]]
            p = self.id_list[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        """
        Checks if two objects are in the same connected component by checking their roots
        complexity O(log N)

        :param p: id of first object
        :param q: id of second object
        :return: False if the two object are not in the same connected component, otherwise True
        """
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        """
        Connects objects p and q into one connected component
        complexity O(log N) has to find roots

        :param p: id of first object
        :param q: id of second object
        """
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return
        if self.size_list[p_root] > self.size_list[q_root]:
            self.id_list[q_root] = p_root
            self.size_list[p_root] += self.size_list[q_root]
        else:
            self.id_list[p_root] = q_root
            self.size_list[p_root] += self.size_list[q_root]
