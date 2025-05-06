class SegmentTree:
	def __init__(self, data):
		self.data = data
		self.segtree = [0] * (4 * len(data))

	def build(self, node, start, end):
		if start == end:
			self.segtree[node] = self.data[start]
		else:
			mid = (start + end) // 2
			self.build(2 * node + 1, start, mid)
			self.build(2 * node + 2, mid + 1, end)
			self.segtree[node] = self.merge(
				self.segtree[2 * node + 1], 
				self.segtree[2 * node + 2]
			)

	def merge(self, node_left, node_right):
		return node_left + node_right

	def update(self, node, start, end, idx, value):
		if start == end:
			self.data[idx] = value
			self.segtree[node] = value
		else:
			mid = (start + end) // 2
			if idx <= mid:
				self.update(2*node+1, start, mid, idx, value)
			else:
				self.update(2*node+2, mid+1, end, idx, value)

			self.segtree[node] = self.merge(
				self.segtree[2*node+1], 
				self.segtree[2*node+2]
			)

	def query(self, node, start, end, L, R):
		if R < start or end < L:
			return 0

		if L == start and end == R:
			return self.segtree[node]

		mid = (start + end) // 2
		left_sum = self.query(
			2*node+1,
			start, mid,
			L, min(R, mid)
		)
		right_sum = self.query(
			2*node+2, 
			mid+1, end, 
			max(L, mid+1), R
		)

		return self.merge(left_sum, right_sum)

if __name__ == "__main__":
	data = [1, 3, 5, 7, 9, 11]
	seg_tree = SegmentTree(data)
	seg_tree.build(0, 0, len(data) - 1)

	print("Initial Segment Tree:", seg_tree.segtree)

	print("Query (1, 3):", seg_tree.query(0, 0, len(data) - 1, 1, 3))

	seg_tree.update(0, 0, len(data) - 1, 1, 10)
	print("After Update (index=1, value=10):", seg_tree.segtree)

	print("Query (1, 3):", seg_tree.query(0, 0, len(data) - 1, 1, 3))