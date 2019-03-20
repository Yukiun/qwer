1. #### 标题
    一个#表示一级标题，最多6个表示6级标题
    ># h1
    >## h2
    >### h3
    >#### h4
    >##### h5
    >###### h6

---
2. #### 列表
>* 无序列表，用* + -都可以表示
    * 列表
        * 次级
        * 次级
    * 列表
>* 有序列表，用数字.表示，【列表用四个空格分级】
    1. 列表
        1. 次级
        2. 次级
    2. 列表
    3. 列表

---
3. #### 区块引用

    用 ">" 表示引用，多层引用就用多个 ">"
    ``` 
    > 一级引用
    >> 二级引用
    >>> 三级引用
    ```
    > 一级引用
        >> 二级引用
            >>> 三级引用

---
4. #### 分割线

    用三个 * (或 - 或 _)表示
    > 
        ***
        ---
        ___
    ***
    ---
    ___

---        
5. #### 链接
 - 链接文字放到中括号"[]"里，链接地址放到小括号中，比如：[链接文字]\(http://www.example.com) 结果是这样：[链接文字](http://www.example.com)
 - 链接地址放到<>里，比如：
    &lt;http://www.example.com&gt; 结果是这样：<http://www.example.com>
---
6. #### 图片
!\[图片文字](url)

    与链接一样只是在开头多了个!
    比如：!\[面灵气](https://yys-fans.fp.ps.netease.com/file/5bc2240e6f049459bd36d994IaCEkYtx?fop=imageView/2/w/845/h/604)
   结果是：
   ![面灵气](https://yys-fans.fp.ps.netease.com/file/5bc2240e6f049459bd36d994IaCEkYtx?fop=imageView/2/w/845/h/604)

---
7. #### 代码框
开头结尾使用反引号\`\` ,单行用一个，多行使用三个
    1. 单行：
        > \`print("hello world")`

        `print("hello world")`

    2. 多行
        >   (貌似也有四个空格)
            for(let i in skills){
                console.log('wanderful skill: ' + skills[I]);
            }

        >   
            npm install webpack

---
8.表格
用:的不同位置来改变对齐方式，默认左对齐(:-),右对齐(:-),居中对齐(:-:)
- 方式一

        |head|head|head| 
        |:----:|:----|----:|
        |center|left|right|
        |center|left|right|
        |center|left|right|

|head|head|head|
|:----:|:----|----:|
|center|left|right|
|center|left|right|
|center|left|right|
- 方式二
            
        head|head|head
        ---|:---:|---|
        cell|cell|cell
        cell|cell|cell
        
head|head|head
---|:---:|---|
cell|cell|cell
cell|cell|cell

- 方式三

        head|head|head
        -|-:|:-:|
        cell|cell|cell
        cell|cell|cell

head|head|head
-|-:|:-:|
cell|cell|cell
cell|cell|cell

---
9. 强调

    开头结尾用\*(或者_)，\* 表示斜体，\*\*表示加粗，\*\*\*表示斜体加粗

    ```
    *em*
    **strong**
    ***斜体加粗***
    ```
    *em*
    **strong**
    ***斜体加粗***

10.转义

    \反斜杠
---
11.删除线

开头结尾使用~~
    
    ~~待删除~~

~~待删除~~


