/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let left = 1;
    let right = Math.floor(x/2) + 1;
    let mid;

    while(left <= right ) {
        mid = Math.floor((left+right)/2);
        let sqr = mid* mid;
        if(sqr > x) {
            right = mid-1;
        } else if (sqr < x){
            left = mid+1;
        }else{
            return mid;
        }

    }
    
    return right;
};