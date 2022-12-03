// input
const array = [1,3,10,199999,10,3,2];

function isReverse(array){
    let i = 0,
    l = array.length-1;
    for(;i<(l/2);i++){
        if (array[i]!=array[l-i]){
            return false;
        }
    }
    return true;
}

//display
console.log(isReverse(array));