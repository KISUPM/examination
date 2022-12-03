const array = [1,4,9,13,20,5,11];

function getOdd(array){
    return (array.filter(x => x%2!=0)).join(",");
}

console.log(getOdd(array));