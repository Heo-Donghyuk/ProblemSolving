SELECT INFO.ITEM_ID AS ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO INFO LEFT JOIN ITEM_TREE TREE ON INFO.ITEM_ID = TREE.PARENT_ITEM_ID
WHERE TREE.ITEM_ID IS NULL
ORDER BY ITEM_ID DESC