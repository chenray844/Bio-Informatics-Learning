class Trie(object):
    def __init__(self):
        self.root = {}
        self.index = 1

    def _insert_helper(self, word, ptr, node):
        if 'id' not in node:
            node['id'] = self.index
            self.index += 1
        if ptr >= len(word):
            # last node.
            return True
        else:
            curr_character = word[ptr]
            if curr_character in node:
                next_node = node[curr_character][0]
                if ptr == len(word) - 1:
                    node[curr_character] = next_node, True
                return self._insert_helper(word, ptr + 1, node[curr_character][0])
            else:
                if ptr == len(word) - 1:
                    node[curr_character] = {}, True
                else:
                    node[curr_character] = {}, False

                return self._insert_helper(word, ptr + 1, node[curr_character][0])


    def _fill_adjacency_list(self, node, answer):
        if len(node) > 0:
            assert ('id' in node)
            current_id = node['id']
            for character in node:
                if character != 'id':
                    next_node, leaf = node[character]
                    next_node_id = next_node['id']
                    if next_node_id < current_id:
                        current_id, next_node_id = next_node_id, current_id
                    answer.add((current_id, next_node_id, character))
                    self._fill_adjacency_list(next_node, answer)

    def get_adjacency(self):
        answer = set()
        self._fill_adjacency_list(self.root, answer)
        return answer


    def insert(self, word):
        try:
            return self._insert_helper(word, 0, self.root)
        except:
            return False


trie = Trie()
f = open('data/Counting_DNA_Nucleotides.dat', 'r')
for line in f:
    line = line.rstrip()
    trie.insert(line)
f.close()
answer = trie.get_adjacency()

f = open('out/out.dat', 'w')
for ans in answer:
    print ans[0], ans[1], ans[2]
    txt = '%s %s %s \n' % tuple(ans)
    f.write(txt)
f.close()