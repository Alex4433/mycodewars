function digitize(n) {
    n = String(n);
    let array = n.split('');
    array = array.map(Number);
    return array
}

let n
n = 8675309

console.log(digitize(n))



//    7 kyu
//    Digitize
//
//    Given a non-negative integer, return an array / a list of the individual digits in order.
//
//    Examples:
//
//    123 => [1,2,3]
//
//    1 => [1]
//
//    8675309 => [8,6,7,5,3,0,9]
