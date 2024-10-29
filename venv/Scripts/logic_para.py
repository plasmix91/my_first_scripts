from pyDatalog import pyDatalog

# Declare variables
pyDatalog.clear()

# Define facts for family relationships
+pyDatalog.assert_fact('parent', 'Alice', 'Bob')
+pyDatalog.assert_fact('parent', 'Alice', 'Carol')
+pyDatalog.assert_fact('parent', 'Bob', 'David')
+pyDatalog.assert_fact('parent', 'Carol', 'Eva')

# Define rules for relationships
# A is a sibling of B if they share the same parent and are not the same person
pyDatalog.create_terms('A, B, C, sibling, parent')
sibling(A, B) <= (parent(C, A)) & (parent(C, B)) & (A != B)

# A is a grandparent of B if A is a parent of C and C is a parent of B
pyDatalog.create_terms('grandparent')
grandparent(A, B) <= (parent(A, C)) & (parent(C, B))

# Queries
# Who are the siblings of Bob?
print("Siblings of Bob:", sibling('Bob', B))

# Who are the grandparents of Eva?
print("Grandparents of Eva:", grandparent(A, 'Eva'))
