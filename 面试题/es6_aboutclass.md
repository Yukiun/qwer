```javascript
class Cash {
    //代码
}
const cash1 = new Cash(105)
const cash2 = new Cash(66)

const cash3 = cash1.add(cash2)
const cash4 = Cash.add(cash1, cash2)
const cash5 = new Cash(cash1 + cash2)
console.log(`${cash3}\n${cash4}\n${cash5}`)
// 期望输出：1元7角1分 1元7角1分 1元7角1分 
```

```
class Cash {
    //代码
    constructor(value) {
        this.num = value
        return this.num
    }
    static format(money) {
        let yuan = money/100 >> 0
        let fen = (money - yuan * 100) / 10 >> 0
        let jiao = money % 10
        return `${yuan}元${fen}分${jiao}角`
    }
    static add(c1, c2){
        return new Cash(c1.num + c2.num)
    }
    add(c2){
        // c2为number
        return Cash.add(this.num += c2)
    }
    toString() {
        return Cash.format(this.num)
    }
    valueOf() {
        return this.num
    }
}
const cash1 = new Cash(105)
const cash2 = new Cash(66)

const cash3 = cash1.add(cash2)
const cash4 = Cash.add(cash1, cash2)
const cash5 = new Cash(cash1 + cash2)
console.log(`${cash3}\n${cash4}\n${cash5}`)
```
使用到的知识点：
- class
  - 构造方法
    - 类实际上是个“特殊的函数”，就像你能够定义的函数表达式和函数声明一样，类语法有两个组成部分：类表达式和类声明。
  - ~~extends(继承)~~
  - static(静态方法)
