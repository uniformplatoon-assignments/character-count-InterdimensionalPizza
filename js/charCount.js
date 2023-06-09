exports.charCount = function(str) {

    const getCount=(ltr, str)=>{
        let count=0
        for(let i=0; i<str.length; i++){
            if(str[i]==ltr){
                count++
            }
        }
        return count;
    }

    let manStr=str.replaceAll(" ","")
    manStr=str.split('')
    let listOfLtrs=[]
    let listOfInst=[]
    let answer=[]
    for(let i=0; i< manStr.length; i++){
        if (listOfLtrs.includes(manStr[i])){
            continue
        }
        else{
            listOfLtrs.push(manStr[i])
            listOfInst.push(getCount(manStr[i], manStr))
        }
    }
    listOfInst=listOfInst.sort().reverse()
    listOfLtrs=listOfLtrs.sort()
    for (let j=0; j<listOfInst.length; j++){
        for(let k=0; k<listOfLtrs.length; k++){
            if (getCount(listOfLtrs[k], manStr)==listOfInst[j] && listOfLtrs[k] !==" "){
                answer.push([listOfLtrs[k],listOfInst[j]])
                listOfLtrs[k]=" "
                listOfInst[j]=0
            }
        }
    }
    return answer;
};
