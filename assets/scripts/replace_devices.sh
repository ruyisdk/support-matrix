#!/bin/bash

FOLDER_PATH="../.."

# 递归处理文件
find "$FOLDER_PATH" -type f | while read -r file; do
    if grep -q "/dev/mmcblk[0-9]\|/dev/sd[a-z]" "$file"; then
        echo "处理文件: $file"
        sed -i 's/\/dev\/mmcblk[0-9]/\/dev\/mmcblkX/g; s/\/dev\/sd[a-z]/\/dev\/sdX/g' "$file"
    fi
done

echo "完成！"