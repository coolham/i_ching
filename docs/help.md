# Help

## 


这些 .ts 文件是 Qt 语言工具使用的翻译源文件。它们包含了原始文本和对应的翻译。在实际使用中，您需要使用 Qt Linguist 工具来编辑这些文件，然后使用 lrelease 工具将它们编译成 .qm 文件，这些 .qm 文件才是应用程序在运行时实际加载的翻译文件。
要生成 .qm 文件，您可以使用以下命令：
这将在 translations 目录中生成 iching_en.qm 和 iching_zh.qm 文件

```
lrelease translations/iching_en.ts
lrelease translations/iching_zh.ts
```

这将在 translations 目录中生成 iching_en.qm 和 iching_zh.qm 文件。