

class QuickFind(object):
    """ Structure that maintains list for connected components.
        Each index of the id_list represents one object and value on this index
        specifies to which connected component this object belongs
    """

    def __init__(self, N: int):
        """
        initialization that assigns each object so its own connected component
        complexity O(N)

        :param N: number of objects that we can connect
        """
        self.id_list = list(range(N))

    def connected(self, p: int, q: int) -> bool:
        """
        Checks if two objects are in the same connected component
        complexity O(1)

        :param p: id of first object
        :param q: id of second object
        :return: False if the two object are not in the same connected component, otherwise True
        """
        return self.id_list[p] == self.id_list[q]

    def union(self, p: int, q: int):
        """
        Connects objects p and q into one connected component
        complexity O(N) ...has to move all the components from 'q' group to 'p' group

        :param p: id of first object
        :param q: id of second object
        """
        p_group = self.id_list[p]
        q_group = self.id_list[q]
        if p_group != q_group:
            for i in range(len(self.id_list)):
                if self.id_list[i] == q_group:
                    self.id_list[i] = p_group
