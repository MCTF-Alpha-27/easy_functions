# 介绍
从它的名字就可以看出，这就是一个简单但很实用的模块
<br/>每个命令都可以使用模块内的helpcmd()命令来帮助
<br/>模块内自带更新日志，使用log()命令来查看
# 迈出第一步
```
  import easy_functions as ef
  ef.help()
```
此操作将会显示命令列表和一些其他的帮助
<br/>如果你想直接获得纯净的命令列表，可以使用easy_functions.cmdlist
# 了解helpcmd()命令
这是本模块自带的解释功能，堪比命令提示符一样清晰的解释！
<br/>你可以很清楚地知道每一个命令的功能以及它们的语法
<br/>使用easy_functions.helpcmd('命令')解释单个命令
<br/>easy_functions.helpcmd('all')解释所有命令
# 最后
如果对本模块有建议一定要告诉我啊，我也是第一次写模块
<br/>请在GitHub反馈问题