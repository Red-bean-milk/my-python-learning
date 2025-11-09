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

;if语句标准格式: (if <predicate> <consequent> <alternative>)  # 见下方函数abs
(display (>= 2 1))  ;  返回#t
(exit)

;===========3.2.2定义===================
(define pi 3.14)   ; define 赋值
(display (* pi 2))
(exit)



(define (square x) (* x x))  ; define 定义函数 标准格式:(define (<name> <formal parameters>) <body>)

(display (square 10))
(newline)                    ; 换行
(display (square (square 3)))
(exit)


(define (average x y)
    (/ (+ x y) 2))
(display (average 1 3))
(exit)  


(define (abs x)
    (if (< x 0)
        (-x)
        x))

; lambda定义函数
; 标准格式: (lambda (<formal-parameters>) <body>)

(define (plus4_1 x) (+ x 4))
(define plus4_2 (lambda (x) (+ x 4)))

(display (plus4_1 5))
(newline)
(display (plus4_2 5))
(exit)

;lambda可以用作运算符
(display ((lambda (x y z) (+ x y (* z z))) 1 2 3))
(exit)  ; 12


;==3.2.3复合类型============
(define x (cons 1 2))   ; cons创建pair数据
(display x)    ; (1 . 2)
(newline)
(display (car x))   ; 1
(newline)
(display (cdr x))   ; 2
(exit)     


(display 
    (cons 1
      (cons 2
            (cons 3
                  (cons 4 '())))))
(exit)     ; (1 2 3 4)


(display (list 1 2 3 4))
(exit)     ; (1 2 3 4)

;定义序列操作(长度和元素选择)
(define (length items)    ;长度选择
    (if (null? items)
        0
        (+ 1 (length (cdr items)))))

(define (getitem items n)
    (if (= n 0)
        (car items)
        (getitem (cdr items) (- n 1))))

(define squares (list 1 4 9 16 25))

(display (length squares))      ; 5
(newline)
(display (getitem squares 3))   ; 16 
(exit)

;=======3.2.4符号数据===============
(define a 1)
(define b 2)

(display (list a b))  ; 返回(1 2)
(newline) 
(display (list 'a 'b)) ; (a b)
(newline)
(display (list 'a b))  ; (a 2)
(exit)

(display (car '(a b c)))
(newline)
(display (cdr '(a b c)))
(exit)

;=======3.2.5海龟图形=================
(define (repeat k fn) (if (> k 0)
                        (begin (fn) (repeat (- k 1) fn))
                        '()))

(repeat 5
        (lambda () (fd 100)
                    (repeat 5
                            (lambda () (fd 20) (rt 144)))
                    (rt 144)))
;scheme好像没有内置Turtle图形功能

;python版谢尔宾斯三角形见 3.2turtle_sier.py