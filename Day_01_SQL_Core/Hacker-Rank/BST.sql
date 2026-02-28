You are given a table, BST, containing two columns: N and P,
where N represents the value of a node in Binary Tree, and P is the parent of N.


Write a query to find the node type of Binary Tree ordered by the value of the node.
Output one of the following for each node:
Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.

Sample Input

BST table:
+----+------+
| N  | P    |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
| 6  | 3    |
+----+------+
Sample Output
+----+-------+
| N  | Type  |

+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Inner |
| 4  | Leaf  |
| 5  | Leaf  |
| 6  | Leaf  |


------------------------------------------------------------------------------------------
Explanation:
Node 1 is the root node because it has no parent (P is null).
Nodes 2 and 3 are inner nodes because they have a parent and at least one child
Nodes 4, 5, and 6 are leaf nodes because they have a parent and no children.
To determine the type of each node in the Binary Tree, we can use a SQL query that checks for the presence of parent and child nodes. Here's how you can write the query:

-------------------------------------------------------------------------------------------
---------------------------- Query to find the node type of Binary Tree: ------------------


SET NULL "NULL";
SELECT 
    N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS NodeType
FROM BST
ORDER BY N;
exit;