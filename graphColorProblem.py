# Given an undirected graph represented as
#  an adjacency matrix and an integer k, 
#  write a function to determine whether each vertex in 
#  the graph can be colored such that no two adjacent vertices share 
#  the same color using at most k colors.

# Hàm kiểm tra xem màu 'c' có thể gán cho đỉnh 'node' hay không
def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

# Hàm đệ quy để thử tô màu từng đỉnh
def graph_coloring_util(graph, k, color, node):
    if node == len(graph):
        return True  # đã tô hết các đỉnh

    for c in range(1, k + 1):  # thử các màu từ 1 đến k
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, k, color, node + 1):
                return True
            color[node] = 0  # quay lui nếu không hợp lệ
    return False

# Hàm chính
def can_color_graph(graph, k):
    n = len(graph)
    color = [0] * n  # khởi tạo màu cho tất cả đỉnh là 0 (chưa tô)
    return graph_coloring_util(graph, k, color, 0)

# -----------------------------
# 📥 INPUT:
graph = [
    [0, 1, 1, 1],  # Đỉnh 0 nối với 1, 2, 3
    [1, 0, 1, 0],  # Đỉnh 1 nối với 0, 2
    [1, 1, 0, 1],  # Đỉnh 2 nối với 0, 1, 3
    [1, 0, 1, 0]   # Đỉnh 3 nối với 0, 2
]
k = 3  # Số màu cho phép

# 📤 OUTPUT:
print(can_color_graph(graph, k))  # 👉 True (vì có thể tô 3 màu thỏa mãn)
