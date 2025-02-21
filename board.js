const size = 8;

for (let i = 0;i < size; i++){
    let l = [];
    for (let j = 0; j < size; j++){
        if ((i + j) % 2 == 0){
            l[j] = " ";
        } else {
            l[j] = "#";
        }
    }
    console.log(l.join(""));
}
