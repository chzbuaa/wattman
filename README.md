# this is the wattman's interview question

要求：
1. 写一个linux shell脚本统计指定目录下文件名满足' *_gt.json*'要求的文件数量，需要注意的是指定目录下的文件夹层数可能不一定。
2. 将完成后的代码上传到github中（可以上传到其它git仓库）。

# 在linux 终端命令行执行：python3 /home/hongzhi/PycharmProjects/pythonProject/main.py /mnt/hgfs/ubuntushare _gt.json

其中   home/hongzhi/PycharmProjects/pythonProject/main.py     是脚本main.py文件的目录路径
\其中   /mnt/hgfs/ubuntushare  是指定目录
\其中  _gt.json  是搜索匹配的关键字

最终linux终端打印效果：
/mnt/hgfs/ubuntushare/123/123_gt.json
/mnt/hgfs/ubuntushare/123/321/456_gt.json
/mnt/hgfs/ubuntushare/_gt.json
搜索出来的文件数量为： 3

