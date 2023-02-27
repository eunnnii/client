// const axios = require('axios'); // node
function getHelloWorld() {
    axios.get('http://localhost:3000/',{mode:'cors'}).then((res)=>{
        console.log(res)
    })
}

export {getHelloWorld};