javascript数组方法中有几个高阶方法，find、filter、some、every、map这几个数组方法的参数均为一个回调函数，对数组中的每个元素进行处理。然后返回结果。

# find
## find是数组中的一个方法，参数为回调函数，结果返回数组中第一个满足要求的元素，如果没有满足要求的元素，则返回undefined。

## find例子

```javascript
const array = [1, 3, 5, 7, 9]

const res1 = array.find(item => {
  return item > 6
})

const res2 = array.find(item => {
  return item > 10
})

console.log(res1)    // 返回大于6的第一个元素7

console.log(res2)    // 没有满足要求的元素，返回undefined
```
# filter
## filter数组方法，参数为回调函数，与find不同的是，可以查找出所有满足要求的元素，并返回一个新的数组，如果没有满足要求的元素，则返回空数组。

## filter例子
```javascript
const array = [1, 3, 5, 7, 9]

const res1 = array.filter(item => {
  return item > 6
})

const res2 = array.filter(item => {
  return item > 10
})

console.log(res1)    // 返回大于6的所有元素7

console.log(res2)    // 返回空数组[]
```
# some
## some数组方法，参数为回调函数，返回布尔值，数组中只要有一个结果满足要求，即返回true，全部都不满足要求则返回false。

## some例子
```javascript
const array = [1, 3, 5, 7, 9]

const res1 = array.some(item => {
  return item === 1
})
const res2 = array.some(item => {
  return item === 2
})

console.log(res1)    // 返回true

console.log(res2)    // 返回false
```
# every

## every数组方法，参数为回调函数，返回布尔值。相比于some方法，some更像或操作符，every更像与操作符。数组中只要有一个结果满足要求，即返回true，全部都不满足要求则返回false。

## every例子
```javascript
const array = [1, 3, 5, 7, 9]

const res1 = array.every(item => {
  return item > 0
})
const res2 = array.every(item => {
  return item > 2
})

console.log(res1)    // 返回true

console.log(res2)    // 返回false
```
# map
## map数组方法，参数为回调函数，将回调函数中处理后的结果返回数组。

## map例子
```javascript
const array = [1, 3, 5, 7, 9]

const res = array.map(item => {
  return item + 1
})

// 返回一个新的数组，每个数组元素都加1，返回值为[2, 4, 6, 8, 10]
console.log(res)
```
