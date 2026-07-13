def postorder_traversal(inorder, preorder):
    if not inorder or not preorder:
        return []
    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]

    return postorder_traversal(left_inorder, left_preorder) + \
           postorder_traversal(right_inorder, right_preorder) + \
           [root]

n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

result = postorder_traversal(inorder, preorder)
print(*result)
