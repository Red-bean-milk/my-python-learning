#|
配置scheme

1、下载
首先下载ChezScheme,地址https://github.com/cisco/ChezScheme/releases/tag/v10.3.0
双击下载的exe文件开始下载
默认下载到C:\Program Files\Chez Scheme 10.3.0

2、配置环境
win + R,输入sysdm.cpl
选择'高级'->'环境变量'->在'系统变量'中找到'Path'->双击打开->点击'新建'
输入scheme.exe所在地址,如果电脑是64位,输入C:\Program Files\Chez Scheme 10.3.0\bin\ta6nt
                      如果电脑是32位,输入C:\Program Files\Chez Scheme 10.3.0\bin\a6nt
点击'确定',环境配置完成

3、vscode配置
下载扩展：Code Runner(运行代码)，vscode-scheme(scheme代码高亮，可选)
vscode中打开'管理',找到'设置',搜索code runner Executor Map,打开'在settings.json中编辑'
添加
    "code-runner.runInTerminal": true,
    "code-runner.executorMapByFileExtension": {
    ".ss": "scheme"
    },
再把  "code-runner.executorMap":   中的"scheme": "csi -script"改成"scheme": "scheme"
重启vscode
新建test.ss文件,点击三角符号'运行',即可在终端交互式运行scheme代码
或者在文本框中输入好代码,选中需要运行的代码后点击三角符号'运行'(或按快捷键Ctrl+Alt+N),即可在终端看到运行结果
|#

(display (+ (* 3 5) (- 10 6)))
(exit)    ;退出交互式


(display
    (+ (* 3
        (+ (* 2 4)
            (+ 3 5)))
    (+ (- 10 7)
        6)))
(exit)     ;输出57